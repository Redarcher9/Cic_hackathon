import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
import json
class wordnet:
        def __init__(self,input_text1,input_text2):
            self.input_text1=input_text1
            self.input_text2=input_text2
        def convert_tag(self,tag):
            tag_dict = {'N': 'n', 'J': 'a', 'R': 'r', 'V': 'v'}
            try:
                return tag_dict[tag[0]]
            except KeyError:
                return None

        def preprocess(self,token):
            articles = set(stopwords.words('english'))
            articles.remove("not")
            filtered_tokens = []
            for w in token:
                if w not in articles:
                    filtered_tokens.append(w)
            return filtered_tokens

        def doc_to_synsets(self,doc):
            tag = nltk.pos_tag(doc)
            nltk2wordnet = [(i[0], self.convert_tag(i[1])) for i in tag]
            output = [wn.synsets(i, z)[0] for i, z in nltk2wordnet if len(wn.synsets(i, z))>0]
            return output


        def similarity_score(self,s1, s2):
            list1 = []
            for a in s1:
                list1.append(max([i.path_similarity(a) for i in s2 if i.path_similarity(a) is not None]))

            output = sum(list1)/len(list1)
            return output

        def document_path_similarity(self,doc1, doc2):
            return (self.similarity_score(doc1, doc2) + self.similarity_score(doc2, doc1)) / 2

        def compute_wn_resullts(self):
            a= self.input_text1
            b= self.input_text2
            tokens1 = nltk.word_tokenize(a)
            tokens2 = nltk.word_tokenize(b)
            processed_tokens1 = self.preprocess(tokens1)
            processed_tokens2 = self.preprocess(tokens2)
            synsets1 = self.doc_to_synsets(processed_tokens1)
            synsets2 = self.doc_to_synsets(processed_tokens2)
            word_net_similarity_score=round(self.document_path_similarity(synsets1,synsets2), 2)
            lis1 =[]
            for e in synsets1:
                lis1.append(str(e))
            final_synsets1=map(lambda each:each.strip("Sysnet()"),lis1)
            final_synsets1=list(map(lambda each:each.strip("')"),final_synsets1))
            lis2 =[]
            for e in synsets2:
                lis2.append(str(e))
            final_synsets2=map(lambda each:each.strip("Sysnet()"),lis2)
            final_synsets2=list(map(lambda each:each.strip("')"),final_synsets2))
            printer = {'tokens1':processed_tokens1,'synsets1':final_synsets1,
            'tokens2':processed_tokens2,'synsets2':final_synsets2,
            'similarity_score':word_net_similarity_score
            }
            return printer
