def KarpRabinNoPrime(text, pattern, sigma, prime):
    n = len(text)
    m = len(pattern)
    if m > n:
        return []
    powsigma = pow(sigma, m-1)
    p = 0
    t = 0
    result = []
    print("preprocessing...")
    for i in range(m): 
        p = (sigma*p + ord(pattern[i]))
        print(pattern[0:i+1], "->", p)
        t = (sigma*t + ord(text[i]))
    print("searching...")
    print(t ,)
    for s in range(n-m+1): 
        if p == t: # compare strings
            match = True
            for i in range(m):
                if pattern[i] != text[s+i]:
                    match = False
                    break
            if match:
                result = result + [s]
        if s < n-m:
            t = (t-powsigma * ord(text[s]))  # remove text[s]
            t = (t*sigma + ord(text[s+m]))  # add text[s+m]
            print(t ,)
    print()
    return result

def KarpRabin(text, pattern, sigma, prime):
    n = len(text)
    m = len(pattern)
    if m > n:
        return []
    powsigma = pow(sigma, m-1) % prime
    p = 0
    t = 0
    result = []
    print("preprocessing...")
    for i in range(m): 
        p = (sigma*p + ord(pattern[i])) % prime
        t = (sigma*t + ord(text[i])) % prime
    print(p)
    print("searching...")
    print(t ,) 
    for s in range(n-m+1): 
        if p == t: # compare strings
            match = True
            for i in range(m):
                if pattern[i] != text[s+i]:
                    match = False
                    break
            if match:
                result = result + [s]
        if s < n-m:
            t = (t-powsigma * ord(text[s])) % prime # remove text[s]
            t = (t*sigma + ord(text[s+m])) % prime # add text[s+m]
            print(t ,)
    print()
    return result

print(KarpRabin("abracadabra", "bra", 257, 5 )) # try with prime = 5, 7

print(KarpRabinNoPrime("abracadabra", "bra", 257, 5 )) # try with prime = 5, 7