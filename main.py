import crawler
from sql import SQLManager
import graph

# 需要爬取的网页的URL
url = "https://www.shanghairanking.cn/rankings/bcmr/2021/080901"
# 获取BeautifulSoup对象
soup = crawler.getSoup(url)
# 获取爬取的数据
dataList = crawler.getData(soup)
# 输出
for item in dataList:
    print(item)

try:
    # 初始化一个SQLManager对象
    sqlManager = SQLManager("localhost:1433", "SA", "123456Kk", "UniversityRanking")
    # 连接数据库
    sqlManager.connect()
except:
    print("连接数据库失败")
else:
    # 先清掉表中的数据
    sqlManager.operate("TRUNCATE TABLE ranking")
    for item in dataList:
        # 执行sql插入语句
        sqlManager.operate("INSERT INTO ranking(rank, univ_name, score) VALUES(%s, '%s', %s)"%(item["rank"], item["name"], item["score"]))
    # 关闭连接
    sqlManager.closeConnet()

# x轴上的数据
scoreList = []
# y轴上的数据
nameList = []
for item in dataList:
    nameList.append(item["name"])
    scoreList.append(float(item["score"]))
# 绘制水平直方图
graph.horizHistogram(scoreList[::-1], nameList[::-1], title="大学排名", xTitle="分数", yTitle="大学名称")
# 绘制垂直直方图
# graph.verticalHistogram(nameList[::-1], scoreList[::-1], title="大学排名", xTitle="大学名称", yTitle="分数")