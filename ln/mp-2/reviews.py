import numpy as np
import string
import sys
import nltk
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm, tree
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

porter = PorterStemmer()
wordnet_lemmatizer = WordNetLemmatizer()

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('omw-1.4', quiet=True)
nltk.download('wordnet', quiet=True)

def naive_bayes(x_train, y_train, x_test):
    classifier = MultinomialNB()
    model = classifier.fit(x_train, y_train)
    return model.predict(x_test)

def svm(x_train, y_train, x_test):
    classifier = SVC()
    model = classifier.fit(x_train, y_train)
    return model.predict(x_test)

def knn(x_train, y_train, x_test):
    classifier = KNeighborsClassifier(n_neighbors=7)
    model = classifier.fit(x_train, y_train)
    return model.predict(x_test)

def decision_tree(x_train, y_train, x_test):
    classifier = tree.DecisionTreeClassifier()
    model = classifier.fit(x_train, y_train)
    return model.predict(x_test)

def random_forest(x_train, y_train, x_test):
    classifier = RandomForestClassifier(max_depth=5, random_state=1, n_estimators=50)
    model = classifier.fit(x_train, y_train)
    return model.predict(x_test)

def voting_ensemble(x_train, y_train, x_test):
    classifier = VotingClassifier(estimators=[
        ('NB', MultinomialNB()),
        ('SVM', SVC())
    ], voting='hard')
    model = classifier.fit(x_train, y_train)
    return model.predict(x_test)

def lower_case(reviews):
    new_reviews = []
    for text in reviews:
        text = text.lower()
        new_reviews += [text]
    return new_reviews

def remove_punctuation(reviews):
    new_reviews = []
    for text in reviews:
        text = text.translate(str.maketrans('', '', string.punctuation))
        new_reviews += [text]
    return new_reviews

def remove_stop_words(reviews):
    new_reviews = []
    good_stop_words = ['not', 'no', 'like', 'dont', 'did', 'didnt', 'wont', 'couldnt', 'cant', 'but', 'very', 'really', 'just', 'will', 'good', 'better', 'ok', 'okay', 'best']

    for text in reviews:
        text_tokens = word_tokenize(text)
        new_text = ""
        for word in text_tokens:
            if word in good_stop_words or not word in stopwords.words():
                new_text += word
                new_text += " "
            else: 
                new_text += ""
        new_reviews += [new_text]
    return new_reviews

def stemming(reviews):
    new_reviews = []
    for text in reviews:
        text_tokens = word_tokenize(text)
        new_text = []
        for word in text_tokens:
            new_text.append(porter.stem(word))
            new_text.append(" ")
        new_reviews += ["".join(new_text)]
    return new_reviews

def lemmatization(reviews):
    new_reviews = []
    for text in reviews:
        text_tokens = word_tokenize(text)
        new_text = []
        for word in text_tokens:
            new_text.append(wordnet_lemmatizer.lemmatize(word))
            new_text.append(" ")
        new_reviews += ["".join(new_text)]
    return new_reviews

def transform_labels(labels):
    return [["=Excellent=", "=VeryGood=", "=Good=", "=Unsatisfactory=", "=Poor="].index(l) for l in labels]

def revert_labels(labels):
    label_names = ["=Excellent=", "=VeryGood=", "=Good=", "=Unsatisfactory=", "=Poor="]
    return [label_names[i] for i in labels]

def main():
    y_train = []
    x_train = []
    x_test = []
    test_file = sys.argv[2]
    train_file = sys.argv[4]

    with open(train_file) as train:
        for line in train:
            line = line.split('\t')
            y_train.append(line[0])
            x_train.append(line[1])

    with open(test_file) as test:
        for line in test:
            x_test.append(line)

    # remove punctuation
    x_train = remove_punctuation(x_train)
    x_test = remove_punctuation(x_test)

    # remove stop words
    # x_train = remove_stop_words(x_train)
    # x_test = remove_stop_words(x_test)

    # stemming
    x_train = stemming(x_train)
    x_test = stemming(x_test)

    #lemmatization
    x_train = lemmatization(x_train)
    x_test = lemmatization(x_test)

    x_train = np.array(x_train)
    y_train = np.array(y_train)
    x_test = np.array(x_test)

    count_vect = CountVectorizer(lowercase=True)
    x_train = count_vect.fit_transform(x_train)
    x_test = count_vect.transform(x_test)
    y_train = transform_labels(y_train)

    y_test = {
        "NB": naive_bayes(x_train, y_train, x_test),
        "SVM": svm(x_train, y_train, x_test),
        "KNN": knn(x_train, y_train, x_test),
        "DT": decision_tree(x_train, y_train, x_test),
        "RF": random_forest(x_train, y_train, x_test),
        "VE": voting_ensemble(x_train, y_train, x_test)
    }

    for result in revert_labels(y_test["VE"]):
        print(result)

if __name__ == "__main__":
    main()