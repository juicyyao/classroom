class Medal(object):
    def __init__(self,nation,gold,silver,bronze):
        self.nation=nation
        self.gold=gold
        self.silver=silver
        self.bronze=bronze
    def add_medal(self,place):
        if place==1:
            self.gold+=1
        elif place==2:
            self.silver +=1
        elif place ==3:
            self.silver += 1
    @property
    def count(self):
        total_num=self.gold+self.silver+self.bronze
        return total_num


    def __str__(self):
        return '%s: 金 %d, 银 %d, 铜 %d, 总 %d' % (
            self.nation, self.gold, self.silver, self.bronze, self.count
        )


if __name__ == '__main__':
    china = Medal("中国", 26, 18, 26)
    us = Medal("美国", 46, 37, 38)
    uk = Medal("英国", 27, 23, 17)
    print(china)
    print(us)
    print(uk)
    print("中国获得一个亚军：")
    china.add_medal(2)
    print (china)
    medal_list=[us,uk,china]
    print(medal_list)
    print("按金牌数排序：")
    order_by_count = sorted(medal_list, key=lambda x: x.gold, reverse=True)
    for o in order_by_count:
        print(o)
    print("按奖牌数排序：")
    order_by_count = sorted(medal_list, key=lambda x: x.count, reverse=True)
    for o in order_by_count:
        print(o)

