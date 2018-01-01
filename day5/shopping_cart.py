# -*- coding: utf-8 -*-

salary=int(input("您目前的工资为："))

items_for_buy={'iphone6s': 5800, 'mac book':9000,'coffee': 32,'python book':80,'bicycle': 1500}
thing_list=[]
price_list=[]
shopping_list=[]
yu_e=salary
index_for_buy=0
for item in items_for_buy:
    index_for_buy=index_for_buy+1
    print('%d.  %s    %d\n'%(index_for_buy,item,items_for_buy[item]))
    thing_list.append(item)
    price_list.append(items_for_buy[item])

while True:
    input_index=input("请输入您想买的物品序号或者输入quit退出：")
    if (input_index=='quit'):
        print('您已经购买以下物品：\n')
        for index_shop in shopping_list:
            print('%s %d'%(index_shop,items_for_buy[index_shop]))
        print('您的余额为%d\n'%yu_e)
        print('欢迎下次光临\n')
        break
    else:
        input_index_int=int(input_index)
        input_index_int=input_index_int-1
        if input_index_int in range(5):
            tmp=yu_e-price_list[input_index_int]
            if tmp>=0:
                yu_e=tmp
                shopping_list.append(thing_list[input_index_int])
                print('已将%s加入到你的购物车' %thing_list[input_index_int])
                print('你的余额为%d'%yu_e)
            else:
                print("余额不足")
        else:
            print("unavailable input, please re-input the index you want to buy")
