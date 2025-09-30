#用户可以选三次
#每次生成20个车牌
import random
import string

source =string.ascii_uppercase+string.digits
count=0

while count<3:
    car=[]
    for i in range(20):
        #第一个字母
        char1=random.choice(string.ascii_uppercase)
        char2="".join(random.sample(source,5))
        car_num=f"京{char1}-{char2}"
        car.append(car_num)
        print(i+1,car_num)
    choice=input("请选车牌：").strip()
    if choice in car:
        print(f"恭喜你选到车牌{car_num}")
        break
    else:
        print("输入有误,表将刷新")
    count+=1        
    