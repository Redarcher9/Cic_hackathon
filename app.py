from flask import Flask, flash, request, redirect, url_for,send_from_directory,render_template
from flask_restplus import fields, Api, Resource
from nltk_stopwords import Stopwords,Tfcompute
from cos_bow import VectorCreation
import json
from flask_restplus import reqparse
from werkzeug.datastructures import FileStorage
from wn_1 import wordnet
import sys
app = Flask(__name__)
api = Api(app)
raw_text = api.model('Rawtext', {'Input1' : fields.String('Your Input.'),
'Input2': fields.String('Your Input.') })
file_model = api.model('filemodel', {'base64' : fields.String('base64'),
'extension': fields.String('extension')})

@api.route('/Preprocessor')
class Preprocessor(Resource):
    @api.expect(raw_text)
    def post(self):
        #data received from post request
        input_text = api.payload
        #dumps the json object into an element
        json_str = json.dumps(input_text)
        #load the json to a string
        resp = json.loads(json_str)
        #Stopwords elimination begins here
        doc11=Stopwords(resp['Input1'].lower())
        doc12=Tfcompute(doc11)
        doc21=Stopwords(resp['Input2'].lower())
        doc22=Tfcompute(doc21)
        doc13=VectorCreation(resp['Input1'].lower(),resp['Input2'].lower())
        tokenised_text_doc1=doc11.nontrivial_words()
        wordfreqdict_doc1=doc12.wordListToFreqDict()
        tokenised_text_doc2=doc21.nontrivial_words()
        wordfreqdict_doc2=doc22.wordListToFreqDict()
        cow_boy_output=doc13.vectorizer()
        return {'tokens_doc1' : tokenised_text_doc1,'term_frequencies_doc1': wordfreqdict_doc1,
                'token_doc2': tokenised_text_doc2,'term_frequencies_doc2': wordfreqdict_doc2,
                'vector_doc1': cow_boy_output['vectors'][0],'vector_doc2':cow_boy_output['vectors'][1],
                'cosine_value': cow_boy_output['cosine_similarity']}


@api.route('/Wordnet')
class Wordnet(Resource):
    @api.expect(raw_text)
    def post(self):
        input_text = api.payload
        json_str = json.dumps(input_text)
        resp = json.loads(json_str)
        doc1=wordnet(resp['Input1'].lower(),resp['Input2'].lower())
        wordnet_results=doc1.compute_wn_resullts()
        print(wordnet_results,file=sys.stderr)
        return {'tokens1' : wordnet_results["tokens1"],
                'tokens2': wordnet_results["tokens2"],
                'similarity_score' : wordnet_results["similarity_score"]}

"""@api_route('/FileUpload')
class FileUpload(Resource):
    @api.expect(file_model)
    def post(self):
        input_text = api.payload
        #dumps the json object into an element
        json_str = json.dumps(input_text)
        #load the json to a string
        resp = json.loads(json_str)
        #Stopwords elimination begins here
"""

if __name__ == "__main__":
    app.run(port=4555,debug=True)
