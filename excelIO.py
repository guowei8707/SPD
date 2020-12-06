#导入xlwings模块
import xlwings as xw

'''
app->book->sheet->range

#必须先安装excel，office 2013即可
'''


def writeExcel(data, axis):
    print("at _writeExcel() head")
    # 打开Excel程序；设置：程序不可见，只打开不新建工作薄，屏幕更新关闭
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    # 设置文件位置：filepath
    filepath = r"./StdList.xlsx"
    # workbook 打开工作簿
    wb = app.books.open(filepath)
    # 实例化工作表对象
    sht = wb.sheets["sheet1"]
    # 返回工作表绝对路径
    sht.range(str(axis)).value = data
    # 保存工作簿，关闭工作簿，关闭应用接口
    wb.save()
    wb.close()
    app.quit()
    print("at _writeExcel() end")
    return


