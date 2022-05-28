'''
This task is about classes and objects in python.
I created the following method for the class "Student":
change_name, change_age, add_track, get_score
'''

class Student:
    
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
    
    # I used a print() function before return, to display the output of the method to the console.
    def change_name(self, name):
        print(name)
        return name
    
    def change_age(self, age):
        print (age)
        return age

    def add_track(self, tracks):
        print(tracks)
        return tracks

    def get_score(self, score):
        print(score)
        return score
        

# Instantiating the Student Class
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(45.0)
