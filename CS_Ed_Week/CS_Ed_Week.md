# CS Ed Week Curriculum

A workshop for getting young people interested in computer science.

## General Info

- Default language is Python, but participants can use whatever they choose.
- Participants will use Replit for coding.
- Cooperation and teamwork is encouraged!
- Topics covered:
  - Basics of Python
  - Control flow in Python
  - Data Structures
  - Algorithms
  - Debugging

## Part 1: Data Types

- All programming languages have variables that have a variety of purposes.
- Variables can be used to store information, edit existing information, or replace information all together.
- Data types are the aspect of the thing being stored in the variable.
- Sound confusing? Let's explain each data type in further depth, and it'll click.

### How to create variables

- Name of variable goes on the left side of the equal sign, data goes on the the right side.
- Example:
  - `foo = 5`
  - `bar = "hello there"`
  - `baz = True`
  - `foo = bar`

### Integers

- Integers are just what they sound like. 
- This data type stores numbers, specifically whole numbers as that's what an integer is.
- They can be edited using standard math operators, such as addition, subtraction, multiplcation, and division.
  - It's important to note that when doing division on numbers that don't go into each other, the data type switches to a double which will be discussed later.
- Integers are the most common data type that's used in programming because most programming involves a lot of algorithms and math to do complex things which will also be seen later.

### Strings

- Let's say you have the word "apple". The word "apple" is simply a combination of different letters in the English alphabet.
- Other examples of words that can be made include "orange", "program", and "bird".
- Variables that store this type of information are known as String varibales, they store words.
- These variables are commonly used to store information that a user inputs to use at later times, but they can also be used to reuse text that shows up in programs.
- In Python, there are a variety of different methods that can be used to edit these String values, but that's for a later time.

### Boolean

- Take a simple light switch.
- Standard light switches have two states: on or off.
- We store either "on or off" using a boolean variable, but instead of using "on or off," we store "true or false".
- Simple conditional statements such as (x > 9) will be converted into a boolean depending on the integer value in x.
- This "true or false" logic is the basis of all of programming and is the core of several algorithms.
  - It's also important to mention that this is the basis of all computers as well.
  - You may have seen it, it's binary.
  - 1 equates to "true" while 0 equates to false.

### Printing data to stdout

- Many programs rely on some sort of output. That output can take many forms, but one of the most common is just text, also called standard output.
- You can print any data type with the print() function:
  - `print(5)`
  - `print("foo")`
  - `print(True)`
- You can also print the value of a variable by using the variable's name as the first argument to print():
  - `bar = "hello world"`
  - `print(bar)`
- Sometimes you may want to print a message that relies on the value of a variable. For instance, you have a variable containing a username, and every time the user logs in, you want to display a personalized welcome message.
- For this, you use format string, also called f-strings:
  - `username = "Joe"`
  - `print(f"Welcome back {username}!")`

### Arrays vs. Linked Lists

- Computer memory resembles a grid of slots, each with its own address.
- When you want to store multiple multiple items in memory, you can can use either arrays or linked lists.
- Elements in an array are stored one after another in memory. They cannot be divided up and then stored in different locations. If you run out of room for your array, you must find a bigger block of memory.
- One solution to the problem of running out of space is to allocate more space than you need to the array. The downside is that the extra memory may be wasted.
- With a linked list, your data may be stored anywhere in memory. This is because each element also stores the address of the next element. You never have to move your data to a different place in memory.
- Both arrays and linked lists have their weaknesses:
  - Since arrays are one continuous block of elements, reading a particular element is just a matter of knowing its index. Insertions however are much slower, since you have to move all of the elements to the right of it over 1.
  - Reading an element of a linked list takes longer, because you do not know a particular element's position. You instead have to start at the beginning of the list, which will tell you the address of the next element and the next, until you find what you are looking for. Insertions however, are much faster, since you just have to change where one element is pointing to.
  - Deletions have the same characteristics as as insertions in this context.

## Part 2: Lists

### Creating lists

- A syntax for creating a list is as follows:
    - `list_name = [1, 2, 3, 4, 5]`
    - This list has 6 elements.
- It is possible to mix and match data types in a list.
- Each element in a list has a position, and that position is referred to as its index.
- Indices start at zero, so on the list above `list_name[0]` is 1, and `list_name[4]` is 5.

### Manipulating Lists

- Python provides a rich set of list manipulation methods.
- A method is a function. To call a method on a variable, you use what's known as dot notation.
- Here are some common list operations:
  - Appending a list element: `list_name.append(value)`
    - list_name.append(6)
    - list_name -> [1, 2, 3, 4, 5, 6]
  - Popping (removing the last element): `list_name.pop()`
    - popped_item = list_name.pop()    # .pop() also returns the value that was removed, so you can store it in a variable for later
    - list_name -> [1, 2, 3, 4, 5] 
    - popped_item -> 6 
  - Inserting: `list_name.insert(index, value)`
    - list_name.insert(1, 10)
    - list_name -> [1, 10, 2, 3, 4, 5]
  - Removing: 'list_name.remove(index)'
    - list_name.remove(3)
    - list_name -> [1, 10, 2, 4, 5]
      
### Printing lists and their elements

- To print the entire contents of a list, simply supply the name of list as the argument to print()
- To print an specific element of a list, supply the name of the list, followed by its index, to print()
  - pets = ["dog", "cat", "bird"]
  - print(pets)
  - print(pets[2])

__Exercises__: 
- Create a guest list for a party with at least three people. Print an individualized message to each member.
- One of the guests can't make it to dinner, so you need to find someone else to invite. Modify your guest list accordingly.
- You found a bigger dinner table, so you can invite three more people. Add a guest to the beginnig, middle, and end of your list.
- Print new messages for these new guests.

## Part 3: Functions

### General Functions

- Functions are segments of code that are given a name so that they can be refered to by a single command.
- They can be used to cut back on the amount of space you take up by removing repetition like loops did.
  - Unlike loops, the repetition can have all sorts of other comands around each use.
- Using a function is called "calling" a function.
- They also allow for different things to happen each call if given parameters.
  - Parameters are input values of functions.
    - They can be used to change what the function will do.
    - Parameters go inside the parenthesis of the function call.
      - ex: moveDistance(12)

### Helper Functions

- These are a specific kind of function that is made to help do a task.
  - ex: turnAround();
- These are mainly to remove repetition but can still be used to do more complex things

#### Setter Functions

- These are a specific kind of helper function that sets values to things.
  - They can set something to a specific value.
    - ex: setToZero()
  - They can set something relative to its current value.
    - ex: addOneToValue()
  - They can even be set or changed relative to a parameter.
    - ex: addToValue(3)

### Getter Functions

- These are another kind of function that return an output.
  - You can store the value they return in a variable.
    - ex: num = power(2, 3)
      - num is set to the output of power(2, 3)
  - You don't always have to store the value being returned.
    - This is done when you have a mix between a helper and getter function and don't need the value on this call.
- They can also be used to give information to places where it normally can't be accessed.

### Recursion

- Recursion is calling a function within itself.
- Similar to loops, it allows the code within the function to be done over and over again.
  - Typically something would be changing so that it doesn't go on forever.
  - Sometimes they are used to have something repeate forever.
    - For example if you made the code for a game but wanted to have the game restart whenever it finishes.

__Exercises__: 
- Create a function that takes an integer argument, and returns its square.
- Create a function takes an integer 'x' and a string and returns a list of 'x' elements, where each element is the string.
  - Example input: function(5, "Lorem")
  - Example output: ["Lorem", "Lorem", "Lorem", "Lorem", "Lorem"]
- Create a function that takes a string and return a list of characters as its elements.
  - Example input: function("Hello")
  - Example output: ['H', 'e', 'l', 'l', 'o']
- Create a function that takes a list of integers and and removes all integers greater than 5
## Part 4: Data Structures and Algorithms

### Binary Search

- Takes a sorted list of elements; if the element you are searching for is in the list, it returns the position.
- The goal of a binary search is to find the elements in as few guesses as possible.
  - Think of a number guessing game, where you have to guess the number the other person is thinking, between 1-100. They then tell you if its too high or too low.
  - You could start guessing 1, 2, 3, 4, 5... until you get the number
  - Or, you could start with the middle number and eliminate half of the possible results.
    - For numbers 1-100, your first guess would be 50.
    - The person says 50 is too high. Your new list of numbers is 1-49. You guess 25.
    - The person says 25 is too high. Your new list of numbers is 1-24. The middle value is 13.
    - The person says 13 is too high. Your new list of numbers is 1-12. The middle value is 7.
    - The person says 7 is too high. Your new list of numbers is 1-6. You guess 4.
    - The person says 4 is too high. Your new list is 1-3. You guess 2.
    - The person says 2 is too high. __Therefore, correct value is 1.__
  - For a list of 100 elements, binary search will never take more than 7 steps, or guesses. Simple search on the other hand, where you guess each element in order, can take as many guesses as there are elements.

__Exercise:__ Write your own implementation of binary search

### Big O Notation

- Tells us how fast an algorithm is.
- Not a measure of time like seconds, but how many operations it will take to search through or sort through a list of *n* elements.
- Different algorithms' run times grow at different rates.
- Assuming one operation takes 1ms:

![Big O growth rates](img/bigO.png "Simple Search vs. Binary Search")

- Here is what Big O notation looks like:

![What Big O notation looks like](img/bigO_notation.png "Big O Notation")

- Common Big O run times:
  - O(log *n*), known as *log time* - binary search
  - O(n), known as *linear time* - simple search

![graphs of algorithms](img/graphs.png "Graphs of different algorithms")

- What is a logarithm?
  - Logs are like a flip of exponents.
  - log<sub>10</sub>100 means "How many 10s must we multiply to get 100?" The answer is 2.
 
![logarithm table](img/logarithms.png "logarithms table")

  - log without a subscript means log<sub>2</sub>

__Exercise:__
```python
my_list = [1, 2 , 3 , 4, 5, 6, 7, 8]

def example1(values):
  print(values[0])
""" What is the Big O notation for example 1? """
example1(my_list)

def example2(values):
  for i in values:
    print(values[i])
""" What is the Big O notation for example 2? """
example2(my_list)

def example3(values):
  for i in values:
    for j in values:
      print(i, j)
""" What is the Big O notation for example 3? """
example3(my_list)
```


### Selection Sort

- Say you have a list of games on your computer, each with the number of hours played. You want to sort them from most played to least played.
- Go through the entire list and take out the most played game. Put that game in a second list, the sorted list.
- Go through the unsorted list again, finding the next most played game, remove it, and place it in the sorted list, after the most played game. Repeat until the unsorted list is empty. You just performed selection sort!
- How would you represent selection sort in Big O notation? 
  - Each time you go through the unsorted list, it takes O(n) time.
  - You must go through the unsorted list 'n' times, one time for each game.
  - So in Big O notation, its O(n * n), or O(n<sup>2</sup>)

__Exercise:__ Write your own implementation of selection sort


Credits: *Grokking Algorithms* by Aditya Y. Bhargava
