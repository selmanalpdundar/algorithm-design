import math
import random

def getPrime( m ):   # naive method to find a prime in [m+1, 2m]
    def isPrime (x):
        for i in range(2, int(math.sqrt(x))):
            if x % i == 0:
                return False
        return True

    for p in range(2*m, m, -1):
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
  
def dataStream( ):
    n = 1000
    m = 100000
    c = 50  # e/epsilom
    r = 20  # ln (1/delta)

    # create exact counter (for educational purposes)
    F = [ 0  for i in range(n)] 
    
    # create an r x c table T initialized to 0
    T = [[0 for i in range(c)] for j in range(r)] 

    # create r random universal hash function from [n] -> [c]
    H = UniversalHashFamily(rangeSize=c)
    h = [H.randomChoose() for j in range(r)] 

    # simulate a stream truncated to its first m items
    for k in range(m):
        i = random.randint(0, n-1)   # an item
        if (i % 2 == 0):
          F[0] += 1
          for j in range(r):          # what we do instead if we have limited space
            T[j][h[j](0)] += 1 
        else:
          F[i] += 1                    # what we do if we have unlimited  space
          for j in range(r):          # what we do instead if we have limited space
            T[j][h[j](i)] += 1 

    #print the estimation for the items 0..99
    for i in range(100):
        value = m            # +oo
        for j in range(r):          
            value = min( value, T[j][h[j](i)] )
        
        print(F[i], value)   # exact, approximate

        
# test the count min sketch
dataStream()
