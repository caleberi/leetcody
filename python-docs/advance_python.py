
class Color:
    def __init__(self,red,green,blue):
        self._red =  red
        self._green = green
        self._blue = blue

    
    def __str__(self):
        return " Color: R={0:d} , G={1:d} , B={2:d}".format(self._red,self._green,self._blue)



color = Color(34,255,23)
print(color)

class LineReader:
    def __init__(self,filename):
        self.file_object = open(filename,"r")
    
    def __getitem__(self,index):
        line = self.file_object.readline()
        if line == "":
            self.file_object.close()
            raise IndexError
        else:
            return line.split("::")[:2]


"""
a list that takes only one type

>>> a = TypedList(1,2,3,4,[84])
>>> a[0] == 1
True
>>> a[1] = 4
>>> a[1]
4
>>>
"""
class TypedList(list):
    def __init__(self,initial_list=[],example_element="str"):
        self.type = type(example_element)
        if not isinstance(initial_list,list):
            raise TypeError("Second argument of the typedlist must be a list")
        for element in initial_list:
            self.__check(element)      
        super().__init__(initial_list)

    def __check(self,element):
        if type(element) != self.type:
                raise TypeError("element of the list must be of type {0}".format(self.type))
    
    def __setitem__(self,idx,element):
        self.__check(element)
        super().__setitem__(idx,element)

    def __getitem__(self,idx):
        return super().__getitem__(idx)

    def __delitem__(self,idx):
        super().__delitem__(idx)


# class Spam:
#     def __init__(self,x):
#         self.x = x
    
#     def show(self):
#         print(self.x)

#OR
# creating a class explicit

def init(self,x):
    self.x=x

def show(self):
    print(self.x)

Spam  =  type("Spam",(object,),{"__init__":init,"show":show})



m_spam = Spam("test")
print(type(m_spam))
print(type(Spam))
print(m_spam.show())
    

x = TypedList(["Hello","Of","Strings"])
print(x)
x[2] = "Life"
print(x)
print(x[1])
del x[2]
print(x)

if __name__ == "__main__":
    import doctest
    doctest.testmod()