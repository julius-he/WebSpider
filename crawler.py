import requests
from bs4 import BeautifulSoup

# 获取HTML文本
def getHTMLText(url):
    # 对网页进行GET请求，并设置超时时间30s
    response = requests.get(url, timeout=30)
    # 设置编码方式为UTF-8
    response.encoding = "UTF-8"
    # 网页的内容
    text = response.text
    # 返回网页的内容
    return text


# 获取BeautifulSoup对象
def getSoup(url):
    # 通过URL获取网页文本
    text = getHTMLText(url)
    # 获取BeautifulSoup对象
    soup = BeautifulSoup(text, "html.parser")
    # 返回BeautifulSoup对象
    return soup


# 获取爬取到的数据
def getData(soup):
    # 根据HTML文本结构分析，需要的数据在<div class="body-container"......></div>中
    tag = soup.find("div", {"class": "body-container"})
    # 用来储存解析出来的数据
    result = []
    # 找出所有的item
    for item in tag.find_all("div", {"class": "univ-item"}):
        # 只需要前15名的数据
        if len(result) >= 15:
            break
        # 获取排名数据，去除多余的字符
        rank = item.find("div", {"class": "ranking"}).string.replace(" ", "").replace("\n", "")
        # 获取大学名称数据，去除多余的字符
        name = item.find("a", {"class": "name-cn"}).string.replace(" ", "").replace("\n", "")
        # 获取分数数据，去除多余的字符
        score = item.find("div", {"class": "score"}).string.replace(" ", "").replace("\n", "")
        # 用字典存储
        dictionary = {"rank": rank, "name": name, "score": score}
        # 添加到list中
        result.append(dictionary)
    # 返回爬取到的数据
    return result