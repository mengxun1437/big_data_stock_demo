# =============================================================================
# 14.2.1 获得股票基本信息数据
# =============================================================================

# 2.获取多天的前10分钟成交信息及每日基本行情信息
import tushare as ts
import pandas as pd
# stock_code = '000002'
# stock_name = '万科A'
# start_date = '2021-04-12'  # 设置起始日期
# end_date = '2021-04-20'  # 设置终止日期


def def2(stock_code, stock_name, start_date, end_date):
    # 股票时间区间内的K线图，用于提取开盘价等有用信息
    stock_k = ts.get_hist_data(stock_code, start=start_date, end=end_date)

    '''下面开始批量获取多日的前10分钟交易数据及日线行情数据'''

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
        stock_table = stock_table.append(
            current_stock_info, ignore_index=True)
        # print(stock_table)

    # # 通过set_index()函数将日期那一列设置为索引
    # stock_table = stock_table.set_index('日期')

    # # 设置列的顺序
    order = ['日期', '名称', '开盘价', '收盘价', '股价涨跌幅(%)', '10分钟成交量']
    stock_table = stock_table[order]

    return stock_table
