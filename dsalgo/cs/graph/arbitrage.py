# EIP Book : Page no 484
# https://medium.com/@anilpai/currency-arbitrage-using-bellman-ford-algorithm-8938dcea56ea
"""
 # TODO : this is incomplete


n commodities are traded

        Sheep   Goat    Wheats
Sheep           (3,7)
Goat                    (4,200)
Wheats
"""
import math

currencies = ('PLN', 'EUR', 'USD', 'RUB', 'INR', 'MXN')

def print_path(path):
    ss = ' -> '.join([currencies[i] for i in path[::-1]])
    ss = ' -> '.join([currencies[i] for i in path[::-1]])
    print ss

def sol(matrix):


    dist = {}
    for i in range(len(matrix)):
        dist[i] = float('inf')
    dist[0] = 0
    parent = {}
    for i in range(len(matrix)):
        parent[i] = -1

    def relax_edge(u,v,w):
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            parent[v] = u # we will go to u to v


    # relax edges V-1 times
    for _ in range(len(matrix)-1):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                w = -math.log(matrix[i][j])
                relax_edge(i,j,w)

    # try relaxing it vth time

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            w = -math.log(matrix[i][j])

            if dist[j] > dist[i] + w:
                path = [j,i]
                path_set = set()
                path_set.update([j,i])

                while parent[i] not in path_set:
                    path.append(parent[i])
                    path_set.add(parent[i])
                    i = parent[i]

                path.append(parent[i])
                print_path(path)






if __name__=="__main__":
    rates = [
        [1, 0.23, 0.25, 16.43, 18.21, 4.94],
        [4.34, 1, 1.11, 71.40, 79.09, 21.44],
        [3.93, 0.90, 1, 64.52, 71.48, 19.37],
        [0.061, 0.014, 0.015, 1, 1.11, 0.30],
        [0.055, 0.013, 0.014, 0.90, 1, 0.27],
        [0.20, 0.047, 0.052, 3.33, 3.69, 1],
    ]
    sol(rates)



