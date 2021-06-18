# =============================================================================
# 14.4.2 Python创建Excel实战
# =============================================================================

import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
import xlwings as xw


'''1.获取数据'''
# stock_code = '000002'
# stock_name = '万科A'
# start_date = '2019-02-01'
# end_date = '2019-04-01'


def def7(stock_code, stock_name, start_date, end_date):
    # 股票时间区间内的K线图，用于提取开盘价等有用信息
    stock_k = ts.get_hist_data(stock_code, start=start_date, end=end_date)

    # 建立一个新的DataFrame，用于存储当前股票的信息
    stock_table = pd.DataFrame()

    # 遍历日期索引，提取所需要的数据
    for current_date in stock_k.index:
        # 通过loc选中K线图中对应current_date这天的数据
        current_k_line = stock_k.loc[current_date]

        # 提取这一天前10分钟股票信息
        df = ts.get_tick_data(stock_code, date=current_date, src='tt')
        df['time'] = pd.to_datetime(current_date + ' ' + df['time'])
        t = pd.to_datetime(current_date).replace(hour=9, minute=40)
        df_10 = df[df.time <= t]
        vol = df_10.volume.sum()  # 通过sum()函数求和

        # 将数据信息放入字典中
        current_stock_info = {
            '名称': stock_name,
            '日期': pd.to_datetime(current_date),
            '开盘价': current_k_line.open,
            '收盘价': current_k_line.close,
            '股价涨跌幅(%)': current_k_line.p_change,
            '10分钟成交量': vol
        }
        # 通过append的方式增加新的一行，忽略索引
        stock_table = stock_table.append(current_stock_info, ignore_index=True)

    # 通过set_index()函数将日期那一列设置为索引
    # stock_table = stock_table.set_index('日期')

    # 设置列的顺序
    order = ['日期', '名称', '开盘价', '收盘价', '股价涨跌幅(%)', '10分钟成交量']
    stock_table = stock_table[order]

    # 获得衍生变量：10分钟成交量涨跌幅(%)
    stock_table['10分钟成交量10日均值'] = stock_table['10分钟成交量'].sort_index().rolling(
        10, min_periods=1).mean()
    stock_table['10分钟成交量涨跌幅(%)'] = (
        stock_table['10分钟成交量'] - stock_table['10分钟成交量10日均值'])/stock_table['10分钟成交量10日均值']*100

    # 选取所需要的列
    target_columns = ['日期', '名称', '开盘价', '收盘价',
                      '股价涨跌幅(%)', '10分钟成交量', '10分钟成交量涨跌幅(%)']
    final_table = stock_table[target_columns]

    return final_table


def drawPicAndSaveFIle(stock_name, final_table):
    '''2.将数据导入到Excel中并可视化呈现'''
    # 创建一个Excel文件，并设置为不可见
    app = xw.App(visible=False)
    wb = app.books.add()

    # 新建一张Excel表，命名为stock_name，也即最开始定义的“万科A”
    sht = wb.sheets.add(stock_name)

    # 将之前生成的final_table表格导入到Excel中
    sht.range('A1').value = final_table

    # 数据可视化，并将图片导入到Excel当中
    fig = plt.figure()  # 设置一下要导入Excel中的图片
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 解决负号'-'显示为方块的问题

    # 绘制第一个折线图：股价涨跌幅(%)
    plt.plot(final_table.index, final_table['股价涨跌幅(%)'].apply(
        lambda x: abs(x)), label='股价涨跌幅(%)', color='red')
    plt.legend(loc='upper left')  # 设置图例位置

    # 绘制第二个折线图：10分钟成交量涨跌幅(%)
    plt.twinx()  # 生成双坐标轴
    plt.plot(final_table.index, final_table['10分钟成交量涨跌幅(%)'].apply(
        lambda x: abs(x)), label='10分钟成交量涨跌幅(%)', linestyle='--')
    plt.legend(loc='upper right')

    # 设置图片标题，自动调整x坐标轴刻度的角度并展示图片
    plt.title(stock_name)  # 设置标题
    plt.gcf().autofmt_xdate()  # 自动调整x坐标轴刻度的角度

    # 把图片放到excel中
    sht.pictures.add(fig, name='图1', update=True, left=500)

    save_success = False
    try:
        # 保存生成的Excel文件
        wb.save(r"D:/股票分析.xlsx")
        save_success = True
    except:
        save_success = False

    finally:
        wb.close()  # 退出工作簿
        app.quit()  # 退出程序
        return save_success
