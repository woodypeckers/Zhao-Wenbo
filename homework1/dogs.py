#encoding:utf-8



class Dog(object): 
    def __init__(self, name, colour): 
        
        self.name = name
        self.colour = colour
       
        print "__init__", self.name  
        print "colour is", colour
    
    def eat(self):
        print self.name, "is eating"
        
    def swim(self):
        print self.name, "is swimming"
        
    def drink(self):
        print self.name, "is drinking"
        
        
d1=Dog("dog1","yello")        
d2=Dog("dog2","black")
d3=Dog("dog3","white")

d1.eat()
d2.swim()      
d3.drink()        
        
        
        
        
        
        
        
        
        