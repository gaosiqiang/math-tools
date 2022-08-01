from django.http import HttpResponse
from mpl_toolkits.axisartist.axislines import SubplotZero
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg

import math
import numpy as np  # 导入数值计算模块
import matplotlib.pyplot as plt  # 导入绘图模块
import mpl_toolkits.axisartist as axisartist  # 导入坐标轴加工模块


def index(request):
    return HttpResponse('Hello word')

# 一次函数
def math_linear_function(request, k, b):

    fig = plt.figure(figsize=(10, 10))  # 新建画布
    ax = axisartist.Subplot(fig, 111)  # 使用axisartist.Subplot方法创建一个绘图区对象ax
    fig.add_axes(ax)  # 将绘图区对象添加到画布中

    ax.axis[:].set_visible(False)  # 隐藏原来的实线矩形

    ax.axis["x"] = ax.new_floating_axis(0, 0, axis_direction="bottom")  # 添加x轴
    ax.axis["y"] = ax.new_floating_axis(1, 0, axis_direction="bottom")  # 添加y轴

    ax.axis["x"].set_axisline_style("->", size=1.0)  # 给x坐标轴加箭头
    ax.axis["y"].set_axisline_style("->", size=1.0)  # 给y坐标轴加箭头
    # ax.annotate(s='x' ,xy=(2*math.pi,0) ,xytext=(2*math.pi,0.1)) #标注x轴
    # ax.annotate(s='y' ,xy=(0,1.0) ,xytext=(-0.5,1.0)) #标注y轴
    ax.annotate('x', xy=(2 * math.pi, 0), xytext=(10, 0.5))  # 标注x轴
    ax.annotate('y', xy=(0, 1.0), xytext=(-0.5, 10.0))  # 标注y轴

    # plt.rcParams['font.sans-serif']=['Adobe Fangsong Std']
    # plt.rcParams['font.family'] = ['sans-serif']
    # plt.rcParams['font.sans-serif'] = ['MingLiU']
    plt.rcParams['font.family'] = 'DejaVu Sans'
    plt.rcParams['axes.unicode_minus'] = False  # 步骤二（解决坐标轴负数的负号显示问题）
    ax.annotate('1-quadrant', xy=(2, 2), xytext=(5, 5))  # 标注第一象限
    ax.annotate('2-quadrant', xy=(2, 2), xytext=(-5, 5))  # 标注第二象限
    ax.annotate('3-quadrant', xy=(2, 2), xytext=(-5, -5))  # 标注第三象限
    ax.annotate('4-quadrant', xy=(2, 2), xytext=(5, -5))  # 标注第四象限

    plt.xlim(-10, 10)  # 设置横坐标范围
    plt.ylim(-10, 10)  # 设置纵坐标范围
    # ax.set_xticks([-2*math.pi,-math.pi,0,math.pi,2*math.pi]) #设置x轴刻度
    ax.set_xticks([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # 设置x轴刻度
    ax.set_yticks([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # 设置y轴刻度

    ax.annotate('o', xy=(2, 2), xytext=(0.5, 0.5))  # 标注坐标系原点o

    # y=[] #用来存放函数值
    # x=np.linspace(-2*math.pi,2*math.pi,100) #构造横坐标数据
    # for xi in x: #生成函数值
    #     y.append(math.sin(xi))#追加

    # my code
    y = []
    x = []

    # 生成一次函数数据
    # a = 10  # 系数
    # k = 5  # 常数
    n = 10
    counter = -11

    while counter < n:
        counter += 0.01  # 数据的颗粒度
        x.append(counter)
    # print(counter)

    # 参数处理
    b_notation = b[0:1]
    b = int(b[1:], 10)
    k_notation = k[0:1]
    k = int(k[1:], 10)
    if k_notation == 'm':
        k = k * -1

    if b_notation == 'm':
        b = b * -1

    for item in x:
        y.append(k * item + b)

    plt.plot(x, y, color="blue")  # 描点连线

    # plt.title('asd')

    plt.show()  # 出图
    ##########
    canvas = FigureCanvasAgg(fig)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response
    # return HttpResponse("Hello, world.")

def inverse_proportion_function(request, k):
    fig = plt.figure(figsize=(10, 10))  # 新建画布
    ax = axisartist.Subplot(fig, 111)  # 使用axisartist.Subplot方法创建一个绘图区对象ax
    fig.add_axes(ax)  # 将绘图区对象添加到画布中

    ax.axis[:].set_visible(False)  # 隐藏原来的实线矩形

    ax.axis["x"] = ax.new_floating_axis(0, 0, axis_direction="bottom")  # 添加x轴
    ax.axis["y"] = ax.new_floating_axis(1, 0, axis_direction="bottom")  # 添加y轴

    ax.axis["x"].set_axisline_style("->", size=1.0)  # 给x坐标轴加箭头
    ax.axis["y"].set_axisline_style("->", size=1.0)  # 给y坐标轴加箭头
    # ax.annotate(s='x' ,xy=(2*math.pi,0) ,xytext=(2*math.pi,0.1)) #标注x轴
    # ax.annotate(s='y' ,xy=(0,1.0) ,xytext=(-0.5,1.0)) #标注y轴
    ax.annotate('x', xy=(2 * math.pi, 0), xytext=(10, 0.5))  # 标注x轴
    ax.annotate('y', xy=(0, 1.0), xytext=(-0.5, 10.0))  # 标注y轴

    # plt.rcParams['font.sans-serif']=['Adobe Fangsong Std']
    # plt.rcParams['font.family'] = ['sans-serif']
    # plt.rcParams['font.sans-serif'] = ['MingLiU']
    plt.rcParams['font.family'] = 'DejaVu Sans'
    plt.rcParams['axes.unicode_minus'] = False  # 步骤二（解决坐标轴负数的负号显示问题）
    ax.annotate('1', xy=(2, 2), xytext=(5, 5))  # 标注第一象限
    ax.annotate('2', xy=(2, 2), xytext=(-5, 5))  # 标注第二象限
    ax.annotate('3', xy=(2, 2), xytext=(-5, -5))  # 标注第三象限
    ax.annotate('4', xy=(2, 2), xytext=(5, -5))  # 标注第四象限

    plt.xlim(-10, 10)  # 设置横坐标范围
    plt.ylim(-10, 10)  # 设置纵坐标范围
    # ax.set_xticks([-2*math.pi,-math.pi,0,math.pi,2*math.pi]) #设置x轴刻度
    ax.set_xticks([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # 设置x轴刻度
    ax.set_yticks([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # 设置y轴刻度

    ax.annotate('o', xy=(2, 2), xytext=(0.5, 0.5))  # 标注坐标系原点o

    # y=[] #用来存放函数值
    # x=np.linspace(-2*math.pi,2*math.pi,100) #构造横坐标数据
    # for xi in x: #生成函数值
    #     y.append(math.sin(xi))#追加

    # my code
    y = []
    x = []

    # 生成反比例函数数据
    n = 10
    counter = -11

    k_notation = k[0:1]
    k = int(k[1:], 10)
    if k_notation == 'm':
        k = k * -1

    while counter < n:
        counter += 0.01  # 数据的颗粒度
        x.append(counter)
    # print(counter)



    for item in x:
        y.append(k / item)

    plt.plot(x, y, color="blue")  # 描点连线

    # plt.title('asd')

    plt.show()  # 出图
    ##########
    canvas = FigureCanvasAgg(fig)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response
    # return HttpResponse("Hello, world.")


def quadratic_function(request, a, b, c):
    fig = plt.figure(figsize=(10, 10))  # 新建画布
    ax = axisartist.Subplot(fig, 111)  # 使用axisartist.Subplot方法创建一个绘图区对象ax
    fig.add_axes(ax)  # 将绘图区对象添加到画布中

    ax.axis[:].set_visible(False)  # 隐藏原来的实线矩形

    ax.axis["x"] = ax.new_floating_axis(0, 0, axis_direction="bottom")  # 添加x轴
    ax.axis["y"] = ax.new_floating_axis(1, 0, axis_direction="bottom")  # 添加y轴

    ax.axis["x"].set_axisline_style("->", size=1.0)  # 给x坐标轴加箭头
    ax.axis["y"].set_axisline_style("->", size=1.0)  # 给y坐标轴加箭头
    # ax.annotate(s='x' ,xy=(2*math.pi,0) ,xytext=(2*math.pi,0.1)) #标注x轴
    # ax.annotate(s='y' ,xy=(0,1.0) ,xytext=(-0.5,1.0)) #标注y轴
    ax.annotate('x', xy=(2 * math.pi, 0), xytext=(10, 0.5))  # 标注x轴
    ax.annotate('y', xy=(0, 1.0), xytext=(-0.5, 10.0))  # 标注y轴

    # plt.rcParams['font.sans-serif']=['Adobe Fangsong Std']
    # plt.rcParams['font.family'] = ['sans-serif']
    # plt.rcParams['font.sans-serif'] = ['MingLiU']
    plt.rcParams['font.family'] = 'DejaVu Sans'
    plt.rcParams['axes.unicode_minus'] = False  # 步骤二（解决坐标轴负数的负号显示问题）
    ax.annotate('1', xy=(2, 2), xytext=(5, 5))  # 标注第一象限
    ax.annotate('2', xy=(2, 2), xytext=(-5, 5))  # 标注第二象限
    ax.annotate('3', xy=(2, 2), xytext=(-5, -5))  # 标注第三象限
    ax.annotate('4', xy=(2, 2), xytext=(5, -5))  # 标注第四象限

    plt.xlim(-10, 10)  # 设置横坐标范围
    plt.ylim(-10, 10)  # 设置纵坐标范围
    # ax.set_xticks([-2*math.pi,-math.pi,0,math.pi,2*math.pi]) #设置x轴刻度
    ax.set_xticks([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # 设置x轴刻度
    ax.set_yticks([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # 设置y轴刻度

    ax.annotate('o', xy=(2, 2), xytext=(0.5, 0.5))  # 标注坐标系原点o

    # y=[] #用来存放函数值
    # x=np.linspace(-2*math.pi,2*math.pi,100) #构造横坐标数据
    # for xi in x: #生成函数值
    #     y.append(math.sin(xi))#追加

    # my code
    y = []
    x = []

    # 生成二次函数数据
    n = 10

    counter = -11
    while counter < n:
        counter += 0.01  # 数据的颗粒度
        x.append(counter)

    # 处理参数
    # a = 5  # 二次项系数
    # b = 6  # 一次项系数数
    # c = 2  # 常数
    a_notation = a[0:1]
    a = int(a[1:], 10)
    b_notation = b[0:1]
    b = int(b[1:], 10)
    c_notation = c[0:1]
    c = int(c[1:], 10)

    if a_notation == 'm':
        a = a * -1

    if b_notation == 'm':
        b = b * -1

    if c_notation == 'm':
        c = c * -1

    for item in x:
        y.append(a * (item ** 2) + b * item + c)

    plt.plot(x, y, color="blue")  # 描点连线

    # plt.title('asd')

    plt.show()  # 出图
    ##########
    canvas = FigureCanvasAgg(fig)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response
    # return HttpResponse("Hello, world.")