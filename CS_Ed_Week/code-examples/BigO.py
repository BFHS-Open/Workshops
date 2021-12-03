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
