def is_valid_username(username):
    """
    判断用户名是否有效，有效，返回True,无效返回False，
    用户名必须由字母、数字、下划线组成，且长度为6-20个字符
    """
    if 6 <= len(username) <= 20:
        for ch in username:
            if not ('0' <= ch <= '9' or 'A' <= ch <= 'Z' or 'a' <= ch <= 'z' or ch == '_'):
                return False
        return True
    return False


def main():
    print(is_valid_username('admin'))
    print(is_valid_username('_andmin_'))
    print(is_valid_username('momowang'))
    print(is_valid_username('jhdsjgshdgfewhegjfsfsdf'))
    print(is_valid_username('5454dfd*fdsncxj'))


if __name__ == '__main__':
    main()