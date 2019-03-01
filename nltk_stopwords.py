#stop words elimination
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')

class Stopwords:
    def __init__(self,input_text):
        self.input_text = input_text

    def eliminator(self):
        stop_words = set(stopwords.words('english')+stopwords.words('danish')+stopwords.words('german')+stopwords.words('russian')
        +stopwords.words('turkish')+stopwords.words('french'))
        tokenizer = RegexpTokenizer(r'\w+')
        word_tokens = tokenizer.tokenize(self.input_text)                           #removes punctuations
        filtered_sentence = [w for w in word_tokens if not w in stop_words]         #removes stop_words
        filtered_sentence = []
        for w in word_tokens:
            if w not in stop_words:
                filtered_sentence.append(w)
        return filtered_sentence                                                      #returns non-trivial words

    def nontrivial_words(self):
        mylist = self.eliminator()
        mylist = list( dict.fromkeys(mylist) )
        return mylist
class Tfcompute(Stopwords):
    def __init__(self,stopwords_instance):
        self.stopwords_instance=stopwords_instance
        self.filtered_sentence=self.stopwords_instance.eliminator()


    def wordListToFreqDict(self):
        wordfreq = [self.filtered_sentence.count(p) for p in self.filtered_sentence]
        return dict(zip(self.filtered_sentence,wordfreq))
