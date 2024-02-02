from itertools import *

table = '12 15 16 21 24 25 34 42 43 45 51 52 54 56 61 65'
graph = 'аб ба ав ва бв вб бг гб гд дг де ед вд дв вг гв'

for per in permutations('абвгде'):
    new_graph = table
    for i in range(1, 7):
        new_graph = new_graph.replace(str(i), per[i-1])

    if set(graph.split()) == set(new_graph.split()):
        print('1 2 3 4 5 6')
        print(*per)
