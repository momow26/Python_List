# 给出一个列表，找出里面的最大数，最小的，找出平均数
# 按照单词的长短排序，短的排前面


def main():
    scores = [95, 78, 62, 99, 45, 32, 80]
    # print(max(scores))
    # print(min(scores))
    # min_scores = max_scores = scores[0] 与下面的一样，不同写法
    min_scores, max_scores = scores[0], scores[0]  # 元组表示
    total = 0
    for score in scores:
        if score > max_scores:
            max_scores = score
        elif score < min_scores:
            min_scores = score
        total += score
    print('最高分：', max_scores)
    print('最低分：', min_scores)
    print('平均分：%.1f' % (total / len(scores)))


if __name__ == '__main__':
    main()

