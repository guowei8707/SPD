import re
from bs4 import BeautifulSoup
import excelIO as eio

# 读html文件
html_fo = open("./dddd.html", "r", encoding='utf-8')
# 只读模式，打开网页，编码模式UTF-8，必须设置不然会报错
html_str = html_fo.read()

# 加载BeautifulSoup
soup = BeautifulSoup(html_str, 'html.parser')

x = soup.find_all("div", class_="mt5")
y = soup.find_all("tbody")
# print(y[0])
print(len(y))

soup_child_1 = BeautifulSoup(str(y[0]), 'html.parser')
z = soup_child_1.find_all("th")
print(len(z))

th_content = []

headline = []
for z_each in z:
    z_find = re.findall(">(.*?)<", str(z_each), re.DOTALL)
    print(z_find[0])
    #z_str = z_find[0].replace(" ", "")
    z_str = ''.join(z_find[0].split())#去空格
    headline.append(z_str)

print("headline", headline)
headline_index = 0
for headline_each in headline:
    axis = ['A1', 'B1', 'C1', 'D1', 'E1']
    eio.writeExcel(headline_each, axis[headline_index])
    headline_index += 1



# print(head_v1.group())

col_list = []
for each in z:
    col_list.append(each)

# print(col_list)


# print(z)


# 流式输出
# head_v1 = re.search('<tbody>(.*)</tbody>', str1, re.DOTALL)
# print(head_v1.group())

# regular_v1 = re.findall('<tbody>(.*?)</tbody>', head_v1.group(), re.DOTALL)
# print(regular_v1[0])

# col = re.search('<th scope=\"col\">(.*?)</th>', regular_v1[0])
# print(col.group())

# for each in regular_v1:
# print('tbody:{}'.format(each[0]))

# regular_v1 = re.findall('<tbody>(.*?)</tbody>', str1, re.DOTALL)
# print(regular_v1)

# regular_v1 = re.findall('<tbody>(.*)</tbody>', str1, re.DOTALL)

# lll = len(regular_v1)

# print(regular_v1)
# print(lll)
