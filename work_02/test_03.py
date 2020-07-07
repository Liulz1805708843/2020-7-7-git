import random

# 电脑随机出拳
computer = random.randint(1, 3)

user = int(input('请出拳：1/拳头，2/剪刀，3/布'))

if computer == 1:
    computer = '拳头'
elif computer == 2:
    computer = '剪刀'
else:
    computer = '布'

if user == 1:
    user = '拳头'
elif user == 2:
    user = '剪刀'
else:
    user = '布'
print('电脑出的是{},沙雕余鹏出的是{}'.format(computer, user))
if (user < computer ):
    print('沙雕余鹏胜出~_~');
elif (user > computer):
    print('电脑胜出！');
elif(user == computer ):
    print('好吧，平局@_@');



