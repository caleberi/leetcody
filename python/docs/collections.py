from collections import ChainMap ,Counter,deque
import os, argparse


baseline = { 
    "music": "bach",
    "art": "picaso"
}

adjustment = {
    "art": " van gogh",
    "opera": "carmen"
}

cm = ChainMap(baseline,adjustment)

print("keys: " , list(cm.keys()))

print("values: " , list(cm.values()))

comb =  baseline.copy()

comb.update(adjustment)

print(list(comb))



defaults = {'color': 'red', 'user': 'guest'}

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v is not None}
combined = ChainMap(command_line_args, os.environ, defaults)
print(combined['color'])
print(combined['user'])


colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
 
cnt  =  Counter(colors)



print(cnt)
print(cnt.most_common(1))


d =  deque('ghana')

for elem in d :
    print(elem.upper())


d.appendleft("/cuba")

print(d)
print(d.pop())