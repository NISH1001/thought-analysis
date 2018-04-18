#!/usr/bin/env python3


import glob


def load_data(dirname):
    fnames = glob.glob(dirname)
    files = []
    for fname in fnames:
        if 'bin' in fname or 'jpeg' in fname or 'jpg' in fname:
            continue
        with open(fname) as f:
            files.append(f.read())
    return files

def load_stopwords(fname):
    stopwords = []
    with open(fname) as f:
        for stopword in f:
            stopwords.append(stopword.strip())
    return stopwords


def main():
    data = load_data("data/*")
    print(data)

if __name__ == "__main__":
    main()

