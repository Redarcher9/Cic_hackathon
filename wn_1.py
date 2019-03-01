import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
import json

def convert_tag(tag):
    tag_dict = {'N': 'n', 'J': 'a', 'R': 'r', 'V': 'v'}
    try:
        return tag_dict[tag[0]]
    except KeyError:
        return None

def preprocess(token):
    articles = set(stopwords.words('english'))
    articles.remove("not")
    filtered_tokens = []
    for w in token:
        if w not in articles:
            filtered_tokens.append(w)
    return filtered_tokens

def doc_to_synsets(doc):
    tag = nltk.pos_tag(doc)
    nltk2wordnet = [(i[0], convert_tag(i[1])) for i in tag]
    output = [wn.synsets(i, z)[0] for i, z in nltk2wordnet if len(wn.synsets(i, z))>0]
    return output


def similarity_score(s1, s2):
    list1 = []
    for a in s1:
        list1.append(max([i.path_similarity(a) for i in s2 if i.path_similarity(a) is not None]))

    output = sum(list1)/len(list1)
    return output

def document_path_similarity(doc1, doc2):
    return (similarity_score(doc1, doc2) + similarity_score(doc2, doc1)) / 2


text = { 'Rawtext1': "Marijuana is legal in some countries. It is illegal in others. For example, it is illegal in south east Asian countries.However, Thailand changes this.It becomes the first south east Asian country to make marijuana legal.People can sell it and buy it.They can use it as medicine.The Thai government controls, who sells marijuana. You can use it. However, you must have a certificate.", 'Rawtext2' :"Marijuana is gaining popularity around the world, and Thailand became the first south east Asian country to legalise it.Beginning with the new year, people will be able to use it as a medicine or study it. However, licenses to produce and sell marijuana products will be strictly controlled. People will be able to carry certain amounts of the drugs if they have a prescription or certificate. The new law also allows kratom, which is a plant native to the region. People use it to treat pain, anxiety and other problems." };
json_str = json.dumps(text)
resp = json.loads(json_str)

a= str(resp['Rawtext1'])
b= str(resp['Rawtext2'])

tokens1 = nltk.word_tokenize(a)
tokens2 = nltk.word_tokenize(b)

processed_tokens1 = preprocess(tokens1)
processed_tokens2 = preprocess(tokens2)

print(processed_tokens1)
print(processed_tokens2)

synsets1 = doc_to_synsets(processed_tokens1)
synsets2 = doc_to_synsets(processed_tokens2)

print(synsets1)
print(synsets2)

print("Similarity Score {:.2f}".format(round(document_path_similarity(synsets1,synsets2), 2)))
