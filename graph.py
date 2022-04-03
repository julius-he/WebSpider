import matplotlib.pyplot as plot
from matplotlib.font_manager import FontProperties

# Mac系统苹方字体
font = FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

# 绘制水平直方图
def horizHistogram(xData, yData, title="", xTitle="", yTitle=""):
    # 创建绘图对象，figsize用于指定绘图对象的宽高
    plot.figure(figsize=(15, 8))
    # 设置字体，避免中文乱码
    # plot.rcParams["font.sans-serif"] = "SimHei"
    # 图的标题
    plot.title(title, fontsize=20, fontproperties=font)
    # x轴标题文字
    plot.xlabel(xTitle, fontsize=18, fontproperties=font)
    # y轴标题文字
    plot.ylabel(yTitle, fontsize=18, fontproperties=font)
    # x轴刻度标签，图的数据
    plot.barh(range(len(xData)), xData)
    # y轴刻度标签
    plot.yticks(range(len(yData)), yData, fontproperties=font)
    # 添加数据标签
    for x, y in enumerate(xData):
        plot.text(y + 0.1, x, "%s" % y, va='center')
    # 显示图表
    plot.show()

# 绘制垂直直方图
def verticalHistogram(xData, yData, title="", xTitle="", yTitle=""):
    # 创建绘图对象，figsize用于指定绘图对象的宽高
    plot.figure(figsize=(15, 8))
    # 设置字体，避免中文乱码
    # plot.rcParams["font.sans-serif"] = "SimHei"
    # 图的标题
    plot.title(title, fontsize=20, fontproperties=font)
    # x轴标题文字
    plot.xlabel(xTitle, fontsize=18, fontproperties=font)
    # y轴标题文字
    plot.ylabel(yTitle, fontsize=18, fontproperties=font)
    # y轴刻度标签，图的数据
    plot.bar(range(len(yData)), yData)
    # x轴刻度标签
    plot.xticks(range(len(xData)), xData, fontproperties=font, rotation=20)
    # 添加数据标签
    for x, y in enumerate(yData):
        plot.text(x-0.25, y+1, "%s" % y, va='center')
    # 显示图表
    plot.show()