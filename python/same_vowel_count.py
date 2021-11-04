

def same_vowel_count(string):
    if len(string)==0:
        return False
    
    i=0
    j=len(string)-1
    m = (i+(j-i)//2)
    left_half=has_vowel(string,i,m)
    right_half = has_vowel(string,m+1,j)
    return right_half == left_half

def has_vowel(string,i,j):
    count=0
    for k in range(i,j+1):
        if string[k] in "AEIOUaeiou":
            count+=1
    return count


print(same_vowel_count("laptop"))
print(same_vowel_count("computer"))