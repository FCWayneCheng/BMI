#!/usr/bin/python3

height = input('請輸入您的身高：')
height = int(height)
weight = input('請輸入你的體重：')
weight = int(weight)
height = height / 100
BMI = weight / height / height
if BMI < 15:
    print('排骨精')
elif BMI >= 18.5 and BMI < 24:
    print('你算正常')
elif BMI >=24 and BMI < 27:
    print('胖')
elif BMI >=27 and BMI < 30:
    print('有點胖')
elif BMI >= 30 and BMI <35:
    print('有點太胖')
else:
    print('超噁')