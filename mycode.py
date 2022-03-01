import nltk
from nltk.tokenize import WordPunctTokenizer
from nltk.corpus import stopwords


def sample_lines(file, lines):
    unzipped_file = gzip.open(file, 'rt')
    contents = unzipped_file.readlines()
    randomized_content = random.choices(contents, k=lines)

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
            elif word == ".":
                continue
            else:
                pos_pair = (word, pos)
                filter_sentence.append(pos_pair)
        processed_sentences.append(filter_sentence)

    return processed_sentences
