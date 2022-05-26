def sqrt(x: int) -> int:
    return get_square_root(x)


def get_square_root(x:int) ->float:
    i = 0
    j = x 
    mid = i + (j-i) / 2
    while i <= j:
        if mid*mid <= x and (mid+1) * (mid+1) > x :
            return int(mid)
        elif ( mid * mid < x):
            i = mid + 1
        else:
            j = mid - 1
        mid = i + (j-i) / 2
    return 0

print(sqrt(5))
