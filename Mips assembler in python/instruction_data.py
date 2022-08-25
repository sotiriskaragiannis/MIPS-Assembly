
# R-type name:{type:... , rs:... , rt: ... , rd: ... , sa: ..., funct: ...}
# I-type name:{type:... , rs:... , rt: ..., label: ..., immed: ..., opcd: ..., rs_in_parenthesis: ...}
# J-type name:{type:... , rs:... , label: ..., opcd: ...}

# rs, rt, rd, sa, label, immed, rs_in_parenthesis in True or False


instruction_data = {"add":{"type":"r", "rs":True, "rt":True, "rd":True, "sa":False, "funct":"100000"},
         "addu":{"type":"r", "rs":True, "rt":True, "rd":True, "sa":False, "funct":"100001"},
         "and":{"type":"r", "rs":True, "rt":True, "rd":True, "sa":False, "funct":"100100"},
         "break":{"type":"r", "rs":False, "rt":False, "rd":False, "sa":False, "funct":"001101"},
         "div":{"type":"r", "rs":True, "rt":True, "rd":False, "sa":False, "funct":"011010"},
         "divu":{"type":"r", "rs":True, "rt":True, "rd":False, "sa":False, "funct":"011011"},
         "jalr":{"type":"r", "rs":True, "rt":False, "rd":True, "sa":False, "funct":"001001"},
         "jr":{"type":"r", "rs":True, "rt":False, "rd":False, "sa":False, "funct":"001000"},
         "mfhi":{"type":"r", "rs":False, "rt":False, "rd":True, "sa":False, "funct":"010000"},
         "mflo":{"type":"r", "rs":False, "rt":False, "rd":True, "sa":False, "funct":"010010"},
         "mthi":{"type":"r", "rs":True, "rt":False, "rd":False, "sa":False, "funct":"010001"},
         "mtlo":{"type":"r", "rs":True, "rt":False, "rd":False, "sa":False, "funct":"010011"},
         "mult":{"type":"r", "rs":True, "rt":True, "rd":False, "sa":False, "funct":"011000"},
         "multu":{"type":"r", "rs":True, "rt":True, "rd":False, "sa":False, "funct":"011001"},
         "nor":{"type":"r", "rs":True, "rt":True, "rd":True, "sa":False, "funct":"100111"},
         "or":{"type":"r", "rs":True, "rt":True, "rd":True, "sa":False, "funct":"100101"},
         "sll":{"type":"r", "rs":False, "rt":True, "rd":True, "sa":True, "funct":"000000"},
         "sllv":{"type":"r", "rs":True, "rt":True, "rd":True, "sa":False, "funct":"000100"},
         "slt":{"type":"r", "rs":True, "rt":True, "rd":True, "sa":False, "funct":"101010"},
         "sltu":{"type":"r", "rs":True, "rt":True, "rd":True, "sa":False, "funct":"101011"},
         "sra":{"type":"r", "rs":False, "rt":True, "rd":True, "sa":True, "funct":"000011"},
         "srav":{"type":"r", "rs":True, "rt":True, "rd":True, "sa":False, "funct":"000111"},
         "srl":{"type":"r", "rs":False, "rt":True, "rd":True, "sa":True, "funct":"000010"},
         "srlv":{"type":"r", "rs":True, "rt":True, "rd":True, "sa":False, "funct":"000110"},
         "sub":{"type":"r", "rs":True, "rt":True, "rd":True, "sa":False, "funct":"100010"},
         "subu":{"type":"r", "rs":True, "rt":True, "rd":True, "sa":False, "funct":"100011"},
         "syscall":{"type":"r", "rs":False, "rt":False, "rd":False, "sa":False, "funct":"001100"},
         "xor":{"type":"r", "rs":True, "rt":True, "rd":True, "sa":False, "funct":"100110"},
         "addi":{"type":"i", "rs":True, "rt":True, "label":False, "immed":True, "opcd":"001000", "rs_in_parenthesis":False},
         "addiu":{"type":"i", "rs":True, "rt":True, "label":False, "immed":True, "opcd":"001001", "rs_in_parenthesis":False},
         "andi":{"type":"i", "rs":True, "rt":True, "label":False, "immed":True, "opcd":"001100", "rs_in_parenthesis":False},
         "beq":{"type":"i", "rs":True, "rt":True, "label":True, "immed":False, "opcd":"000100", "rs_in_parenthesis":False},
         "bgez":{"type":"i", "rs":True, "rt":False, "label":True, "immed":False, "opcd":"000001", "rs_in_parenthesis":False},
         "bgtz":{"type":"i", "rs":True, "rt":False, "label":True, "immed":False, "opcd":"000111", "rs_in_parenthesis":False},
         "blez":{"type":"i", "rs":True, "rt":False, "label":True, "immed":False, "opcd":"000110", "rs_in_parenthesis":False},
         "bltz":{"type":"i", "rs":True, "rt":False, "label":True, "immed":False, "opcd":"000001", "rs_in_parenthesis":False},
         "bne":{"type":"i", "rs":True, "rt":True, "label":True, "immed":False, "opcd":"000101", "rs_in_parenthesis":False},
         "lb":{"type":"i", "rs":False, "rt":True, "label":False, "immed":True, "opcd":"100000", "rs_in_parenthesis":True},
         "lbu":{"type":"i", "rs":False, "rt":True, "label":False, "immed":True, "opcd":"100100", "rs_in_parenthesis":True},
         "lh":{"type":"i", "rs":False, "rt":True, "label":False, "immed":True, "opcd":"100001", "rs_in_parenthesis":True},
         "lhu":{"type":"i", "rs":False, "rt":True, "label":False, "immed":True, "opcd":"100101", "rs_in_parenthesis":True},
         "lui":{"type":"i", "rs":False, "rt":True, "label":False, "immed":True, "opcd":"001111", "rs_in_parenthesis":False},
         "lw":{"type":"i", "rs":False, "rt":True, "label":False, "immed":True, "opcd":"100011", "rs_in_parenthesis":True},
         "lwc1":{"type":"i", "rs":False, "rt":True, "label":False, "immed":True, "opcd":"110001", "rs_in_parenthesis":True},
         "ori":{"type":"i", "rs":True, "rt":True, "label":False, "immed":True, "opcd":"001101", "rs_in_parenthesis":False},
         "sb":{"type":"i", "rs":False, "rt":True, "label":False, "immed":True, "opcd":"101000", "rs_in_parenthesis":True},
         "slti":{"type":"i", "rs":True, "rt":True, "label":False, "immed":True, "opcd":"001010", "rs_in_parenthesis":False},
         "sltiu":{"type":"i", "rs":True, "rt":True, "label":False, "immed":True, "opcd":"001011", "rs_in_parenthesis":False},
         "sh":{"type":"i", "rs":False, "rt":True, "label":False, "immed":True, "opcd":"101001", "rs_in_parenthesis":True},
         "sw":{"type":"i", "rs":False, "rt":True, "label":False, "immed":True, "opcd":"101011", "rs_in_parenthesis":True},
         "swc1":{"type":"i", "rs":False, "rt":True, "label":False, "immed":True, "opcd":"111001", "rs_in_parenthesis":True},
         "xori":{"type":"i", "rs":True, "rt":True, "label":False, "immed":True, "opcd":"001110", "rs_in_parenthesis":False},
         "j":{"type":"j", "opcd":"000010" },
         "jal":{"type":"j", "opcd":"000011"}}



register_table = {"$zero":"00000", "$at":"00001", "$v0":"00010", "$v1":"00011",
                  "$a0":"00100", "$a1":"00101", "$a2":"00110", "$a3":"00111",
                  "$t0":"01000", "$t1":"01001", "$t2":"01010", "$t3":"01011",
                  "$t4":"01100", "$t5":"01101", "$t6":"01110", "$t7":"01111",
                  "$s0":"10000", "$s1":"10001", "$s2":"10010", "$s3":"10011",
                  "$s4":"10100", "$s5":"10101", "$s6":"10110", "$s7":"10111",
                  "$t8":"11000", "$t9":"11001", "$k0":"11010", "$k1":"11011",
                  "$gp":"11100", "$sp":"11101", "$fp":"11110", "$ra":"11111"}