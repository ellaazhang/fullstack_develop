def triangle(n):
    i = 1
    while i <= n:
        m=0
        while m < i:
            if m == i-1:
                print("#")
            else:
                print("#",end='')
            m = m+1
        i = i+1

triangle(3)
