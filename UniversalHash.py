import math
import random


def getPrime( m ):   # naive method to find a prime in [m+1, 2m]
    def isPrime (x):
        for i in range(2, int(math.sqrt(x))):
            if x % i == 0:
                return False
        return True

    for p in range(m+1, 2*m+1):
        if isPrime(p):
            return p


class UniversalHashFamily(object):
   def __init__(self, rangeSize):
      self.m = rangeSize
      self.p = getPrime( rangeSize )
      self.a = 0
      self.b = 0
      
   def randomChoose(self):
      self.a = a = random.randint(1, self.p-1)
      self.b = b = random.randint(0, self.p-1)
      return lambda x: ((a * x + b) % self.p) % self.m

   def __str__(self):
       return "h(x) = (%d*x+%d %% %d) %% %d" % (self.a,self.b,self.p,self.m)
  
def buildPerfectHash( S ):
    n = len(S)
    m = 2*n
    
    H = UniversalHashFamily(rangeSize=m)
    h = H.randomChoose()
    print(H)
    
    buckets = [[] for i in range(m)]
    bucketSize = [0] * m
    bucketHash = [ None ] * m
    bucketTable = [[] for i in range(m)]
    
    for i in range(n):
        buckets[ h(S[i]) ] += [ S[i] ]
        bucketSize[ h(S[i]) ] += 1
    print("buckets =", buckets)
    print("bucket sizes = ", bucketSize)

    for i in range(m):
        if (bucketSize[i] > 0):
            F = UniversalHashFamily(rangeSize=int(bucketSize[i]*bucketSize[i]))
            g = bucketHash[i] = F.randomChoose()
            t = bucketTable[i] = [None] * (bucketSize[i]*bucketSize[i])
            for j in range(bucketSize[i]):
                key = buckets[i][j]
                if t[ g(key) ] != None:  # rehashing
                    print("Collision detected: rerun!")
                    exit(1)
                t[ g(key) ] = key
            print("bucket table =", t, "where", F)
    print ("total table space", sum([bucketSize[i]*bucketSize[i] for i in range(m)]))



# test the perfect hash
S = [ 11, 25, 36, 41, 57, 66, 73, 89, 95 ]
print("S =", S)
buildPerfectHash( S )




