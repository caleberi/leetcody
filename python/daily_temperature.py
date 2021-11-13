"""
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to 
wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.
Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

"""

def daily_temperature(temperatures):
    temp_stk=[]
    if len(temperatures)==0:
        return temp_stk
    result = [ 0 for _ in range(len(temperatures))]
    for i in range(len(temperatures)):
        temp = temperatures[i]
        curr_temp = (temp,i)
        if len(temp_stk)<=0:
            temp_stk.append(curr_temp)
        else:
            t,idx =  curr_temp
            lt,lt_idx  = temp_stk[-1]
            while len(temp_stk)>0 and t>lt :
                # calculate the number of day from the future
                dist = idx-lt_idx
                temp_stk.pop()
                result[lt_idx]=dist
                if len(temp_stk):
                    # update the lastest temperature on stack 
                    lt,lt_idx  = temp_stk[-1] 
            temp_stk.append(curr_temp)
    return result

if __name__ == "__main__":
    print(daily_temperature([73,74,75,71,69,72,76,73]))
    print(daily_temperature([30,60,90]))



    
