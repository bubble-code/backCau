from sentence_transformers import SentenceTransformer, util
import spacy
from data.DataClass import DataClass


class Query:
    def __init__(self):
        self.st_model_embedder = SentenceTransformer('paraphrase-MiniLM-L6-v2')
        self.dataclass = DataClass()
        try:
            # self.file_load_text = self.load_text_from_file("../data/text.txt")
            self.section_file_load = self.process_sections_text(self.dataclass.text)
            self.sentence_embeddings = self.encode_sentences()
        except Exception as e:
            print("Error:", e)
            exit(1)

    def load_text_from_file(self, filename, encodings=None):
        if encodings is None:
            encodings = ['utf-8', 'latin-1', 'latin1', 'ISO-8859-1']
        for encoding in encodings:
            try:
                with open(filename, 'r', encoding=encoding) as file:
                    return file.read()
            except UnicodeDecodeError:
                pass
        raise Exception("No se pudo decodificar el archivo con ninguna codificación.")

    def process_sections_text(self,sections_text):
        sections = {}
        sections_text1 = sections_text.split("\n\n")
        for section_text in sections_text1:
            lines = section_text.split('\n')
            section_name = lines[0]
            section_text = '\n'.join(lines[1:])
            sections[section_name] = section_text
        return sections

    def encode_sentences(self):
        sentence_embeddings = []
        for name, sentence in self.section_file_load.items():
            sentence_embedding = self.st_model_embedder.encode(
                sentence, convert_to_tensor=True)
            sentence_embeddings.append((name, sentence, sentence_embedding))
        return sentence_embeddings

    def query(self, query):
        query_embedding = self.embedding_query(query=query)
        similarity_list = []
        for section_name, sentence_text, sentence_embedding in self.sentence_embeddings:
            similarity = util.pytorch_cos_sim(
                query_embedding, sentence_embedding)[0][0].item()
            similarity_list.append((section_name, sentence_text, similarity))
        similarity_list.sort(key=lambda x: x[2], reverse=True)
        return similarity_list

    def embedding_query(self, query="¿Cómo actualizo el stock?"):
        query_embedding = self.st_model_embedder.encode(
            query, convert_to_tensor=True)
        return query_embedding

    @staticmethod
    def tokenize_sections(sections, nlp_model):
        section_tokenizer = {}
        for section_name, section_content in sections.items():
            section_doc = nlp_model(section_content)
            section_tokenizer[section_name] = section_doc
        return section_tokenizer
