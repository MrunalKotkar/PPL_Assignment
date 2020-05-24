def sumdiv(n) :
    i = 1; new = 0
    while i < n :
        if n%i == 0 :
            new = new + i
        i = i + 1
    return new

if __name__ == "__main__" :
    k = 1; l = 1
    while k <= 8 :
        m = sumdiv(l)
        if m != l :
            p = sumdiv(m)
            if p == l :
                print(l," and ",m," is pair of amicable numbers")
                k = k + 1
                l = m
        l = l + 1
