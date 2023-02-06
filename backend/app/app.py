import sys 
sys.path.append('..')

from utils.search_bar import SearchCourses

from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route('/dashboard/', methods = ['GET'])
def get_list_courses():
    cursos = SearchCourses()
    result = cursos.lista_cursos()
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
