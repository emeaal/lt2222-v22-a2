import gzip
import random
import nltk
from nltk.tokenize import WordPunctTokenizer
from nltk.corpus import stopwords
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score


def sample_lines(file, lines):
    unzipped_file = gzip.open(file, 'rt')
    contents = unzipped_file.readlines()
    randomized_content = random.sample(contents, k=lines)

    return randomized_content


def process_sentences(sampled_lines):
    tk = WordPunctTokenizer()
    not_processed_sent = []
    tagged_sentences = []
    for line in sampled_lines:
        tokenized_text = tk.tokenize(line)
        not_processed_sent.append(tokenized_text)

    for sent in not_processed_sent:
        tagged_sentence = nltk.pos_tag(sent)
        tagged_sentences.append(tagged_sentence)

    long_sentences = []
    for sentence in tagged_sentences:
        if len(sentence) < 5:
            continue
        else:
            long_sentences.append(sentence)

    stop_words = set(stopwords.words('english'))
    filter_sentence = []
    processed_sentences = []
    for sentence in long_sentences:
        for word, pos in sentence:
            word = word.lower()
            if word in stop_words:
                continue
            elif len(word) < 2:
                continue
            elif not word.isalpha():
                continue
            elif word == ".": #redundant?
                continue
            else:
                pos_pair = (word, pos)
                filter_sentence.append(pos_pair)
        processed_sentences.append(filter_sentence)

    return processed_sentences


def last_char(word):      # Helper function for getting last characters from words
    last_chars = word[-2:]

    return last_chars


def create_samples(processed_sentences, samples=50):
    five_words = []
    sample_size = 5
    for sentence in processed_sentences:
        sorted_sample = [sentence[i] for i in sorted(random.sample(range(len(sentence)), sample_size))]
        if len(five_words) < samples:
            five_words.append(sorted_sample)
        else:
            break

    all_samples = []
    for pair1, pair2, pair3, pair4, pair5 in five_words:
        word1 = last_char(pair1[0]) + "_1"
        word2 = last_char(pair2[0]) + "_2"
        pos_tag = pair3[1]  # POS tag for third pair, look for VERB
        word4 = last_char(pair4[0]) + "_3"
        word5 = last_char(pair5[0]) + "_4"

        if "V" in pos_tag:
            verb_score = 1
        else:
            verb_score = 0

        sample = (word1, word2, word4, word5), verb_score
        all_samples.append(sample)

    return all_samples


def create_df(all_samples):
    features = []
    tested_set = set()
    for sample in all_samples:
        feature = sample[0]
        for item in feature:
            if item not in tested_set:
                features.append(item)
                tested_set.add(item)
    features.append("v")

    datacounter = []
    for sample in all_samples:
        counter = []
        word_ending = sample[0]
        yesno = sample[1]
        for item in features:
            if item != "v":
                if item in word_ending:
                    counter.append(1)
                else:
                    counter.append(0)
        counter.append(yesno)
        datacounter.append(counter)

    df = pd.DataFrame(datacounter, columns=features)

    return df


def split_samples(fulldf, test_percent=20):
    size_test = test_percent / 100
    y = fulldf.loc[:, 'v'].values
    fulldf.drop('v', inplace=True, axis=1)
    X = fulldf
    train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=size_test)

    return train_X, train_y, test_X, test_y


def train(train_X, train_y, kernel='linear'):
    kern = kernel
    clf = svm.SVC(kernel=kern)
    clf.fit(train_X, train_y)

    return clf


def eval_model(model, test_X, test_y):
    y_pred = model.predict(test_X)
    precision = precision_score(test_y, y_pred)
    recall = recall_score(test_y, y_pred)
    f1 = f1_score(test_y, y_pred)

    print("Modelname: ", model)
    print("Precision: ", precision, "Recall: ", recall, "F1: ", f1)
