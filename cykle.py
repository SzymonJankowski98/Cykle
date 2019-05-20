import time
import random
import sys
sys.setrecursionlimit(10000000)

consistentTab = []
def generator(n, w):
    tab = []
    for i in range(n):
        tab.append([])
        for j in range(int(n)):
            tab[i].append(0)
    y = 0
    while list(set(list(range(len(tab)))) - set(consistentTab)):
        consistentTab.clear()
        x = list(range(1, n))
        random.shuffle(x)
        prev = 0
        for i in x:
            tab[i][prev] = 1
            tab[prev][i] = 1
            prev = i
        tab[0][prev] = 1
        tab[prev][0] = 1
        y = n
        while y < n * (n - 1) / 2 * w:
            a = random.randint(0, n-1)
            b = random.randint(0, n-1)
            c = random.randint(0, n-1)
            while tab[a][b] == 1 or tab[a][c] == 1 or tab[b][c] == 1 or a == b or a == c or b == c:
                a = random.randint(0, n-1)
                b = random.randint(0, n-1)
                c = random.randint(0, n-1)
            tab[a][b] = 1
            tab[b][a] = 1
            tab[a][c] = 1
            tab[c][a] = 1
            tab[b][c] = 1
            tab[c][b] = 1
            y += 3
        isConsistentRec(tab)
    return tab

def isConsistentRec(tab, i=0):
    consistentTab.append(i)
    for j in range(len(tab[i])):
        if tab[i][j] == 1 and j not in consistentTab:
            isConsistentRec(tab, j)
    return

class Euler:
    def __init__(self, tab):
        self.tab = tab
        self.result = []

    def euler_cycle(self, j=0):
        for i in range(len(self.tab)):
            if self.tab[j][i] == 1:
                self.tab[j][i] -= 1
                self.tab[i][j] -= 1
                self.euler_cycle(i)
        self.result.append(j)
        return

class Hamilton:
    def __init__(self, tab):
        self.tab = tab
        self.result = []

    def hamilton_cycle(self, j=0, w=[0]):
        for i in range(len(self.tab)):
            if self.tab[j][i] == 1 and i not in w:
                if len(w)+1 == len(self.tab):
                    if self.tab[i][0] == 1:
                        w.append(i)
                        w.append(0)
                        self.result = w
                        return True
                    else:
                        return
                if self.hamilton_cycle(i, w+[i]):
                    return True
        return

g=generator(10, 0.3)
h=Hamilton(g)
e=Euler(g)
h.hamilton_cycle()
e.euler_cycle()
print(h.result, e.result)