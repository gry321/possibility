from matplotlib import pyplot as plt
import random


def main():
    COIN_NUMBER = int(input("Enter coin number:"))
    num = input("Enter num to test:")
    num = int(num)
    temp = 0
    lst = []
    bars = []

    ###
    for i in range(num):  # 运行几次？
        for x in range(COIN_NUMBER):  # 每次几个硬币？
            if random.randint(0, 1) == 0:  # 如果朝上
                temp = temp + 1  # 朝上次数加一
        lst.append(temp)  # 把每次结果保存
        temp = 0  # 重置
    ###

    # 用matplotlib的bar，和bar_label（展示概率）
    values_pl = ["{:.4f}".format(lst.count(x) / len(lst))
                 for x in range(COIN_NUMBER+1)]    # 概率
    values = [lst.count(x) for x in range(COIN_NUMBER+1)]     # 每次抛了几次朝上的
    bars = plt.bar(range(len(values)), values, align='center')   # 绘制
    plt.bar_label(bars, values_pl)
    plt.title(f"By GuoRuoYao")
    plt.show()


if __name__ == '__main__':
    main()
