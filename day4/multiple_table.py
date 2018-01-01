def multiple_table():
    shu1 = 1
    while shu1 <= 9:
        shu2 = 1
        while shu2 <= shu1:
            if shu2 == shu1:
                print("%d*%d=%d"%(shu2,shu1,(shu2*shu1)))
            else:
                str2=str(shu2)
                str1=str(shu1)
                result=str(shu2*shu1)
                print(str1+'*'+str2+'='+ result + ' ', end='')
            shu2=shu2+1
        shu1=shu1+1


multiple_table()