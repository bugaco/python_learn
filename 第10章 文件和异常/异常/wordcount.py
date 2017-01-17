def count_words(file_name):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(file_name) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
        print('很遗憾，没有找到"' + file_name + '"这个文件')
    else:
        words = contents.split();
        print('这本书大概有' + str(len(words)) + '个单词')
        print('其中包含' + str(contents.count('the')) + '个 the')
file_names = ['53500.txt', '53500-0.txt']
for file_name in file_names:
    count_words(file_name)