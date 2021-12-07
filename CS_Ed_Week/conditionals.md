## Comparators & Conditionals

- Remember Booleans? 1/0, T/F, on/off, yes/no, etc...

- __Comparisons produce a boolean value__ by comparing two peices of data.
  - The keywords in computer languages that communicate this are called operators.
  - Sometimes, as in the case of Python, operators can look like English words.

### Python Logical Operators:

| Operator | Description | Example | Resulting Value |
| :---: |---    |---    | --- |
|and	|Returns True if __both__ sides are True| (5 == 5) __and__ (True != False) | True |
|or	|Returns True if __either__ side is True| (False == False) __or__ (10 > 100) | True |
|not	|Returns the opposite boolean value| __not__(True) | False |


  - The comparison operators look a little more like math, but remember they are just funtions that take two pieces of data, compare them, and return a boolean value.

### Python Comparison Operators:

| Operator | Name | Example | Resulting Value |
| :---:	|---	|---	|--- |
|==	|Equal	|	x == 10 | depends on x |
|!=	|Not Equal	|	False != True | True |
|>	|Greater than	|	100 > 10 | True |
|<	|Less than	|	number1 < number2 | depends |
|>=	|Greater than or equal to |	11 >= 11 | True |
|<=	|Less than or equal to	|	string1.len() <= string2.len() | depends |


- __Conditional statements use booleans to control the flow__ of the code
  - Imagine a train track switch at a fork in the tracks
  - Much like these switches, 'if' statements and other conditionals are tools for controlling what path the CPU takes through the program's code. 

#### Hypothetical train code:
    if (lever == 1)  
      destination = 'Cincinatti'  
    elif (lever == 0)  
      destination = 'New York'  
    else  
      #Error: lever is broken 
      Print('STOP THE TRAIN!!!')




### Some generic if statement syntax in Python:
    # the hash/pound symbol is how you start a comment in Python
    if()
      ...
    ________________________
    # if/else
    
    if ()
      ...
    else 
      ...
    ________________________
    # Nested if/else
    
    if ()
      ...
      if ()
        ...
      else
        ...
    else
      ...
    ________________________
    # if/elif/else

    if ()
      ...
    elif ()
      ...
    elif ()
      ...
    else
      ...
    ________________________
