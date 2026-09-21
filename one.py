'''
#Dictionary
movies = {
    "name" : "Avengers Endgame",
    "year" : 2019
}
'''
'''TYPE ANNOTATIONS'''

#Typed dictionary
from typing import TypedDict

class Movie(TypedDict):
    name : str
    year : int

movie = Movie(name = "Avengers Endgame",year = 2019)

#union
from typing import union

def square(x : Union[int, float] -> float):
    return x*x





