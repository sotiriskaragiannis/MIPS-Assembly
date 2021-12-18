.data  # Data segment 
msg: .ascii "The result is \0"			# I used the \0 so the assembler knows when to stop the string.
prompt1: .ascii "Enter the first number: \0"
prompt2: .ascii "Enter the second number: \0"
.text  # Code segment
#Prompt the user for the first input
la $a0, prompt1		# Load the address of the first prompt label to the a0 register for printing string.
li $v0, 4		# Load code 4 in to the resgister v0, for printing the string with the correct syscall
syscall
li $v0, 5		# Load code 5 for syscall about reading an integer.
syscall
move $t0, $v0		# The result of the input goes to register $v0 so wwe move it to $t0 to get another input and add the two together.-

#Prompt the user for the first input
la $a0, prompt2
li $v0, 4
syscall
li $v0, 5
syscall
move $t1, $v0

# Add integers
add $t2, $t1, $t0

# Print result
la $a0, msg	# Load the address of the message label to the a0 register for printing string. 
li $v0, 4	# Load code 4 in to the resgister v0.
syscall		

move $a0, $t2 	# Move the value of the t2 register, the result of the addition to the a0 register for printing integer. 
li $v0, 1	# Load code 1 in to the resgister v0.
syscall

# Exit
li $v0, 10	# Load code 10 in to the resgister v0, for exiting the program.
syscall
