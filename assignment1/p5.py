if __name__ == "__main__" :
    l = []
    print("Enter page numbers from 1 to 25. Press zero to terminate. \n")
    while 1 :
        a = int(input())
        if a == 0 :
            break
        if a > 25:
            print("Enter a number less than 25")
            continue
        l.append(a)
    l.sort()
    print(l)
    i = 0; k = 1; m = []
    while i < len(l) :
        if l[i] != k :
            while k < l[i] :
                m.append(k)
                k = k + 1
        else :
            k = k + 1
            i = i + 1
    while(k <= 25):
        m.append(k)
        k = k + 1
    print("The missing page numbers from the book are as follows \n")
    print(m)

