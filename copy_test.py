# -*-coding:utf-8 -*-
# copy 拷贝值对象， deepcopy 拷贝引用对象和值对象
import copy
class A:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def __str__(self):
        return "{},{}".format(self.name, self.salary)

class B:
    def __init__(self, class_a, int_value):
        self.class_a = class_a
        self.int_value = int_value
    def __str__(self):
        return "{},{}".format(self.class_a, self.int_value)

a = A(["a","b"], 100)

b = a

c = copy.copy(a)

d = copy.deepcopy(a)

a.name.append("c")
a.salary = 10

print(a)
print(b)
print(c)
print(d)

print("____________")
testb_a = B(d, 100)

testb_b = testb_a

testb_c = copy.copy(testb_a)

testb_d = copy.deepcopy(testb_a)

testb_a.int_value = 1000

testb_a.class_a.name.append("d")

testb_a.class_a.salary = 10000

print(testb_a)
print(testb_b)
print(testb_c)
print(testb_d)

# result
# ['a', 'b', 'c'],10
# ['a', 'b', 'c'],10
# ['a', 'b', 'c'],100
# ['a', 'b'],100
# ____________
# ['a', 'b', 'd'],10000,1000
# ['a', 'b', 'd'],10000,1000
# ['a', 'b', 'd'],10000,100
# ['a', 'b'],100,100


# a = [1, 2, 3, 4, ['a', 'b']] #原始对象
 
# b = a                       #赋值，传对象的引用
# c = copy.copy(a)            #对象拷贝，浅拷贝
# d = copy.deepcopy(a)        #对象拷贝，深拷贝
 
# a.append(5)                 #修改对象a
# a[4].append('c')            #修改对象a中的['a', 'b']数组对象
 
# print( 'a = ', a )
# print( 'b = ', b )
# print( 'c = ', c )
# print( 'd = ', d )



