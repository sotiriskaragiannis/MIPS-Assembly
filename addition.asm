.data  # Data segment 
msg: .ascii "The result is "

.text  # Code segment
# Load integers into registers
li $t0, 4
li $t1, 5

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
