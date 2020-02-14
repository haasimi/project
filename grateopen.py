import requests
from bs4 import BeautifulSoup

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('http://ecos.bok.or.kr/api/StatisticSearch/"#key"/xml/kr/1/100/111Y002/YY/1970/2018/20101/',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

x_list = []
y_list = []

for i in soup.find_all('row'):
    time = i.select_one('time').text
    grate = i.select_one('data_value').text

    print(time, grate)
    print("구분선 —")

    x = float(time)
    y = float(grate)
    print(x, y)

    x_list.append(x)
    y_list.append(y)

plt.plot(x_list, y_list, linewidth=3.0, color = 'b', marker='o')

plt.xlabel("Year")
plt.ylabel("Growth Rate")
plt.title("GDP Growth Rate")

plt.grid(True, axis='x', color='pink', alpha=0.5, linestyle='--')
plt.grid(True, axis='y', color='gray', alpha=0.5, linestyle='--')

plt.hlines([0, 7.5], 1970, 2018, color='r')

style = dict(size=15, color='red')

ax.annotate("IMF Crisis(-5.1)", xy = (1998, -5.1), xycoords='data', **style)
ax.annotate("1987(12.7)", xy = (1987, 12.7), xycoords='data', **style)
ax.annotate("1980(-1.6)", xy = (1980, -1.6), xycoords='data', **style)

fig.tight_layout()
plt.show()

