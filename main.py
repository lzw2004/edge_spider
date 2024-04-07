"""
lzw
2024年04月07日 19:02:05
"""

from time import sleep
# 导入selenium包
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def edge_spider(text):
    # 打开指定浏览器(不关闭)
    option = webdriver.EdgeOptions()
    option.add_experimental_option("detach", True)
    driver = webdriver.Edge(options=option)
    # 指定加载页面
    driver.get("https://www.google.com.hk/")
    sleep(2)  # 静默2秒

    # 通过id属性获取搜索输入框
    input_text = driver.find_element(By.ID, value="APjFqb")
    # 向搜索输入框内输入selenium
    input_text.send_keys(text)
    sleep(1)  # 静默1秒
    driver.find_element(By.ID, value="APjFqb").send_keys(Keys.ENTER)


print("-------------------------")
print("1_“完全一致”式搜索")
print("2_“特定网站”式搜索")
print("3_“排除特定词汇”式搜索")
print("4_搜索特定大小的图片")
print("5_搜索特定文件类型")
print("6_“通配符”式搜索")
print("7_“AND-OR”式搜索")
print("8_“年份”式搜索")
print("9_查询相关网站")
print("10_Google对某个网站的缓存版本")
print("-------------------------")
num = input("选择你的选项：")

if num == "1":
    text = input("请输入要搜索的内容：")
    text = '"' + text + '"'
    edge_spider(text)

elif num == "2":
    text = input("请输入要搜索的内容：")
    url = input("请输入特定网站的域名：")
    text = f'site:{url} {text}'
    edge_spider(text)

elif num == "3":
    text = input("请输入要搜索的内容：")
    text1 = input("要排除的词汇：")
    text = text + " -" + text1
    edge_spider(text)

elif num == "4":
    text = input("请输入要搜索的内容：")
    imagesize1 = input("请输入图片长：")
    imagesize2 = input("请输入图片宽：")
    text = f'{text} imagesize:{imagesize1}*{imagesize2}'
    edge_spider(text)

elif num == "5":
    text = input("请输入要搜索的内容：")
    filetype = input("请输入文件类型(后缀)：")
    text = f'{text} filetype:{filetype}'
    edge_spider(text)

elif num == "6":
    text1 = input("通配符前的字符：")
    text2 = input("通配符后的字符：")
    text = f'{text1} * {text2}'
    edge_spider(text)

elif num == "7":
    text1 = input("1.AND \n2.OR \n请输入你的选项：")
    if text1 == "1":
        AND1 = input("请输入AND前的字符：")
        AND2 = input("请输入AND后的字符：")
        text = f'{AND1} and {AND2}'
        edge_spider(text)
    elif text1 == "2":
        OR1 = input("请输入OR前的字符：")
        OR2 = input("请输入OR后的字符：")
        text = f'{OR1} or {OR2}'
        edge_spider(text)

elif num == "8":
    text = input('请输入要搜索的内容：')
    agu = input('请输入年份：')
    num = input(f'1.{agu}年之前 \n2.{agu}年之后 \n请输入你的选项：')
    if num == "1":
        text = f'{text} before:{agu}'
        edge_spider(text)
    elif num == "2":
        text = f'{text} after:{agu}'
        edge_spider(text)

elif num == "9":
    url = input("请输入要查询相关网站的域名：")
    text = f'related:{url}'
    edge_spider(text)

elif num == "10":
    url = input('请输入要查询网站的域名：')
    text = f'cache:{url}'
    edge_spider(text)