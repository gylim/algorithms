class Percolation:
    
    def __init__(self, n):
        self.n = n
        self.dy = [-1, 1, 0, 0]
        self.dx = [0, 0, -1, 1]
        self.status = [[0]*self.n for i in range(self.n)]
        self.root_list = [i for i in range(self.n**2+2)] # first and last index are virtual
        self.tree_size = [1]*(self.n**2+2) # first and last index are virtual
        for i in range(1, self.n+1):
            self.union(self.root_list[0], self.root_list[i])
            self.union(self.root_list[self.n**2+1], self.root_list[-i-1])
    
    def inside(self, x, y):
        if (0 <= x < self.n and 0 <= y < self.n):
            return True
        return False
        
    def root(self, a):
        while self.root_list[a] != a:
            self.root_list[a] = self.root_list[self.root_list[a]]
            a = self.root_list[a]
        return a
    
    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        if i == j: 
            return "Trees already connected"
        # Updating size array to keep track of tree size
        elif self.tree_size[i] < self.tree_size[j]:
            self.root_list[i] = j
            self.tree_size[j] += self.tree_size[i]
        else:
            self.root_list[j] = i
            self.tree_size[i] += self.tree_size[j]
        return self.root_list, self.tree_size

    def open(self, row, col):
        if self.inside(row-1, col-1):
            self.status[row-1][col-1] = 1
            for j in range(4):
                if self.inside(row-1+self.dx[j], col-1+self.dy[j]) and self.status[row-1+self.dx[j]][col-1+self.dy[j]]:
                    self.union(self.root_list[(row-1+self.dx[j])*self.n + col+self.dy[j]], self.root_list[(row-1)*self.n + col])

        else:
            print("Coordinates out of range!")
    
    def isOpen(self, row, col):
        return self.status[row-1][col-1] == 1
    
    def isFull(self, row, col):
        if col == self.n+1:
            return True if self.root_list[(row-1)*self.n + col] == 0 else False
        elif self.inside(row, col):
            return True if self.root_list[(row-1)*self.n + col] == 0 and self.isOpen(row, col) else False

    def numberOfOpenSites(self):
        total = 0
        for row in self.status:
            total += sum(row)
        return total
    
    def percolates(self):
        return True if self.isFull(self.n, self.n+1) else False

from random import randint as ri

threshold = []
pc = Percolation(10)
while pc.percolates() == False:
    pc.open(ri(1,10),ri(1,10))
threshold.extend(pc.numberOfOpenSites()/(10**2))
print(sum(threshold))

# print(pc.numberOfOpenSites(), pc.isFull(4,1), pc.percolates())
# print(pc.root_list, "\n", pc.tree_size, "\n", pc.status)