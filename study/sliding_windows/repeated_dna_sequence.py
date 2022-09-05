def findRepeatedDnaSequences(s):
    if len(s)==0:
        return 0
    
    h = {}
    i = 0
    j = 0
    curr_string = ''
    while i < len(s) and j < len(s):
        if j-i+1 == 10:
            if h[s[i:j+1]] not in h:
                h[s[i:j+1]]=1
            else:
                h[s[i:j+1]]+=1
        
