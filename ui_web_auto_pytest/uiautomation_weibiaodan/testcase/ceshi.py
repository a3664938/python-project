# from turtle import *
# #
# # # 设置色彩模式是RGB:
# # colormode(255)
# #
# # lt(90)
# #
# # lv = 14
# # l = 120
# # s = 45
# #
# # width(lv)
# #
# # # 初始化RGB颜色:
# # r = 0
# # g = 0
# # b = 0
# # pencolor(r, g, b)
# #
# # penup()
# # bk(l)
# # pendown()
# # fd(l)
# #
# # def draw_tree(l, level):
# #     global r, g, b
# #     # save the current pen width
# #     w = width()
# #
# #     # narrow the pen width
# #     width(w * 3.0 / 4.0)
# #     # set color:
# #     r = r + 1
# #     g = g + 2
# #     b = b + 3
# #     pencolor(r % 200, g % 200, b % 200)
# #
# #     l = 3.0 / 4.0 * l
# #
# #     lt(s)
# #     fd(l)
# #
# #     if level < lv:
# #         draw_tree(l, level + 1)
# #     bk(l)
# #     rt(2 * s)
# #     fd(l)
# #
# #     if level < lv:
# #         draw_tree(l, level + 1)
# #     bk(l)
# #     lt(s)
# #
# #     # restore the previous pen width
# #     width(w)
# #
# # speed("fastest")
# #
# # draw_tree(l, 4)
# #
# # done()
#
#
from enum import Enum
#
# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#
# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)


# class Gender(Enum):
#     Male = 0
#     Female = 1
# Gender=Enum('Genger',('Male','Female'))
#
# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#
# bart = Student('Bart', Gender.Male)
# print(bart.gender)
# if bart.gender == Gender.Male:
#     print('测试通过!')
# else:
#     print('测试失败!')

# def numbers_less_than_five(num):
#      if num > 5:
#          raise ValueError
#      else:
#          print(f"Number entered is {num}")
# numbers_less_than_five(4)
# numbers_less_than_five(6)

# def log(func):
#     def wrapper(*arg,**kw):
#         print("Start %s()"%func.__name__)
#         return func(*arg,**kw)
#     return wrapper
#
# @log
# def func_a():
#     pass
# def func_b():
#     pass
# def func_c():
#     pass

# def a():
#     pass
# def b():
#     pass
# def c():
#     pass
#
# def decorator(func):
#     print("Start %s"% func.__name__)
#     return func
#
#
# a=decorator(a)



# def canYou(func):
#   def decorator(*args, **kwargs):
#       if int(*args) > 1 and int(*args)  < 10:
#           return func(*args, **kwargs)
#       print('你的年龄不符合要求，不能看')
#   return decorator
#
# @canYou
# def play(a):
#     userAge=a
#     print('开始播放动画片 《喜洋洋和灰太狼》')
#
# play(12)





