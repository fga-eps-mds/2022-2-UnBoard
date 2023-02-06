import sys

from selenium.webdriver.common.virtual_authenticator import required_virtual_authenticator 
sys.path.append('..')

from utils.search_bar import SearchCourses
from flask import Flask, jsonify, request

import json
import typing
from pathlib import Path

json_data = Path('../Dashboard/data.json')

app = Flask(__name__)


@app.route('/dashboard/', methods = ['GET'])
def get_lista_cursos():
    cursos = SearchCourses()
    result = cursos.lista_cursos()
    return jsonify(result)

@app.route('/post', methods = ['POST'])
def set_curso():

    ano = request
    content = request.get_json()
    curso = content['curso']
    ano = content['ano']
    data = {'ano': ano, 'curso' : curso}
    with open(json_data, 'w', encoding='utf-8') as f:
        json.dump(data, f,ensure_ascii=False, indent=4)
    
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
