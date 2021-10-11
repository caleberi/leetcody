"""Circle module containing Circle class"""

class Shape:
    classname = "*Shape*"
    def __init__(self,_x=0,_y=0):
        self.x = _x
        self.y = _y

    def move(self,delta_x,delta_y):
        self.x = self.x+delta_x
        self.y = self.y+delta_y
        return (self.x,self.y)

class Circle(Shape):
    """Circle class"""
    # class variables 
    pi = 3.14159
    all_circles = []
    def __init__(self,radius,_x=0,_y=0):
        """Create a Circle with the given radius"""
        # instance variables
        super().__init__(_x,_y)
        self.radius = radius
        self.__class__.all_circles.append(self)
        print(self.__class__.all_circles)

    def area(self):
        """Determine the area of the circle"""
        # return Circle.pi * (self.radius**2) explicit useage of  pi
        return self.__class__.pi * (self.radius**2) # implicity useage of pi

    def circumference(self):
        """Determine the  circumference of a circle"""
        return  2 * Circle.pi * self.radius 

    @staticmethod
    def total_area():
        total=0
        for c in Circle.all_circles:
            total+= c.area()
        return total

    @classmethod
    def total_circumference(cls):
        total=0
        for c in cls.all_circles:
            total+= c.circumference()
        return total


class Square(Shape):
    def __init__(self,side=1,_x=0,_y=0):
        super().__init__(_x,_y) # or Shape.__init__(_x,_y)  this is  bad since it is hardcoded and not dynamic
        self.side = side
        


class Temperature:
    def __init__(self):
        self._temp_fahr = 0

    @property
    def temp(self):
        return (self._temp_fahr - 32) * 5 / 9
    
    @temp.setter
    def temp(self,new_temp):
        self._temp_fahr = new_temp * 9 / 5 + 32 


c1 =  Circle(1)
c2  = Circle(2)
c1.pi = 3.14
print(c1.pi)
print(c2.pi)
print(Circle.pi)
print(c1.__class__.pi)
print(c1.total_area())
print(Circle.all_circles)
print(c1.move(3,5))
print(c1.move(3,5))
print(c1.classname)
t = Temperature()
print(t.temp)
t.temp = 230
print(t.temp)

#simple example of a destructor in python class

class SpecialFile:
    def __init__(self,file_name,mode):
        self.__file = open(file_name,mode)
        self.__file.write("******** Start of SpecialFile ***********\n")

    def write(self,string):
        self.__file.write(string)

    def writelines(self,string_list):
        self.__file.writelines(string_list)

    def __del__(self):
        print("Entering into autocloser for SpecialFile ")
        self.close()

    def close(self):
        if self.__file:
            self.__file.write("\*************** End of SpecialFile ********\n")
            self.__file.close()
            self.__file= None


def test():
    f = SpecialFile("./input.txt","w")
    f.write("1299249204\n")
    f.close()


test()
# - Added  10 seconds delay to prevent  message collision immediately the dispute is open
# - Added related bank comment on terminal dispute if dispute source is bank 