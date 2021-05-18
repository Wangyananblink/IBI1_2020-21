
class Grade(object):
    def __init__(self, name, code, poster, final, score):#This step is used to initialize the function, and construct a class
        self.name = name
        self.code = code
        self.poster = poster
        self.final = final
        self.score = score
#This step show the real function
def Grade_calculator(self):
        self.score = 0 + 0.4 * self.code + 0.3 * self.poster + 0.3 * self.final#We use this command line to calculate the total grade
        print(self.name, ': ', self.score)
x=Grade('Sam',50,90,20,0)#The input is the grade class, containing many numbers
Grade_calculator(x)