#! /home/blank/Documents/PythonFlask/Product_list/venv/bin/python3

from CustomApi import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='localhost', debug=True)