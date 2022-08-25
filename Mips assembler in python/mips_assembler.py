from instruction_data import instruction_data, register_table



def TwosComp(str):
    n = len(str)
 
    # Traverse the string to get first
    # '1' from the last of string
    i = n - 1
    while(i >= 0):
        if (str[i] == '1'):
            break
 
        i -= 1
 
    # If there exists no '1' concatenate 1
    # at the starting of string
    if (i == -1):
        return '1'+str
 
    # Continue traversal after the
    # position of first '1'
    k = i - 1
    while(k >= 0):
         
        # Just flip the values
        if (str[k] == '1'):
            str = list(str)
            str[k] = '0'
            str = ''.join(str)
        else:
            str = list(str)
            str[k] = '1'
            str = ''.join(str)
 
        k -= 1
 
    # return the modified string
    return str

def SeperateWordsOfLine(line):
    line = line.replace(',', '')
    return line.split()
    
def BinaryStringToHexString(binary):
    decimal_representation = int(binary, 2)
    return hex(decimal_representation)

def DecimalToNbitBinary(x, n):
    if x >= 0:
        return "0"+format(x, f'0{n-1}b')[-n-1:]
    else:
        num = format(x, f'0{n}b')[-n:]
        return TwosComp(num)

def DetermineBinaryInstruction(line, filename, current_number_of_line):
    words = SeperateWordsOfLine(line)
    binary_form  = ""

    if ":" in words[0]:         # remove label from instruction
        words.remove(words[0])

    if words[0] in instruction_data.keys():

        if instruction_data[words[0]]["type"] == "r":    # for R-type instructions.
            
            opcode = "000000"
            rs = rd = rt = sa = "00000"
            i = 1


            if instruction_data[words[0]]["rd"] == True:
                rd = register_table[words[i]]
                i+=1

            if instruction_data[words[0]]["rs"] == True:
                rs = register_table[words[i]]
                i+=1

            if instruction_data[words[0]]["rt"] == True:
                rt = register_table[words[i]]
                i+=1

            if instruction_data[words[0]]["sa"] == True:
                sa = words[i]
                sa = DecimalToNbitBinary(int(sa), 5)


            binary_form = opcode + rs + rt + rd + sa + instruction_data[words[0]]["funct"]


        elif instruction_data[words[0]]["type"] == "i":      # for I-type instructions.
            rs = rt = "00000"
            immediate = "0000000000000000"
            i = 1


            opcode = instruction_data[words[0]]["opcd"]

            if instruction_data[words[0]]["label"] == False:

                if instruction_data[words[0]]["rt"] == True:
                    rt = register_table[words[i]]
                    i+=1

                if instruction_data[words[0]]["rs"] == True:
                    rs = register_table[words[i]]
                    i+=1

                if instruction_data[words[0]]["immed"] == True:         # immediate is inputed as a decimal
                    if instruction_data[words[0]]["rs_in_parenthesis"] == True:         # supporting syntax like: lw $t4, 4($s0)
                        l = words[i]
                        l = l.replace("(", " ")
                        l = l.replace(")", "")
                        l = l.split()
                        immediate = l[0]
                        rs = register_table[l[1]]
                    else:
                        immediate = words[i]
                        
                    immediate = DecimalToNbitBinary(int(immediate), 16)

                

                binary_form = opcode + rs + rt + immediate

            elif instruction_data[words[0]]["label"] == True:


                if instruction_data[words[0]]["rs"] == True:
                    rs = register_table[words[i]]
                    i+=1

                if instruction_data[words[0]]["rt"] == True:
                    rt = register_table[words[i]]
                    i+=1
                    
                label = words[i]
            
                j = 0

                with open(filename, "r") as f:      # Search for label in file and calculate offset
                    for line in f:
                        if (label + ":" in line):
                            jump_offset = j - current_number_of_line - 1
                        else:
                            j += 1


                jump_offset = DecimalToNbitBinary(jump_offset, 16)

                binary_form = opcode + rs + rt + jump_offset

        elif instruction_data[words[0]]["type"] == "j":      # for J-type instructions.

            opcode = instruction_data[words[0]]["opcd"]
            
            if words[1].isnumeric():                # check if address of jump is given in number form (decimal)
                target = DecimalToNbitBinary(int(int(words[1]) / 4), 26)

            binary_form = opcode + target



    return binary_form
    
    



filename = input("Enter the name of the input text file:")
current_number_of_line = 0

outfile = open("output.bin", "ab")

total_string = ''

with open(filename,"r") as f:
    for line in f:
        bin_array = []
        bin_output = DetermineBinaryInstruction(line, filename, current_number_of_line)
        current_number_of_line += 1
        if bin_output != '':
            hex_output = BinaryStringToHexString(bin_output)
            print(f"%-24s: {bin_output}   {hex_output}"% (line[:-1]))
            

            bin_array.append(int(bin_output[:8], 2))                # Divide the 32-bit instruction to 4 8bit parts.
            bin_array.append(int(bin_output[8:16], 2))              # Convert each string to an integer
            bin_array.append(int(bin_output[16:24], 2))
            bin_array.append(int(bin_output[24:32], 2))
            
            outfile.write(bytearray(bin_array))                     # Convert to bytes and write to binary file

outfile.close()                

