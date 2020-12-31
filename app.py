#! /home/blank/Documents/PythonFlask/Product_list/venv/bin/python3

from CustomApi import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)