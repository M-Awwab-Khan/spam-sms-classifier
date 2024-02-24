import pickle
from preprocess import preprocess_text
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

def classify_msg(msg):
    processed_msg = preprocess_text(msg)
    transformed_msg= tfidf.transform([processed_msg])
    prediction = model.predict(transformed_msg)[0]
    return 'Spam' if prediction else 'Not Spam'