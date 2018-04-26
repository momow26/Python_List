# 正则表达式 -  工具 - 定义字符串的匹配模式
# \w{6,20} - \w 字母数字下划线  {6,20} 最少6个，最多20个
"""
判断用户名是否有效，有效，返回True,无效返回False，
用户名必须由字母、数字、下划线组成，且长度为6-20个字符
"""
# re - Regular Expression
import re


def main():
    # username = 'momowang'
    # match - 从第一个字符开始匹配
    # m = re.match(r'\w{6,20}',username) # 前面需要加r---原始字符串   username -- 返回匹配对象

    # username = 'momowang!@#$%' # 可以匹配成功，因为从开始匹配，成功后就不再考虑后面的内容了
    # m = re.match(r'\w{6,20}', username)

    # username = '!@#$%momowang!@#$%'  # 不能匹配成功，因为不是以字母、数字和下划线开始的
    # m = re. match(r'\w{6,20}', username)

    username = 'momowang'
    # m = re.match(r'^\w{6,20}$', username) # match匹配成功返回内容，匹配不成功，返回None，^字符串的开始，$字符串结束
    # m = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    # 如果一个正则表达式创建了之后，需要反复的利用，应该换如下的写法，效果与上面相同,且性能会更好
    pattern1 = re.compile(r'^[0-9a-zA-Z_]{6,20}$')
    m = pattern1.match(username)
    if m:
        print(m)
        # m.span()  那个部分匹配成功， 得到匹配的范围
        print(m.span())
        print(m.group()) # 取出匹配合适的部分

    # search 从任意位置开始匹配， 匹配完成的字符串，用^$,开始和结尾


if __name__ == '__main__':
    main()