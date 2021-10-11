"""
Given an integer array, salaries, salaries[i] represents the salary of the ith employee.
Return the average employee salary not considering the largest or the smallest salary.
Ex: Given the following salaries ...
salaries = [5000, 2000, 3000, 4000], return 3500.00000 ((3000 + 4000) / 2).

"""

from collections import deque

def average_salary(salaries):
    dq_salaries = deque(maxlen=(len(salaries)))
    salaries.sort()
    for salary in salaries:
        dq_salaries.append(salary)
    dq_salaries.popleft()
    dq_salaries.pop()
    total = 0
    for salary in dq_salaries:
        total+=salary
    return  float(total/len(dq_salaries))

if __name__ == "__main__":
    print(average_salary([5000, 2000, 3000, 4000]))