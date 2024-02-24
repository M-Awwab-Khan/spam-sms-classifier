import nltk
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
nltk.download('stopwords')
nltk.download('punkt')
sw = stopwords.words('english')
p = string.punctuation

def preprocess_text(text):
    text = text.lower()
    text_tokenized = nltk.word_tokenize(text)
    text_processed = [ps.stem(word) for word in text_tokenized if word.isalnum() and word not in sw and word not in p]
    return " ".join(text_processed)