class student:
    pass

std1 = student()
std2 = student()

std1.fname = 'anwar'
std1.lname = 'ali'
std1.reg = 'abbcd'
std2.fname = 'arohi'
std2.lname = 'suhohi'
std2.reg = 'efgh'

print(std1.fname)
print(std2.lname)

#object programming

class student:
    def initialize(obj,f,l,r):
        obj.fname=f
        obj.lname=l
        obj.reg=r

std1 = student()
std2 = student()

std1.initialize('anwar','ali','abcd')
std2.initialize('asif','mukhi','efgh')
print(std1.fname)
print(std2.lname)

#onemore with self

class student:
    def initialize(self,fname,lname,reg):
        self.fname = fname
        self.lname = lname
        self.reg = reg

std1 = student()
std2 = student()

std1.initialize('abdu','rahman','abcd')
std2.initialize('asif','ali','efgh')

print(std1.fname)
print(std2.reg)