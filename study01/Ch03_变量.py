'''
变量的命名规则
1、变量必须以字母（a - z，A - Z）或下划线（_）开头
2、其他字符可以是字母，数字或 _
3、变量区分大小写
4、Python 关键字不能用作变量名。

命名规范
1、见名知意，尽量使用有语义的单词命名。如使用 password 用作密码，username 用户名。
2、小驼峰式命名法：第一个单词首字母小写其他单词首字母大写，如 userName
3、大驼峰式命名法：全部单词首字母都用大写 ， 如 UserName
4、下划线命名法：每个单词用_下划线连接 ， 如 user_name
'''

Name = '吴老师'
name = '刘德华'
_name = '冯德华'
# 22name = '报错啦'  # 数字不能开头
print(Name, name, _name)
