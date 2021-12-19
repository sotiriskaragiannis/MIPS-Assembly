.data  # Data segment 
prompt: .ascii "Enter the number of elements: \0"
space: .ascii " "
.text  # Code segment

.globl main
main:
	la $a0 prompt	#Print the prompt string with syscall 4.
	li $v0 4
	syscall
	
	li $v0 5	# Use syscall 5 for reading integer from a user.
	syscall
	move $t0, $v0 # $t0 will be the limit of the iteration.
	
	li $t1, 2 # t1 is our counter (i)
	li $t2, 0 # t2 holds the previous number.
	li $t3, 1 # t3 holds the current number.
	
	move $a0, $t2	# Print the first number with syscall 1.
	li $v0 1
	syscall
	 
	la $a0 space	# Print the space string with syscall 4.
	li $v0 4
	syscall
	 
	move $a0, $t3	# Print the second number.
	li $v0 1
	syscall
loop:
	beq $t1, $t0, end  # if t1 == 10 end loop
	add $t4, $t3, $t2 # body
	
	addi $t1, $t1, 1 # in C this step would be equal to i++
	
	la $a0 space	#Print the space string with syscall 4.
	li $v0 4
	syscall
	
	move $a0, $t4 # Print the fibonacci number.
	li $v0 1
	syscall
	
	move $t2, $t3	# switch the nnumbers.
	move $t3, $t4
	
	la $a0 space	#Print the space string with syscall 4.
	li $v0 4
	syscall
	
	j loop # jump at the top of the loop
end:
	# Exit
	li $v0, 10	# Load code 10 in to the resgister v0, for exiting the program.
	syscall
