from flask import Flask, flash, request, redirect, url_for,send_from_directory,render_template
from flask_restplus import fields, Api, Resource
from nltk_stopwords import Stopwords,Tfcompute
from cos_bow import VectorCreation
import json
from flask_restplus import reqparse
from werkzeug.datastructures import FileStorage
from wn_1 import wordnet
import sys
from extract import miner
app = Flask(__name__)
api = Api(app)
raw_text = api.model('Rawtext', {'Input1' : fields.String('Your Input.'),
'Input2': fields.String('Your Input.') })
file_model = api.model('filemodel', {'base64_1' : fields.String('base64'),
'extension_1': fields.String('extension'),'base64_2' : fields.String('base64'),
'extension_2': fields.String('extension')})

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
                'synsets1': wordnet_results["synsets1"],
                'synsets2': wordnet_results["synsets2"],
                'similarity_score' : wordnet_results["similarity_score"]}

@api.route('/FileUpload')
class FileUpload(Resource):
    @api.expect(file_model)
    def post(self):
        input_text = api.payload
        #dumps the json object into an element
        json_str = json.dumps(input_text)
        #load the json to a string
        resp = json.loads(json_str)
        #Stopwords elimination begins here
        input_text1 = miner(resp['base64_1'],resp['extension_1'])
        input_text2 = miner(resp['base64_2'],resp['extension_2'])
        doc11=Stopwords(input_text1.text_extractor().lower())
        doc12=Tfcompute(doc11)
        doc21=Stopwords(input_text2.text_extractor().lower())
        doc22=Tfcompute(doc21)
        doc13=VectorCreation(input_text1.text_extractor().lower(),input_text2.text_extractor().lower())
        tokenised_text_doc1=doc11.nontrivial_words()
        wordfreqdict_doc1=doc12.wordListToFreqDict()
        tokenised_text_doc2=doc21.nontrivial_words()
        wordfreqdict_doc2=doc22.wordListToFreqDict()
        cow_boy_output=doc13.vectorizer()
        return {'tokens_doc1' : tokenised_text_doc1,'term_frequencies_doc1': wordfreqdict_doc1,
                'token_doc2': tokenised_text_doc2,'term_frequencies_doc2': wordfreqdict_doc2,
                'vector_doc1': cow_boy_output['vectors'][0],'vector_doc2':cow_boy_output['vectors'][1],
                'cosine_value': cow_boy_output['cosine_similarity']}

@api.route('/FileUploadWordnet')
class Wordnet(Resource):
    @api.expect(file_model)
    def post(self):
        input_text = api.payload
        json_str = json.dumps(input_text)
        resp = json.loads(json_str)
        input_text = api.payload
        #dumps the json object into an element
        json_str = json.dumps(input_text)
        #load the json to a string
        resp = json.loads(json_str)
        #Stopwords elimination begins here
        input_text1 = miner(resp['base64_1'],resp['extension_1'])
        input_text2 = miner(resp['base64_2'],resp['extension_2'])
        doc1=wordnet(input_text1.text_extractor().lower(),input_text2.text_extractor().lower())
        wordnet_results=doc1.compute_wn_resullts()
        return {'tokens1' : wordnet_results["tokens1"],
                'tokens2': wordnet_results["tokens2"],
                'similarity_score' : wordnet_results["similarity_score"]}



if __name__ == "__main__":
    app.run(port=4555,debug=True)
