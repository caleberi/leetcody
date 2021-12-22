cost =[
    [0,10,75,94],
    [-1,0,35,50],
    [-1,-1,0,80],
    [-1,-1,-1,0]
]


def minimum_cost_travel(cost,source,destination):
    if source == destination or source == destination-1:
        print("min_cost(%d,%d) => %d" %(source,destination,cost[source][destination]))
        return cost[source][destination]
    minimum_cost = cost[source][destination]
    for i in range(source+1,destination):
        temp = minimum_cost_travel(cost,source,i)+ minimum_cost_travel(cost,i,destination)
        print("min_cost(%d,%d) => %d" %(source,destination,temp))
        minimum_cost = min(minimum_cost,temp)
    print("min_cost(%d,%d) => %d" %(source,destination,cost[source][destination]))
    return minimum_cost


if __name__ == "__main__":
    print(minimum_cost_travel(cost,0,len(cost)-1))