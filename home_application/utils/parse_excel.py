# coding: utf-8
# @Time: 2019/10/16 10:01
# @Author: renpingsheng

import xlwt
import xlrd
import xlsxwriter


################# xlwt和xlrd 版本########################
# 写Excel
def write_excel(sheet_name, titles, col1, col2):
    f = xlwt.Workbook()
    # 添加一个Sheet，名字为 sheet_name 所传的参数
    sheet1 = f.add_sheet(sheet_name, cell_overwrite_ok=True)
    # 写文件头
    for i in range(0, len(titles)):
        # i 表示第一行的第 i 列
        sheet1.write(0, i, titles[i])

    # 从第二行开始写入数据
    for i in range(0, len(col1)):
        # 向每一行的第1列写入数据
        sheet1.write(i + 1, 0, col1[i])
        # 向每一行的第2列写入数据
        sheet1.write(i + 1, 1, col2[i])

    # 第一个参数表示行，从0开始计算
    # 第二个参数表示列，从0开始计算
    # 第二个参数表示写入的数据
    # sheet1.write(1, 3, '2006/12/12')

    # 第一个参数：合并开始的行
    # 第二个参数：合并结束的行(可以一次合并多行)
    # 第三个参数：合并开始的列
    # 第四个参数：合并结束的列(可以一次合并多行多列)
    # 第五个参数：写入的数据
    sheet1.write_merge(1, 3, 3, 3, u'打游戏')  # 合并列单元格
    sheet1.write_merge(4, 10, 3, 4, u'打篮球')
    f.save('%s.xls' % sheet_name)


# 读取Excel文件
def read_excel():
    # 路径前加 r，读取的文件路径
    file_path = r'网管IP地址.xlsx'

    # 文件路径的中文转码
    file_path = file_path.decode('utf-8')

    # 获取数据
    data = xlrd.open_workbook(file_path)

    # 获取sheet，通常为 Sheet1
    table = data.sheet_by_name(u'管理地址(Vlan999)')

    # 获取excel文件的总行数
    nrows = table.nrows
    # 从第二行开始读取数据
    for i in range(1, nrows):
        # 读取每一行第一列的数据
        manage_ip = table.cell(i, 0).value.strip()
        # 读取每一行第二列的数据
        dept = table.cell(i, 1).value.strip()


################# xlsxwriter版本########################

def write_excel1():
    # 新建文件，文件名为: hello.xlsx
    workbook = xlsxwriter.Workbook('hello.xlsx')
    # 建立sheet，可以传入参数来指定sheet名
    worksheet = workbook.add_worksheet(u"任平生")

    titles = [u"姓名", u"年龄", u"出生日期", u"爱好"]
    col1 = [u"张三", u"李四", u"恋习Python", u"小明", u"小红", u"无名"]
    col2 = [12, 13, 14, 15, 16, 17]

    # 写入文件头部
    for i in range(len(titles)):
        worksheet.write(0, i, titles[i])

    # 写入文件内容
    for j in range(len(col1)):
        # 从第二行开始向每行的第一列写入数据
        worksheet.write(j + 1, 0, col1[j])
        # 从第二行开始向每行的第二列写入数据
        worksheet.write(j + 1, 1, col2[j])

    workbook.close()

















