from flask import Flask, jsonify, request
import spacy
from sentence_transformers import SentenceTransformer, util
from flask_cors import CORS

# Crea una instancia de la aplicación Flask
app = Flask(__name__)
CORS(app)


# Carga los modelos de procesamiento de lenguaje antes de la primera solicitud
@app.before_first_request
def load_models():
    # Carga el modelo de procesamiento de lenguaje de spaCy
    global st_model_embedder, file_load_text, section_file_load
    global similarity_list 
    # Load el modelo de procesamiento de lenguaje de spaCy
    # nlp_model = spacy.load('es_core_news_lg')

    # Este es el modelo de procesamiento de lenguaje de SentenceTransformer
    # Load el modelo de procesamiento de lenguaje de SentenceTransformer
    st_model_embedder = SentenceTransformer(
        'paraphrase-MiniLM-L6-v2')  # Carga un modelo de embeddings
    # st_model_embedder = SentenceTransformer(
    # 'multi-qa-MiniLM-L6-cos-v1')  # Carga un modelo de embeddings

    # Carga el texto desde el archivo con manejo de errores
    try:
        file_load_text = load_text_from_file("data/text.txt")
        section_file_load = process_sections_text(file_load_text)
    except Exception as e:
        print("Error:", e)
        exit(1)

    query_embedding = embedding_query()

    # Dividir en oraciones utilizando SpaCy
    # sentences = nlp_model(file_load_text).sents
    sentence_embeddings = []
    for name, sentence in section_file_load.items():
        sentence_embedding = st_model_embedder.encode(
            sentence, convert_to_tensor=True)
        sentence_embeddings.append((name, sentence, sentence_embedding))

def query(self, query):
    query_embedding = embedding_query(query=query)
    similarity_list1 = []
    for seccion_name, sentence_text, sentence_embedding in self.sentence_embeddings:
        similarity = util.pytorch_cos_sim(
            query_embedding, sentence_embedding)[0][0].item()
        similarity_list1.append((seccion_name, sentence_text, similarity))

    # Ordenar la lista por similitud en orden descendente
    similarity_list1.sort(key=lambda x: x[2], reverse=True)

    return similarity_list1

def embedding_query(query="¿Cómo actualizo el stock?"):
    query_embedding = st_model_embedder.encode(query, convert_to_tensor=True)
    return query_embedding


# Función para cargar el texto desde un archivo con manejo de errores
def load_text_from_file(filename, encodings=None):
    if encodings is None:
        # Lista de codificaciones a probar
        encodings = ['utf-8', 'latin-1', 'latin1', 'ISO-8859-1']
    for encoding in encodings:
        try:
            with open(filename, 'r', encoding=encoding) as file:
                return file.read()
        except UnicodeDecodeError:
            pass
    raise Exception(
        "No se pudo decodificar el archivo con ninguna codificación.")

# Procesar las secciones


def process_sections_text(sections_text):
    sections = {}
    sections_text1 = sections_text.split("\n\n")
    for section_text in sections_text1:
        lines = section_text.split('\n')
        section_name = lines[0]
        section_text = '\n'.join(lines[1:])
        sections[section_name] = section_text
    return sections

# Tokenizar las secciones


def tokenize_sections(sections, nlp_model):
    section_tokenizer = {}
    for section_name, section_content in sections.items():
        section_doc = nlp_model(section_content)
        # section_tokens = [token for token in section_doc]
        section_tokenizer[section_name] = section_doc
    return section_tokenizer


@app.route('/',methods=['POST'])
def hello():
    # Verifica que se haya enviado una solicitud POST con datos JSON
    if request.method == 'POST' and request.is_json:
        # Procesa los datos de la solicitud
        data = request.json
        print(data['query'])
        similarity_list = query(data['query'])
        returnList = []
        # for seccion_name, sentence_text, similarity in self.similarity_list[:5]:
        #     returnList.append({
        #     "section_name": seccion_name,
        #     "sentence_text": sentence_text,
        #     "similarity": similarity
        #                     })
        return jsonify(returnList)
    return jsonify({"error": "No se ha podido procesar la solicitud."}), 400


@app.route('/')
def GetHome():
    print('Cargando')
    returnList = []
    for seccion_name, sentence_text, similarity in similarity_list[:5]:
            returnList.append({
            "section_name": seccion_name,
            "sentence_text": sentence_text,
            "similarity": similarity
                            })
    return jsonify(returnList)

# Ejecuta la aplicación Flask
if __name__ == '__main__':
    app.run()
