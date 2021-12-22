
def parser_in_file():
    number_of_test_cases = int(input())
    cases = []
    for _ in range(number_of_test_cases):
        N = int(input())
        days = []
        for _ in range(N):
            days.append(list(map(int,input().split(" "))))
        cases.append((N,days))
    return cases


def doctor_extreme_schedule():
    tests = parser_in_file()
    for test in tests:
        number_of_days,days = test
        compute_doctor_extreme_schedule(number_of_days,days)
        
            

def compute_doctor_extreme_schedule(number_of_days,schedule):
    record = set()
    for sh in schedule:
        for e in sh:
            record.add(e)

    return list(record) if len(record)==number_of_days else "impossible"        




if __name__ == "__main__":
    doctor_extreme_schedule()