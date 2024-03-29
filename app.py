from flask import Flask, jsonify, request
from flask_cors import CORS
from model.Query import Query


app = Flask(__name__)
CORS(app)
query_instance = Query()


# Carga los modelos de procesamiento de lenguaje antes de la primera solicitud
# @app.before_first_request

@app.route('/', methods=['POST'])
def hello():
    returnList = []
    data = request.json
    query = data['query']
    if query is None or query.strip() == "":
        returnList.append({
            "section_name": "Sin preguntas...",
            "sentence_text": "Debe escribir una pregunta o texto",
            "similarity": 0
        })
        return jsonify(returnList)
    print(query)
    similarity_list = query_instance.query(query)
    for seccion_name, sentence_text, similarity in similarity_list[:10]:
        returnList.append({
            "section_name": seccion_name,
            "sentence_text": sentence_text,
            "similarity": similarity
        })
    return jsonify(returnList)


@app.route('/')
def GetHome():
    print('Cargando')
    returnList = []
    similarity_list = query_instance.query("Datos del Artículo")
    for seccion_name, sentence_text, similarity in similarity_list[:10]:
        returnList.append({
            "section_name": seccion_name,
            "sentence_text": sentence_text,
            "similarity": similarity
        })
    return jsonify(returnList)


# Ejecuta la aplicación Flask
if __name__ == '__main__':
    app.run()
