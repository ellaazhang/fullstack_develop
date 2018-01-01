def triangle_r(n):
    i = n
    while i >= 1:
        m = 1
        while m <= i:
            if m == i:
                print("#")
            else:
                print("#",end='')
            m = m+1
        i = i-1

triangle_r(4)