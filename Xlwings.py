# =============================================================================
# 14.4.1 Python创建Excel基础
# =============================================================================
import xlwings as xw
import matplotlib.pyplot as plt
import pandas as pd


def def6(sht_name, a1_value, file_name, file_path):
    # 新建一个Excel文件，并设置为不可见
    app = xw.App(visible=False)
    wb = app.books.add()

    # 创建新工作表
    sht = wb.sheets.add(sht_name)
    # 将A1单元格改为华小智
    sht.range('A1').value = a1_value

    # 导入表格
    df = pd.DataFrame([[1, 2], [3, 4]], columns=['a', 'b'])
    sht.range('A2').value = df

    # 生成图片
    fig = plt.figure()
    x = [1, 2, 3]
    y = [2, 4, 6]
    plt.plot(x, y)
    # 将产生的图片导入到Excel当中
    sht.pictures.add(fig, name='图片1', update=True, left=500)
    save_success = False
    try:
        # 保存生成的Excel文件
        wb.save(str(file_path + "/" + file_name))
        save_success = True
    except:
        save_success = False

    finally:
        wb.close()  # 退出工作簿
        app.quit()  # 退出程序
        return save_success
