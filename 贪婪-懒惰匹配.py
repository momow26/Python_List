import re


def main():
    # 贪婪匹配 - a.*b
    sentence1 = 'aabacddfbabajdfjskdfjdb'
    m = re.match(r'a.*b', sentence1)
    print(m)
    print(m.group())

    # 懒惰匹配
    sentence2 = 'aabacddfbabajdfjskdfjdb'
    m = re.match(r'a.*?b', sentence2)
    print(m)
    print(m.group())


if __name__ == '__main__':
    main()