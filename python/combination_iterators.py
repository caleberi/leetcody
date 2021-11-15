from itertools import combinations
def sortCombinations(l):
    l = list(l)
    l.sort()
    return l

class CombinationIterator:
    """Design the CombinationIterator class:
    `CombinationIterator(string characters, int combinationLength)` Initializes the object with a string characters of sorted distinct 
    lowercase English letters and a number combinationLength as arguments.
    next() Returns the next combination of length combinationLength in lexicographical order.
    hasNext() Returns true if and only if there exists a next combination.
    
    Example 1:

    Input
    ["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
    [["abc", 2], [], [], [], [], [], []]
    Output
    [null, "ab", true, "ac", true, "bc", false]

    Explanation
    CombinationIterator itr = new CombinationIterator("abc", 2);
    itr.next();    // return "ab"
    itr.hasNext(); // return True
    itr.next();    // return "ac"
    itr.hasNext(); // return True
    itr.next();    // return "bc"
    itr.hasNext(); // return False
    """
    def __init__(self, characters, combinationLength):   
        comb = list(combinations(characters,combinationLength))
        scomb = list(map(sortCombinations,comb))
        
        lcomb = list(map(lambda c :"".join(c),scomb))
        fcomb = list(set(lcomb))
        fcomb.sort()
        self.perms = fcomb
        self.idx = 0

    def next(self) :
        val = self.perms[self.idx]
        self.idx+=1
        return val


    def hasNext(self):
        return self.idx < len(self.perms)

    
    def create_permutation(self,str,dth):
        if dth==0 or len(str)==0:
            return ''

        ret = []
        for i in range(len(str)):
            b = str[i]
            o = self.create_permutation(''+str[:i]+str[i+1:],dth-1)
            if len(o)>0:
                ret.extend([x+b for x in o if b>x[-1]])
                continue
            else:
                o+=b
            ret.append(o)
        return ret

itr =  CombinationIterator("abc", 2)
print(itr.next());    # return "ab"
print(itr.hasNext()); # return True
print(itr.next());    # return "ac"
print(itr.hasNext()); # return True
print(itr.next());    # return "bc"
print(itr.hasNext()); # return False

