class myclass:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def show(self):
        print(self.firstname,self.lastname)

class student(myclass):
    pass
x=student("Mike","Olsen")
x.show()

#p=myclass(2,5)
#p.show()
#print(p.x)
#print(p.y)
#print(myclass)
