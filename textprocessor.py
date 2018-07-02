#!/usr/bin/env python3


import re

def reduce_whitespaces(text):
    return re.sub(r"[\s\n]+", " ", text)

def remove_punctuations(text):
    text = re.sub(r"[()-_:.;!,*]+", " ", text)
    return re.sub(u'[—]+', ' ', text)

def remove_illegal_chars(text):
    return re.sub(r'[*]+', ' ', text)

def process_text(text):
    text = text.encode('ascii', errors='ignore').decode()
    text = text.lower()
    text = re.sub(r"([A-Za-z]+)'s", r"\1 is", text)
    #text = re.sub(r"\'s", " ", text)
    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"can't", "can not ", text)
    text = re.sub(r"won't", "will not ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub('\W', ' ', text)
    text = re.sub(r'\d+', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip()
    return text

# def process_text(text):
#     text = text.lower()
#     text = remove_punctuations(text)
#     # text = remove_illegal_chars(text)
#     text = reduce_whitespaces(text)
#     return text

def remove_urls(text):
    pass

def process_documents(documents):
    return list(map(process_text, documents))

def remove_stopwords(tokens, stopwords):
    res = []
    for token in tokens:
        if not token in stopwords:
            res.append(token)
    return res


def main():
    documents = ["hello! world. how are you?", "i am nishan"]
    print(process_documents(documents))

if __name__ == "__main__":
    main()

