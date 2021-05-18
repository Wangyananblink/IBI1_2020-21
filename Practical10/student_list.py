class Student(object):
    def __init__ (self, first_name, last_name, programme):
        #set the first name
        self.first_name = first_name
        #set the last name
        self.last_name = last_name
        #set the undergraduate programme
        self.programme = programme
    def information(self):
        return (self.first_name + '  ' + self.last_name + '   ' + self.programme) #retrun full name and programme
#Here is an example
information1 =Student('Xiaoming', 'Wang', 'BMI')
print(information11.information())