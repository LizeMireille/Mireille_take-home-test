Option 1: Python Task

## Scores
##### Completeness: 3/4
##### Efficiency: 3/4
##### Style: 3/4
##### Documentation: 3/4

## Positive aspects of the submission

Thank you for your submission. The provided code is logical and easy to follow. It is clear that you understood what the task was about and what
the specific criteria were. Excellent job, keep it up!

## Aspects of the submission that could be improved

### Completeness
The code meets the requirements given in the prompt,
however, there is a small mistake in line 5. The sorted() function is called without any argument, which raises a TypeError.
To fix the error, the sorted() function should be called with the string i as its argument.

### Efficiency
For a relatively short list of strings, this code will run efficiently and its simplicity makes it easy to follow.
However, since the code iterates over each string in the input list to sort it correctly, if the input list of strings is very long,
the output speed will be negatively impacted. The code also defines a class and then a function inside the class, and in this case, the
added complexity of using a class is not necessary. If you needed to implement other methods for manipulating lists of strings or anagrams, they
could be added to this same class; however, in this case, using a standalone function may be simpler and more straightforward.

### Style
Python code should be written according to the PEP8 style guide (please see https://realpython.com/python-pep8/).
There are a few style guidelines you did not adhere to.

1. Try working on your indentation, as the inconsistent indentation (starting from line 2) will in fact raise an
IndentationError. Based on PEP8 guidelines, the code indentation should be 4 spaces for each level of logical indentation.  In this code specifically, the def statement (line 2) and the subsequent statements within the groupAnagrams function should be indented with 4 spaces (a tab). The same logic applies for body of the for loop (inside groupAnagrams) as well the if and else statements (inside the for loop) that should also be indented with the appropriate additional 4 space indents.   

2. Remember to consider when to use whitespaces. Typically, two blank lines are used to separate the end of a function or class definition from the next line of code. Therefore, after the groupAnagrams function is closed, you should have two blank lines before the ob1 = Solution() line.

### Documentation
There are no comments added to your code. Comments and documentation are essential for code readability and maintainability.
In cases where the code is fairly self-explanatory, it is important not to add too many unnecessary comments, but please remember
to add relevant comments to help other developers understand what the code does, how it does it, and why.

## Overall feedback
This was a great first attempt. Fixing the minor errors should be very quick and hassle-free. I look forward to the resubmission.
