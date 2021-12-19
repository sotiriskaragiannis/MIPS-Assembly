#  An assembly program that checks if an inputed year is leap or not.

.data  # Data segment 
prompt: .ascii "Enter a year: \0"		# I used the \0 so the assembler knows when to stop the string.
msg1: .ascii " is a leap year\0"
msg2: .ascii " is not a leap year\0"
.text  # Code segment
.globl main
main:
	la $a0 prompt	#Print the prompt string with syscall 4.
	li $v0 4
	syscall
	
	li $v0 5	# Use syscall 5 for reading the year from the user.
	syscall 
	move $t0, $v0   # Move the input, which is stored in $v0 to another register.
	
	li $t1, 400     # $t1 will be used for the condition of 400
	li $t2, 100     # $t2 will be used for the condition of 100
	li $t3, 4       # $t3 will be used for the condition of 4
	
	div $t0, $t1 	# Divides the inputed year with 400.
	mfhi $t4	# $t4 will hold each time the remainder, from hi register.
	beq $0, $t4, output1  # Checks if the remainder is 0, and if True goes to output 1.
	
	div $t0, $t2	# Divides the inputed year with 100.
	mfhi $t4	# $t4 will hold each time the remainder, from hi register.
	beq $0, $t4, output2  # Checks if the remainder is 0, and if True goes to output 2.
	
	div $t0, $t3 	# Divides the inputed year with 4.
	mfhi $t4	# $t4 will hold each time the remainder, from hi register.
	beq $0, $t4, output1 # Checks if the remainder is 0, and if True goes to output 1.
			# else:
	j output2 
	
output1:
 	move $a0, $t0
	li $v0 1	# Use syscall 1 to print the year of the user.
	syscall
	
	la $a0 msg1	# Print that the year is leap.
	li $v0 4
	syscall
	
	j end # Go to the end of the program.
	
output2:
	move $a0, $t0
	li $v0 1	# Use syscall 1 to print the year of the user.
	syscall
	
	la $a0 msg2	# Print that the year is not leap.
	li $v0 4
	syscall
	
	j end # Go to the end of the program.
	
end:
	# Exit
	li $v0, 10	# Load code 10 in to the resgister v0, for exiting the program.
	syscall
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
