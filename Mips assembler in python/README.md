# MIPS Assembler in python
This is an attempt to create an assembler for mips assembly, using python. The program takes the name of a text file that contains assembly instructions and converts them to a binary file.
## Notes
- All immediate values should be written in decimal form.
- J-type instructions (j, jal) dont work with labels. You must input the exact decimal address of the jump.
- Instructions like lw, sw, sh etc. that use parenthesis must follow a specific syntax like "lw $t4, 4($s0)".
- The programs doesn't show error messages yet.
