from matplotlib import pyplot as plt
    # from ... as ... 简化pyplot 为 plt
x=range(2,26,2)
    # 数据x，从2到26,2.4.6...24，间隔2，无26
y=[15,13,14.5,17,20,25,26,26,27,22,18,15]

# 设置图片大小，宽和高，分辨率dpi：每英寸点的个数，越大越清晰
plt.figure(figsize=(10,6),dpi=80)

# plot命令绘折线图
plt.plot(x,y)

# 设置x轴刻度
_xtick_labels = [i/2 for i in range(4,49)]
plt.xticks(_xtick_labels[::4]) # 当刻度太密时，使用列表取步长
plt.yticks(range(min(y),max(y)+1)[::2])

# 绘制之后保存图片,保存.png或者.svg图片格式，svg是矢量图格式，放大不会有锯齿
plt.savefig("./t1.svg")

# show命令展示图
plt.show()
