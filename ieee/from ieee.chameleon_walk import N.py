from ieee.chameleon_walk import N


class Spy:
    def __init__(self,label,senior=None):
        self.label = label
        self.senior =  senior
    
test_cases = int(input())
number_of_red,number_of_blue,events = tuple(map(input().split(" ")))
names_of_seniors_red = input("").split("")
names_of_seniors_blue = input("").split("")
events_arr  = []
for i in range(events):
    events_arr.append((input().split(" ")))

country_graph_blue = {}
if names_of_seniors_blue[0] not in country_graph_blue.keys():
    country_graph_blue[names_of_seniors_blue[0]] = Spy(names_of_seniors_blue[0])
for i in range(1,len(names_of_seniors_blue)+1):
    if names_of_seniors_blue[i] not in country_graph_blue.keys:
        country_graph_blue[names_of_seniors_blue[i]] = Spy(names_of_seniors_blue[i],names_of_seniors_blue[i-1])

country_graph_red = {}
if names_of_seniors_blue[0] not in country_graph_red.keys():
    country_graph_red[names_of_seniors_blue[0]] = Spy(names_of_seniors_blue[0])
for i in range(1,len(names_of_seniors_blue)+1):
    if names_of_seniors_blue[i] not in country_graph_red.keys:
        country_graph_red[names_of_seniors_blue[i]] = Spy(names_of_seniors_blue[i],names_of_seniors_blue[i-1])



# def cross_over(spy_x,spy_y,country_x,country_y):
#     spy_x.senior = spy_y
#     country_y[spy_x.label] = spy_x
#     country[spy_x.]

# for evnt in events_arr:
#     d,x,y = evnt
#     if d == "w":
        
#     else:
#         spy_x = country_red[x] if x.startsWith("R") else country_blue[x]
#         spy_y = country_red[x] if x.startsWith("R") else country_blue[x]
#         if spy_x.name.startsWith("R"):
#             cross_over(spy_x,spy_y,country_blue)
#         else:
#             cross_over(spy_x,spy_y,country_red)

