from openpyxl import load_workbook

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    excel = load_workbook('goods.xlsx')
    page = excel['Лист1']
    goods_list = [
        page['A1'].value, page['A2'].value, page['A3'].value, 
        page['A4'].value, page['A5'].value, page['A6'].value
    ]
    return render_template('index.html', goods=goods_list)

if __name__ == '__main__':
    app.run(debug=True) 