
# vbsdinoooki

def find_longest_substring(string):
    start = 0
    end = 0
    max_len = 0
    seen = {}
    while start < len(string) and end < len(string):
        current = string[end]
        if current not in seen:
            seen[current] = end
        elif current in seen:
            temp = end - start
            start = seen[current]+1
            max_len =  max(temp,max_len)
        end += 1
    return max_len

print(find_longest_substring("vbsdinoooki"))
            
print(find_longest_substring("talentupafrica"))
        

