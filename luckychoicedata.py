# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv

import parsel
import requests
from collections import defaultdict

rcounts = defaultdict(int)
bcounts = defaultdict(int)

for i in range(2007, 2025):
    url = f'https://www.55128.cn/zs/12_96.htm?year={i}'
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    html_data = response.text
    selector = parsel.Selector(html_data)
    trs = selector.xpath('//*[@id="chartData"]/tr')
    for tr in trs:
        res = []
        rr = []
        r1 = tr.xpath('td[@class="chartball_red1"]/text()').getall()
        r2 = tr.xpath('td[@class="chartball_red2"]/text()').getall()
        r3 = tr.xpath('td[@class="chartball_blue"]/text()').getall()
        for r in r1:
            rcounts[r] += 1
        for r in r2:
            rcounts[r] += 1
        for r in r3:
            bcounts[r] += 1
        rr.extend(r1)
        rr.extend(r2)
        rr = sorted(rr)
        res.extend(rr)
        res.extend(r3)

t1 = defaultdict(list)
t2 = defaultdict(list)

print('红色数据:')
sorted_rcounts = sorted(rcounts.items(), key=lambda x: int(x[1]))
for num, count in sorted_rcounts:
    t1[count].append(num)
    print(f"\t{num}: {count}")

print('蓝色数据:')
sorted_bcounts = sorted(bcounts.items(), key=lambda x: int(x[1]))
for num, count in sorted_bcounts:
    t2[count].append(num)
    print(f"\t{num}: {count}")

last_five_lists = list(t1.values())[-5:]
last_two_lists = list(t2.values())[-2:]
print('按出现次数最大得到的号码：\n红：', last_five_lists , "\n蓝：", last_two_lists)

first_five_lists = list(t1.values())[:5]
first_two_lists = list(t2.values())[:2]
print('按出现次数最小得到的号码：\n红：', first_five_lists , "\n蓝：", first_two_lists)

print('所有历史中将数据已经保存完毕!')
print('最新一期的中奖号码是：\t',res[0:])
