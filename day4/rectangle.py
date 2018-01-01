def rectangle(n,m):
    kuan=0
    while kuan < m:
        chang=0
        while chang < n:
            if chang == n-1:
                print("#")
            else:
                print("#", end='')
            chang+=1
        kuan=kuan+1


rectangle(4,3)
