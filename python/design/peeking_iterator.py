class PeekingIterator:
    def __init__(self, iterator):
        def get_elements_in_iterator(iterator):
            ret = []
            while iterator.hasNext():
                ret.append(iterator.next())
            return ret
            
        self.sublist = get_elements_in_iterator(iterator)
        self.pointer = -1
        self.iterator =iterator

    def peek(self):
        return  self.sublist[self.pointer]
        

    def next(self):
        self.pointer+=1
        self.iterator.next()
        return  self.sublist[self.pointer]
        

    def hasNext(self):
        idx = self.pointer+1
        return idx < len(self.sublist)