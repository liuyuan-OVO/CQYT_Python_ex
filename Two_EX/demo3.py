import random
sys_num = random.randint(1, 1000)
while True:
    user_num = int(input("请输入你猜的数字："))
    if user_num > sys_num:
        print("猜大了")
    elif user_num < sys_num:
        print("猜小了")
    else:
        print("恭喜你中奖了")
        break