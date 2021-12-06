# CS Ed Week Curriculum
A workshop for getting young people interested in computer science
## General Info
- default language is Python, but participants can use whatever they choose
- Participants will use Replit for coding
- cooperation and teamwork is encouraged
- Topics covered:
  - Basics of Python
  - Control flow in Python
  - Data Structures
  - Algorithms
  - Debugging

## Part 1: Data Types
- All programming languages have variables that have a variety of purposes.
- Variables can be used to store information, edit existing information, or replace information all together.
- Data Types are the aspect of the things stored in the variable.
- Sound confusing? Let's explain each data type in further depth, and it'll click.
### How to create variable
- Name of variable goes on the left side of the equal sign, data goes on the the right side
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
- Let's say you have the word "apple". The word "apple" is simply a combination of the different letters of the English alphabet.
- Other examples of words that can be made include "orange" or "program" or "bird"
- Variables that store this type of information are known as String varibales, they store words.
- These variables are commonly used to store information that a user inputs to use at later times, but they can also be used to reuse text that shows up in programs.
- In Python, there are a variety of different methods that can be used to edit these String values, but that's for a later time.
### Boolean
- Take a simple light switch.
- Standard light switches have two states: on or off.
- We store either "on or off" using a boolean varibale, but instead of using "on or off," we store "true or false".
- Simple statements such as (x > 9) will be converted into a boolean depending on the integer value in x.
- This "true or false" logic is the basis of all of programming and is the core of several algorithms.
  - It's also important to mention that this is the basis of all computers as well.
  - You may have seen it, it's binary.
  - 1 equates to "true" while 0 equates to false.
### Arrays vs. Linked Lists
- Computer memory resemble a grid of slots, each with its own address
- When you want to store multiple multiple items in memory, you can can use either arrays or linked lists
- Elements is an array are stored one after another in memory. They cannot be divided up and then stored in different locations. If you run out of room for your array, you must find a bigger block of memory
- One solution to the problem of running out of space allocate more space than you need to the array. The downside is that the extra memory may be wasted.
- With a linked list, you data may be stored anywhere in memory. This is because each element also stores the address of the next element. You never have to move your data to a different place in memory.
- Both arrays and linked lists have their weaknesses:
    - Since arrays are one continuous block of elements, reading a particular element is just a matter of knowing its index. Insertions however are much slower, since you have to move all of the elements to the right of it over 1.
    - Reading an element of a linked list takes longer, because you do not know a particular elements position. You instead have to start at the beginning of the list, which will tell you the address of the next element and the next, until you find what you are looking for. Insertion however, are much faster, since you just have to change where one element is pointing to.
    - Deletions have the same characteristics as as insertions in this context

## Part X: Lists
### Creating lists
- A sytax for creating a list is as follows:
    - `list_name = [1, 2, 3, 4, 5]`
    - This list has 6 elements
- It is possible to mix and match data types in a list.
- Each element in a list has a position, and that position is referred to as its index
- Indices start at zero, so on the list above `list_name[0]` is 1, and `list_name[4]` is 5.
### Manipulating Lists
- Python provide a rich set of list manipulation methods
- A method is a function. To call a method on a variable, you use what's known as dot notation
- Here are some common list operations:
    - Appending a list element: `list_name.append(6)`
      - list_name -> [1, 2, 3, 4, 5, 6]
    - Popping (removing the last element): `popped_item = list_name.pop()`
      - list_name -> [1, 2, 3, 4, 5]
      - popped_item -> 6
    - Inserting: `list_name.insert(1, 10)`
      - list_name -> [1, 10, 2, 3, 4, 5]
    - Removing: list_name.remove(3)
      - list_name -> [1, 10, 2, 4, 5]

## Part ?: Loops
- Loops let you run a section of code multiple times.
  - In everyday language, "repeat 5 times", "repeat for each page", "repeat until mixture solidifies", etc.
- There are a few different types of loops:
  - `while <condition>: <do_thing>` checks the `<condition>`, and if it's true, runs `<do_thing>`. It then checks the `<condition>` again, and if it's still true, runs `<do_thing>` again, and so on. When the `<condition>` is false, the `while` loop is exited and the computer moves on to the next thing.
    - ```python
      temperature = 80
      while temperature > 65:
          temperature -= 1
      print(temperature) # prints 65
      ```
    - Note that the `<condition>` is only checked before each time `<do_thing>` is run, not continuously.
    - In pseudocode:
      1. If `<condition>` is false, end.
      2. Run `<do_thing>`.
      3. Go to (1).
    - If you are familiar with other languages, Python doesn't have a "do while" loop.
  - `for <var-name> in <sequence>: <do_thing>` runs `<do_thing>` for each item in `<sequence>`. In each iteration of the loop, the value of `<var-name>` is set to the current item.
    - ```python
      things = ["cats", "dogs", "programming"]
      for thing in things:
          print("I like " + thing)
      # prints:
      # I like cats
      # I like dogs
      # I like programming
      ```
    - Note that the `<sequence>` is not modified.
    - In pseudocode:
      1. If there are no more items in `<sequence>`, end.
      2. Get the next item of `<sequence>` and set the value of `<var-name>` to it.
      3. Run `<do_thing>`.
      4. Go to (1).
    - If you are familiar with other languages, you'll notice this isn't a regular "for" loop, but rather a "for each" loop. Python doesn't have regular "for" loops.
- Sometimes, in the middle of running a loop, you want to skip the rest of the current iteration or the whole loop altogether. This is usually because the current item of a sequence is not useful to you, or you've already found or calculated the value you wanted, or something else.
  - `continue` skips the current iteration of the loop, immediately moving back to the top.
    - ```python
      things = ["cats", "dogs", "programming", "coding", "random stuff"]
      for thing in things:
          if len(thing) > 10:
              continue # if it's more than 10 characters long, we don't like it!
          print("I like " + thing)
      # prints:
      # I like cats
      # I like dogs
      # I like coding
      ```
  - `break` breaks out of the loop entirely, moving on to the next thing.
    - ```python
      has_dogs = False
      things = ["cats", "dogs", "programming", "coding", "random stuff"]
      for thing in things:
          print("Checking " + thing + "...")
          if thing == "dogs":
              has_dogs = True
              break # we already know the list has dogs, we don't need to check the rest!
      # prints:
      # "Checking cats..."
      # "Checking dogs..."

      if has_dogs:
          print("The list has dogs!") # prints
      else:
          print("The list does not have dogs!") # does not print
      ```
- You can nest loops (have a loop within a loop):
  - ```python
    grid = [[0, 1, 0],
            [1, 2, 1],
            [2, 1, 2]] # a list of lists
    for row in grid:
        print("Next row:")
        for number in row:
            print("Checking " + str(number) + "...")
            if number > 1:
                print("Larger than 1!")
                break; # this only breaks out of the inner loop!
            print("Not larger than 1.")
    ```

## Part ?: Functions
### General Functions
- Functions are segments of code that are given a name so that they can be refered to by a single command
- They can be used to cut back on the amount of space you take up by removing repetition like loops did
  - unlike loops the repition can have all sorts of other comands around each use
- Using a function is called "calling" a function
- They also allow for different things to happen each call if given parameters
  - Parameters are input values of functions
  - They can be used to change what the function will do
  - The parameters are put inside the parenthesis of the function
    - ex: moveDistance(12)
### Helper Functions
- These are a specific kind of function that is made to help do a task
  - ex: turnAround();
- These are mainly to remove repition 
  - But can still be used to do more complex things
#### Setter Functions
- These are a specific kind of helper function that sets values to things 
  - They can set something to a specific value
    - ex: setToZero()
  - They can set something relative to its current value
    - ex: addOneToValue()
  - They can even be set or changed relative to a parameter
    - ex: addToValue(3)
### Getter Functions
- These are another kind of function that give back an output
  - You store the value they return in a variable
    - ex: num = power(2, 3)
      - num is set to the output of power(2, 3)
  - You don't always have to store the value being returned
    - This is done when you have a mix between a helper and getter function and don't need the value on this call
- They can also be used to give information to places where it normally can't be accessed
### Recursion
- Recursion is calling a function within itself
- Similar to loops, it allows the code within the function to be done over and over again
  - Typically something would be changing so that it doesn't go on forever
  - Sometimes they are used to have something repeate forever
    - For example if you made the code for a game but wanted to have the game restart whenever it finishes
## Part 3(?): Data Structures and Algorithms
### Binary Search
- Takes a sorted list of elements; if the element you are searching for is in the list, it returns the position.
- The goal of a binary search is to find the elements in as few guesses as possible
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
- Tells us how fast an algorithm is
- Not a measure of time like seconds, but how many operations it will take to search through or sort through a list of *n* elements
- Different algorithm's run times grow at different rates
- Assuming one operation takes 1ms:

![Big O growth rates](img/bigO.png "Simple Search vs. Binary Search")
- Here is what Big O notation looks like:

![What Big O notation looks like](img/bigO_notation.png "Big O Notation")
- Common Big O run times:
    - O(log *n*), known as *log time* - binary search
    - O(n), known as *linear time* - simple search

![graphs of algorithms](img/graphs.png "Graphs of different algorithms")
- What is a logarithms?
  - Logs are like a flip of exponents
  - log<sub>10</sub>100 means "How many 10s must we multiply to get 100?" The answer is 2.
 
![logarithm table](img/logarithms.png "logarithms table")
  - log without a subscript means log<sub>2</sub>

__Exercise:__ Determine Big O times for BigO.py examples.

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
