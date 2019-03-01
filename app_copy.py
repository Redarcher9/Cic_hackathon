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
file_modelmul1 = api.model('filemodel', {'base64_1' : fields.String('base64'),
'extension_1': fields.String('extension'),'base64_2' : fields.String('base64'),
'extension_2': fields.String('extension'),
'extension_3': fields.String('extension'),'base64_3' : fields.String('base64'),
'extension_4': fields.String('extension'),'base64_4' : fields.String('base64'),
'extension_5': fields.String('extension'),'base64_5' : fields.String('base64')
})
file_modelmul = api.model('Rawtext', {'Input1' : fields.String('Your Input.'),
'Input2': fields.String('Your Input.'),
'Input3': fields.String('Your Input.'),
'Input4': fields.String('Your Input.'),
'Input5': fields.String('Your Input.')})


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
        print(input_text1.text_extractor().lower(),file=sys.stderr)
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
    @api.expect(file_modelmul)
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
        input_text3 = miner(resp['base64_3'],resp['extension_3'])
        input_text4 = miner(resp['base64_4'],resp['extension_4'])
        input_text5 = miner(resp['base64_5'],resp['extension_5'])


        doc1=wordnet(input_text1.text_extractor().lower(),input_text2.text_extractor().lower())
        doc2=wordnet(input_text1.text_extractor().lower(),input_text3.text_extractor().lower())
        doc3=wordnet(input_text1.text_extractor().lower(),input_text4.text_extractor().lower())
        doc4=wordnet(input_text1.text_extractor().lower(),input_text5.text_extractor().lower())
        wordnet_results1=doc1.compute_wn_resullts()
        wordnet_results2=doc2.compute_wn_resullts()
        wordnet_results3=doc3.compute_wn_resullts()
        wordnet_results4=doc4.compute_wn_resullts()
        return {'similarity_score1' : wordnet_results1["similarity_score"],
                'similarity_score2' : wordnet_results2["similarity_score"],
                'similarity_score3' : wordnet_results3["similarity_score"],
                'similarity_score4' : wordnet_results4["similarity_score"],
                'tokens1' : wordnet_results["tokens1"],
                        'tokens2': wordnet_results["tokens2"],
                        'similarity_score' : wordnet_results["similarity_score"]}
@api.route('/Preprocessormul')
class Preprocessor(Resource):
    @api.expect(file_modelmul)
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
        doc31=Stopwords(resp['Input3'].lower())
        doc32=Tfcompute(doc31)
        doc41=Stopwords(resp['Input4'].lower())
        doc42=Tfcompute(doc41)
        doc51=Stopwords(resp['Input5'].lower())
        doc52=Tfcompute(doc51)
        doc112=VectorCreation(resp['Input1'].lower(),resp['Input2'].lower())
        doc113=VectorCreation(resp['Input1'].lower(),resp['Input3'].lower())
        doc114=VectorCreation(resp['Input1'].lower(),resp['Input4'].lower())
        doc115=VectorCreation(resp['Input1'].lower(),resp['Input5'].lower())
        tokenised_text_doc1=doc11.nontrivial_words()
        wordfreqdict_doc1=doc12.wordListToFreqDict()
        tokenised_text_doc2=doc21.nontrivial_words()
        wordfreqdict_doc2=doc22.wordListToFreqDict()
        cow_boy_output1=doc112.vectorizer()
        cow_boy_output2=doc113.vectorizer()
        cow_boy_output3=doc114.vectorizer()
        cow_boy_output4=doc115.vectorizer()
        return {
              'cosine_value1': cow_boy_output1['cosine_similarity'],
              'cosine_value2': cow_boy_output2['cosine_similarity'],
              'cosine_value3': cow_boy_output3['cosine_similarity'],
              'cosine_value4': cow_boy_output4['cosine_similarity']}




if __name__ == "__main__":
    app.run(port=4555,debug=True)
