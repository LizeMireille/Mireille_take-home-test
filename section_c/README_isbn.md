# Option 4: International Standard Book Numbers

For the Code Challenge I attempted option 4 using python. 
In short, this code validates ISBNs (International Standard Book Numbers) and converts ISBN-10 to ISBN-13 format. 
The code checks if an ISBN number is valid or not and coverts valid ISBN-10 numbers to their ISBN-13 versions. 

# Instructions 
To run and test the solution on Linux, macOS and Windows operating systems; 

### Prerequisites
You need Python (Version 3. ...) and git installed on your system. With Python 3; 

### Step 1
Run the following command in your terminal:
git clone https://github.com/LizeMireille/Mireille_take-home-test.git

### Step 2
Run the following to locate the section_c folder:
cd Mireille_take-home-test/section_c

### Step 3
To run the test suite use this:
python -m unittest test_isbn_final.py
The tests should run and display the results.

### Step 4 
To run the solution use this:
python isbn_final.py
The program will prompt the user to enter an ISBN number.
The program will output whether the ISBN number is valid or not and ask for another ISBN number.
The progam will continue to ask for ISBN number until the user inputs 'exit'

# More detail on the code

The isbn_final.py do have comments included to assist with understanding the logic. It is essentially one function
with one main if, elif and else statement. The first if statement addresses the ISBN-13 inputs and validates them (with another nested if and else statement). The elif statement addresses the 10 digit/ISBN-10 inputs by first considering if the number ends on a X and then checking if it is a valid ISBN-10. If it is, it is converted to ISBN-13 using the Luhn alogrithm to calculate the check/last digit. 

# The worst-case space complexity 

The space complexity refers to the amount of memory space required by an algorithm  to solve a problem. It includes the space used by the input and any additional space used by the algorithm during its execution.

In this , a valid ISBN-10 number with X in position 10 has the worst-case space complexity.

For all inputs that contain anything other than 13 or 10 characters (expluding whitespaces and '-' that is removed first if applicable), the final else statement  will run meaning they do not require as much space as inputs with 13 digits, or 10 characters (specifically, either 10 digits or 9 digits and a 'X' in the [-1] position). 

For a valid ISBN-13 number, the solution creates a list of all the separate digits in the input ISBN-13 number, which requires additional memory proportional to the length of the input ISBN number, which is 13.After determining the product sum using the digits and multipliers witht the zip function, the solution does not require any additional memory to change the ISBN number, since ISBN-13 is the desired format.

However for a valid ISBN-10 number with X in position 10, the solution needs to create a list of all separate digits for poistions 0 -8 in the  number, and add a additional digit 10 for the X character. Then it needs to calculate and store the ISBN-13 version of the number, which is 13 digits long, in order to display it to the user. This requires additional memory proportional to the length of the input ISBN number, which is 10 in this case, plus the additional memory needed to store the resulting ISBN-13 number, which is also 13 digits long.

Therefore, in terms of worst-case space complexity, a valid ISBN-10 number with X in position 10 requires more space than a valid ISBN-13 number.

# References

I consulted some online resources to complete this section, here is some of the main ones:

https://www.geeksforgeeks.org/luhn-algorithm/
https://www.geeksforgeeks.org/program-check-isbn/
https://dev.to/bellatrix/worst-case-and-space-complexity-5gp8
https://www.youtube.com/watch?v=SHIg5UIfBnI
https://www.youtube.com/watch?v=6tNS--WetLI

I also used ChatGPT responses to help identify errors in my code. 
