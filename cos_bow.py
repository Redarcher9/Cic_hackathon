import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string
import numpy as np
import json

word_net_lemmatizer = WordNetLemmatizer()
class VectorCreation:
    def __init__(self,input_text1,input_text2):
        self.input_text1=input_text1
        self.input_text2=input_text2

    def text_preprocessing(self,text):
        final_list = []
        tokens = word_tokenize(text.lower())
        stopwords_and_punctuations_list = stopwords.words("english")+list(string.punctuation)
        for word in tokens:
            if word not in stopwords_and_punctuations_list:
                final_list.append(word_net_lemmatizer.lemmatize(word))
        return final_list

    def compute_cosine_similarity(self,vector_A,vector_B):
        return (np.dot(vector_A,vector_B) /( np.linalg.norm(vector_A) * np.linalg.norm(vector_B)))

    def vectorizer(self):
        text = { 'Rawtext1': "Marijuana is legal in some countries. It is illegal in others. For example, it is illegal in south east Asian countries.However, Thailand changes this.It becomes the first south east Asian country to make marijuana legal.People can sell it and buy it.They can use it as medicine.The Thai government controls, who sells marijuana. You can use it. However, you must have a certificate.",'Rawtext2' :" It is illegal in others. For example, it is illegal in south east Asian countries.However, Thailand changes this.It becomes the first south east Asian country to make marijuana legal.People can sell it and buy it.They can use it as medicine.The Thai government controls, who sells marijuana. You can use it. However, you must have a certificate.Marijuana is legal in some countries." };
        json_str1 = json.dumps(self.input_text1)
        json_str2 = json.dumps(self.input_text2)
        resp1 = json.loads(json_str1)
        resp2 = json.loads(json_str2)
        a= str(resp1)
        b= str(resp2)
        tokens = sorted(set(self.text_preprocessing(a)+self.text_preprocessing(b)))
        bag_of_words_a = []
        bag_of_words_b = []
        for word in tokens:
            bag_of_words_a.append(self.text_preprocessing(a).count(word))
        len1 = 100-len(bag_of_words_a)
        for i in range(0,len1):
            bag_of_words_a.append(0)
        for word in tokens:
            bag_of_words_b.append(self.text_preprocessing(b).count(word))
        len2 = 100-len(bag_of_words_b)
        for i in range(0,len2):
            bag_of_words_b.append(0)
        vectorz = []
        vectorz.append(bag_of_words_a)
        vectorz.append(bag_of_words_b)
        csvalue=round(self.compute_cosine_similarity(bag_of_words_a,bag_of_words_b), 2)
        return {'vectors': vectorz,'cosine_similarity': csvalue}
