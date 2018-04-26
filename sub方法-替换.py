import re
# sub - substitute - 替换
#匹配到的话，替换匹配到的东西
def main():
    #sentence1 = '刘强东你个煞笔我草你大妈二姑三姨妈四舅妈，日你姥姥的，Fuck奶茶妹'
    # |---表示分支
    #pure_sent = re.sub('[草操屮日]|刘强东|煞笔|fuck|shit', '*', sentence1, flags=re.IGNORECASE)
    # pure -- 过滤之后的句子  flags= 正则表达式的匹配标记---忽略大小写  flags=re.IGNORECASE 或者flags=re.I
    #print(pure_sent)


    # split 拆分  '\s ---'表示匹配任意空白字符
    sentence2 = 'You go your way, I will go mine!'
    mylist = re.split(r'[ ,!]', sentence2)
    print(mylist)

if __name__ == '__main__':
    main()