import re


# def main():
#     # 两种方法
#     # 1 直接使用
#     # 2 使用多的时候，先创建对象（compile）
#     # match-从头开始 search-任意位置开始，search还可以指定后面的位置
#     pattern = re.compile(r'1[34589]\d{9}')
#     sentence = '我的手机号是13512345678不是13398745632,淑玲的手机号是13545678521,不是521'
#     m = pattern.search(sentence)
#     # 通过span可以找到匹配的位置
#     while m:
#         print(m.group()) # 取出第一个匹配到的号码
#         m = pattern.search(sentence, m.span()[1]) # m.span()[1] 第二个匹配的位置，然后再继续往后搜索，继续下去，直到匹配到所有的
#         # (sentence, m.span()[1])---为一个元组
#
# if __name__ == '__main__':
#     main()

# 如果正则表达式经常用，就先把对象创建出来，
# 如果用一次，就直接用re里面的方法
def main():
    pattern = re.compile(r'(?<=\D)1[345789]\d{9}(?=\D)')
    # (? <= \D) - (?<=exp) -- 断言自身出现的位置的前面能匹配表达式exp
    # (?=\D)- (?=exp) --断言自身出现的位置的后面能匹配表达式exp

    sentence = '我喜欢刘明湘130000000000倍她的手机号是13512345678不是13398745632,淑玲的手机号是13545678521,不是521'
    # mylist = pattern.findall(sentence)  # 列表
    # findall 取到所有的 取整个列表
    # finiter   iter - iterator - 迭代器   -- 做循环，用一个取一个
    # print(mylist)
    for temp in pattern.finditer(sentence):
        print(temp)
        print(temp.span())
        print(temp.group())

if __name__ == '__main__':
    main()