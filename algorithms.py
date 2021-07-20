# UnionFind algorithm with list implementation
class UnionFind:
    def __init__(self, num):
        self.num = num
        self.orphan = [i for i in range(self.num)]
        self.joined = []

    def connected(self, p, q):
        if p in self.orphan or q in self.orphan:
            return False
        else:
            for i in self.joined:
                return True if p in i and q in i else False
    
    def union(self, p, q):
        if p in self.orphan and q in self.orphan:
            self.orphan = [e for e in self.orphan if e not in (p, q)]
            self.joined.append([p, q])
        elif p in self.orphan:
            self.orphan.remove(p)
            for i in self.joined:
                if q in i: i.extend([p])
        elif q in self.orphan:
            self.orphan.remove(q)
            for i in self.joined:
                if p in i: i.extend([q])
        elif self.connected(p,q):
            return "Already joined"
        else:
            a, b = [], []
            for i in self.joined:
                if p in i: a = i
                elif q in i: b = i
            self.joined.remove(a)
            self.joined.remove(b)
            self.joined.append(a+b)
        return self.joined
    
    # question 2 of Interview Questions for Union Find
    def find(self, i):
        if i in self.orphan: return i
        else:
            for j in self.joined:
                if i in j: return max(j)
        
# QuickFind algorithm using a list implementation
class QuickFind:
    def __init__(self, num):
        self.num = num
        self.id = [i for i in range(self.num)]
    
    def connected(self, p, q):
        return self.id[p] == self.id[q]
    
    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]
        for k in range(len(self.id)):
            if self.id[k] == pid:
                self.id[k] = qid
        return "Elements connected!"

# QuickUnion using list implementation, uses a tree-root structure
class QuickUnion(QuickFind):
    def __init__(self, num):
        QuickFind.__init__(self, num)

    def root(self, a):
        while self.id[a] != a:
            a = self.id[a]
        return a
    
    def connected(self, p, q):
        return self.root(p) == self.root(q)
    
    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        self.id[i] = j
        return self.id

# Weighted QuickUnion by size with path compression to prevent creation of long/tall trees
class w_pc_QU(QuickFind):
    def __init__(self, num):
        super().__init__(num)
        self.sz = [1]*self.num

    def root(self, a):
        while self.id[a] != a:
            self.id[a] = self.id[self.id[a]] # path compression
            a = self.id[a]
        return a
    
    def connected(self, p, q):
        return self.root(p) == self.root(q)
    
    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        if i == j: 
            return "Trees already connected"
        # Updating size lstay to keep track of tree size
        elif self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]
        return self.id, self.sz

# question 3 of Interview Questions for Union Find
class Succ_del:
    def __init__(self, n):
        self.S = [i for i in range(n)]

    def rem_succ(self, x):
        try:
            self.S.remove(x)
        except ValueError:
            return print(f'{x} not in S')
        if max(self.S) != x:
            y = x
            while y not in self.S:
                y += 1
            return print(x, y)
        else:
            return print(f'No successor, {x} was the max')

def binarySearch(a, key):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = int(lo + (hi-lo) // 2)
        if key < a[mid]:
            hi = mid - 1
        elif key > a[mid]:
            lo = mid + 1
        else:
            return mid
    return "Not Found"

# question 1 of Interview Questions for Analysis of Algorithms
def threeSum(nums, target):
    nums.sort()
    result = []
    for i in range(len(nums)):
        left = i+1
        right = len(nums) - 1
        while left < right:
            if nums[i] + nums[left] + nums[right] == target:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
            elif nums[i] + nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
    return result

# question 2 of Interview Questions for Analysis of Algorithms
def findBitonic(lst):
    l = len(lst)
    idx = l // 2 + 1
    bitonicPt = 0
    while True:
        if lst[idx] > lst[idx-1] and lst[idx] > lst[idx+1]:
            bitonicPt = idx
            break
        elif lst[idx] > lst[idx-1] and lst[idx] < lst[idx+1]:
            idx += 1
        else:
            idx -= 1
    return bitonicPt

def bitonicSearch(lst, bitonicPt, target):
    if target > lst[bitonicPt]:
        return print("Not Found")
    elif target == lst[bitonicPt]:
        return print(f"Number found at index {bitonicPt}")
    else:
        out = binarySearch(lst[:bitonicPt+1], target)
        if out != "Not Found":
            return print(f"Number found at index {out}")
        new = lst[-(len(lst)-bitonicPt):]
        new.reverse()
        out2 = binarySearch(new, target)
        if out2 != "Not Found":
            return print(f"Number found at index {len(lst) - out2}")
        return "Not Found"

# import random as rand
# sd = Succ_del(100)
# for i in range(50):
#     sd.rem_succ(rand.randint(0, 100-1))
