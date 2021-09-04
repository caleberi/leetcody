def mergeString(str_1,str_2):
    if len(str_1)<0 and len(str_2)<0:
        return ""
    if len(str_1)<0 and len(str_2):
        return str_2
    if len(str_2)<0 and len(str_1):
        return str_1
        
    resulting_string_arr = [str_1[0]]
    i,j=1,0
    while i <len(str_1) and j<len(str_2):
        if (abs(i-j)!=1):
            resulting_string_arr.append(str_1[j])
            i+=1
            continue
        else:
            j+=1
        if  (abs(j-i)==i+1):
            resulting_string_arr.append(str_1[i])
            j+=1
            continue

    print(resulting_string_arr)


mergeString("abc","def")
    
