import math
import random
import binascii

#----------------------------------------------------#
# UNIVERSAL HASHING
#----------------------------------------------------#

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


#----------------------------------------------------#
# PARSE INTO SHINGLES
#----------------------------------------------------#

def computeShingles3( words ):
    print("Shingles of 3 consecutive words and their IDs:")
    shingles = []
    shingleIDs = []
    shingleIDset = set()
    for i in range(len(words) - 2):
        shingle = (words[i] + " " + words[i+1] + " " + words[i+2])
        shingles += [shingle]
        
        # Hash the shingle (use Karp-Rabin as an alternative)
        shingleID = binascii.crc32(str.encode(shingle)) & 0xffffffff
        shingleIDs += [shingleID]
        shingleIDset.add(shingleID)

    print(shingles)
    print(shingleIDs)
    #print shingleIDset
    return shingleIDset

def parse( text ):
    # parse into words
    T = text.split(" ")
    #print T
    S = computeShingles3(T)
    #print S
    print()
    return S

#----------------------------------------------------#
# RESEMBLANCE: JACCARD & MINHASH
#----------------------------------------------------#

def Jaccard( setA, setB ):
    result= float(len(setA.intersection(setB)))/len(setA.union(setB))
    return result
    
def minHash( setA, setB, k ):
    # create k random universal hash functions
    m = len(setA.union(setB))
    H = UniversalHashFamily( rangeSize=(m*m) )  # perfect with prob > 1/2
    h = [H.randomChoose() for i in range(k)]
    # create k-skecthes
    sketchA = [ min( map(h[i], setA) ) for i in range(k) ]
    sketchB = [ min( map(h[i], setB) ) for i in range(k) ]
    print(sketchA)
    print(sketchB)
    count = 0
    for i in range(k):
        if sketchA[i] == sketchB[i]:
            count += 1
    return float(count)/k
    
def resemblance():
    textA = "a rose is a rose is a rose flower"
    textB = "a rose is a flower which is a rose"
    print(textA)
    print(textB)
    print()

    setA = parse(textA)
    setB = parse(textB)
    print("set A =", setA)
    print("set B =", setB)
    print()
    print("set intersection :", setA.intersection(setB))
    print("set union :", setA.union(setB))
    print()

    print("Jaccard (resemblance) :", Jaccard( setA, setB ))
    mH = minHash(setA,setB,3 )
    print("minHash (resemblance) :", mH)


# test minHash sketches
resemblance()
