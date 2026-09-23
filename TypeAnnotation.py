#Dictionary
'''
movies = {
    "name" : "Avengers Endgame",
    "year" : 2019
}
'''
'''TYPE ANNOTATIONS'''

#Typed dictionary
'''
from typing import TypedDict

class Movie(TypedDict):
    name : str
    year : int

movie = Movie(name = "Avengers Endgame",year = 2019)
'''

#union method1
'''
from typing import Union

def square(x: Union[int, float]) -> float:
    return x*x
'''

'''
#Type hints = instructions about what type of data is expected.
list[int]   # type information
list()      # create an actual list
#Type hints make your code much safer and easier to contain
'''
'''
#union method2
from typing import Union

def square(x: int|float) -> int|float:
    return x*x
'''
'''
#Optional
from typing import Optional

def niceMessage(name : Optional[str]) -> None:
    if name is None:
        print("Hey random person!")
    else:
        print(f"Hi there, {name} !")
'''
'''
#Any
from typing import Any

def print_value(x : Any):
    print(x)

print_value("I pretend to be batman in the shower sometimes")
'''

#Lambda Function
#Anonymous functions in python are usually written with Lambda
square = lambda x: x*x   #lambda x:Create a small anonymous function that takes one input called x.
#x * x - This is the value the lambda returns. 
# “Store a function inside square that takes x and returns x * x.”
square(10)

nums = [1,2,3,4]
squares = list(map(lambda x : x*x, nums)) #means run this function on each and every item in the iterable(our iterable in this case is a list)
#A beginner here would have used a for loop. 
#You can challenge yourself to write this in a for loop








