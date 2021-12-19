# An assembly program that calculates and prints the factorial of an inputed number.

.data  # Data segment 
prompt: .ascii "Enter an integer: \0"
msg: .ascii "Factorial of \0"
eq: .ascii " = \0"
error_msg: .ascii "Error! Factorial of a negative number doesn't exist.\0"
.text  # Code segment
.globl main
main:
	la $a0 prompt	#Print the prompt string with syscall 4.
	li $v0 4
	syscall
	
	li $v0 5	# Use syscall 5 for reading the year from the user.
	syscall 
	move $t0, $v0   # Move the input, which is stored in $v0 to another register. 
	
	blt $t0, $0 error  # Checks if input is negative and branches to label error if true.
	li $t1, 1     # Else sets the counter register to 1,
	li $t2, 1     # initializes the register t2 with the value of 1 (t2 is going to be the factorial register)
	j loop             # and jumps to label loop.
	
error:
	la $a0 error_msg	#Print the error message with syscall 4.
	li $v0 4
	syscall
	j end
	
loop:
	bgt $t1, $t0 output  # Ends the loop when the counter (t1) is greater than the input number.
	mul $t2, $t2, $t1   # Multiplies the counter with the factorial so far,
	addi $t1, $t1, 1  # Increases the counter by one.
	j loop
	 
output:
	la $a0 msg	# Print the msg string with syscall 4.
	li $v0 4
	syscall
	
	move $a0, $t0    # Print the inputed number with syscall 1.
	li $v0 1
	syscall 
	
	la $a0 eq	# Print the equal symbol with syscall 4.
	li $v0 4
	syscall
	
	move $a0, $t2    # Print the factorial with syscall 1.
	li $v0 1
	syscall 
	
	j end
	
end:
	# Exit
	li $v0, 10	# Load code 10 in to the resgister v0, for exiting the program.
	syscall
	
