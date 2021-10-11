def maximum_histogram(histogram):
    if len(histogram):
        stack = [0]
        height = [histogram[0]]
        max_area = histogram[0]*1
        for i in range(1, len(histogram)):
            if histogram[i] < height[-1]:
                height = [histogram[i]]
                stack = [i]
            elif histogram[i] >= height[-1]:
                if stack:
                    last = stack[-1]
                    length = last+1-stack[0]
                    _ = stack.pop()
                    stack.append(histogram[i])
                    max_area = max(max_area, length*histogram[i])
                else:
                    stack.append(i)
        print(max_area)
    else:
        return 0


print(maximum_histogram([2, 4, 2, 1]))
