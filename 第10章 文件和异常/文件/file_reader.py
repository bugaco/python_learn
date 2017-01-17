with open('other/hello.txt') as file_object:
    contents = file_object.read() # 读取所有内容
    print(contents)

print('---')
"""第二种写法"""
with open('other/hello.txt') as file_object:
    count = 0
    for line in file_object:# 把所有的内容按行拆开
        print(line.rstrip())
"""第三种写法"""
print('\n第三种写法:')
with open('other/hello.txt') as file_object:
    lines = file_object.readlines() # 把所有的内容按行保存在数组中
for line in lines:
    print(line.rstrip())

"""把文本存储起来"""
print('\n把文本存储起来:')
with open('other/hello.txt') as file_object:
    lines = file_object.readlines()

txt_string = ''
for line in lines:
    txt_string += line
print(txt_string[:] + "...")
print(len(txt_string))
input = input('\n请输入你要查询的内容：')

print('您输入的是：' + input)
input.replace('111', '和尚')
print('修改之后是：' + input)

if input in txt_string:
    print('您输入的内容查到了耶！～')
else:
    print('很遗憾，没有找到～')