#判断QQ号 ，0不能开头，开头的为1-9，后面是任意的数字，最多为12个数字。最少为5位
# [1-9] - 1-9的数字，只能取任意一个 {4,11} 中间不能加空格
# [1-9]\d{4,11}
import re


def main():
    qq = input('请输入qq号：')
    m = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m:  #逻辑取反
        print('请输入有效的QQ号.')
    else:
        print('输入的QQ号正确，请继续')


if __name__ == '__main__':
    main()