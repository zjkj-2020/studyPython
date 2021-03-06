# 元组操作 不能进行修改、增加、删除   只能进行查找（一般是使用切片）
'''
元组：是一种不可变的序列，在创建之后不能做任何的修改
1：不可变
2：用（）创建元组类型，数据项用逗号来分割
3：可以是任何的类型
4：当元组中只有一个元素时，要加上逗号，不然后解释器会当做其他类型来处理
5：同样可是支持切片操作
'''
print('--------------------1、元组 创建（注意：当元组中只有一个元素时）-----------------------')
tupleA = ()
print(type(tupleA))
tupleA = ('abcd')
print(type(tupleA))
tupleA = ('abcd',)  # 当元组中只有一个元素时，要加上逗号，不然后解释器会当做其他类型来处理
print(type(tupleA))
tupleA = ('abcd', 89, 9.12, 'peter', [11, 22, 33])
print(type(tupleA))

print('--------------------2、元组 遍历-----------------------')
print('for 循环遍历:', end='')
for item in tupleA:
    print(item, end=' ')
    pass

print()
print('切片截取:', tupleA[2:4])
print('逆序打印：', tupleA[::-1])  # 步长为-1时，逆序打印

print('反转字符串 每隔 1 个取一次：', tupleA[::-2])  # 表示反转字符串 每隔1 个取一次
print('反转字符串 每隔 2 个取一次：', tupleA[::-3])  # 表示反转字符串 每隔 2 个取一次

print('倒着取下标 为-2 到 -1 区间的：', tupleA[-2:-1:])  # 倒着取下标 为-2 到 -1 区间的  左不包含，右包含
print('倒着取下标 为-4 到 -2 区间的：', tupleA[-4:-2:])  # 倒着取下标 为-2 到 -1 区间的

print('---------------------3、元组不可修改，但可修改里面的列表------------------------')
# tupleA[0]='PythonHello'  #错误的
print(type(tupleA[4]))  # <class 'list'>
tupleA[4][0] = 285202  # 可以对元组中的列表类型的数据进行修改
print(tupleA)

print('---------------------4、元组和range方法------------------------')
tupleC = tuple(range(10))
print(tupleC)

print('---------------------统计元素出现的次数------------------------')
print(tupleC.count(4))  # 可以统计元素出现的次数
