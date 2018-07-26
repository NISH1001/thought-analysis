#!/usr/bin/env python3


import nltk
import re

def reduce_whitespaces(text):
    return re.sub(r"[\s\n]+", " ", text)

def remove_punctuations(text):
    text = re.sub(r"[()-_:.;!,*]+", " ", text)
    return re.sub(u'[—]+', ' ', text)

def remove_illegal_chars(text):
    return re.sub(r'[*]+', ' ', text)

def lemmatize(tokens):
    lemmatizer = nltk.stem.WordNetLemmatizer()
    lemma_list = []
    for token in tokens:
        lemma = lemmatizer.lemmatize(token, 'v')
        if lemma == token:
            lemma = lemmatizer.lemmatize(token)
        lemma_list.append(lemma)
    # return [ lemmatizer.lemmatize(token, 'v') for token in tokens ]
    return lemma_list

def process_text(text):
    text = text.encode('ascii', errors='ignore').decode()
    text = text.lower()
    text = re.sub(r'http\S+', ' <url> ', text)
    text = re.sub(r'#+', ' <hashtag> ', text )
    text = re.sub(r'@[A-Za-z0-9]+', ' <user> ', text)
    text = re.sub(r"([A-Za-z]+)'s", r"\1 is", text)

    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"don't", "do not ", text)
    text = re.sub(r"did't", "did not ", text)
    text = re.sub(r"shouldn't", "should not ", text)
    text = re.sub(r"wouldn't", "would not ", text)
    text = re.sub(r"hadn't", "had not ", text)
    text = re.sub(r"can't", "can not", text)
    text = re.sub(r"won't", "will not ", text)
    text = re.sub(r"isn't", "is not ", text)
    text = re.sub(r"can't", "can not ", text)
    text = re.sub(r"n't", " not ", text)

    text = re.sub(r"dont", " do not", text)
    text = re.sub(r"didnt", " did not", text)
    text = re.sub(r"wont", " will not", text)
    text = re.sub(r"cant", " can not", text)

    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\d+', ' <number> ', text)
    text = re.sub('\s+url\s+', ' <url> ', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text


def process_documents(documents):
    return list(map(process_text, documents))

def remove_stopwords(tokens, stopwords):
    res = []
    for token in tokens:
        if not token in stopwords:
            res.append(token)
    return res


def main():
    documents = ["hello! world. how are you?", "i am nishan", "http://nishanpantha.com.np hello 123 abc"]
    print(process_documents(documents))

if __name__ == "__main__":
    main()

