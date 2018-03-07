class UnionFind():
    def __init__(self, N):
        # negative value: represents the root of a tree; its absolute value is the size of the tree
        # positive value: the parent's index
        self.vertices = [-1 for _ in range(N+1)]

    def find(self, v):
        if self.vertices[v] < 0:
            return v
        else:
            # path compression
            self.vertices[v] = self.find(self.vertices[v])
            return self.vertices[v]

    def union(self, a, b):
        s1 = self.find(a)
        s2 = self.find(b)
        if s1 == s2: # a and b is in the same tree
            return False
        else:
            if self.vertices[s1] <= self.vertices[s2]: # the tree including a is bigger
                self.vertices[s1] += self.vertices[s2] # update the size of the bigger tree
                self.vertices[s2] = s1
            elif self.vertices[s1] > self.vertices[s2]: # the tree including b is bigger
                self.vertices[s2] += self.vertices[s1] # update the size of the bigger tree
                self.vertices[s1] = s2
            return True

N, Q = map(int, input().split())
uf = UnionFind(N)

for _ in range(Q):
    p, a, b = map(int, input().split())
    if p == 0: # union query
        uf.union(a, b)
    else: # judge query
        if uf.find(a) == uf.find(b):
            print("Yes")
        else:
            print("No")
