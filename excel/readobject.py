import xlrd

path = r"C:\Users\Yashaswini\Desktop\locator_py.xlsx"

def Excel():
    wb = xlrd.open_workbook(path)
    sn = wb.sheet_by_name("login_page")
    rows = sn.get_rows()
    # print(rows)

    # traversing
    # to read the data only.headings will be available
    # for row in rows:
    #     print(row[0].value,row[1].value,row[2].value, sep="::")

    headers = next(rows)       #it will read one line from the rows i.e it will skip the header
    return {row[0].value: (row[1].value, row[2].value) for row in rows}

# Excel(





























