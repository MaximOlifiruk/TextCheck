import pandas as pd
import regex as re
from nltk.tokenize import RegexpTokenizer


def print_data(data):
    for elem in data:
        print(elem)


def cleaning_data(file_name):
    data = open(file_name, 'r').read()
    data = cleaning_check_data(data)
    return data


def cleaning_check_data(data):
    data = re.sub(r"\[\d+\]", "", data)
    data = re.sub(r"\([А-Яа-я ,.'A-Za-z0-9]+\)", "", data)
    data = re.sub(r"[,!?@\'\`\"\_\n«»:;()]", "", data)
    data = re.sub(r"[-—]", " ", data)
    data = data.split(".")
    return data


def create_dataframe_check(main, not_main):
    return pd.DataFrame({
        'text': main + not_main,
        'class_label': [1 for i in range(0, len(main))] + [0 for i in range(0, len(not_main))]
    })


def create_dataframe_main(main):
    return pd.DataFrame({
        'text': main,
        'class_label': [1 for i in range(0, len(main))]
    })


def tokenize(data):
    tokenizer = RegexpTokenizer(r'\w+')
    data["tokens"] = data["text"].apply(tokenizer.tokenize)


def create_data(file_name):
    main = cleaning_data(file_name)
    not_main = cleaning_data("notMain.txt")
    global clean_data
    clean_data = create_dataframe_check(main, not_main)
    tokenize(clean_data)


def give_text(obj):
    data_check = cleaning_check_data(str(obj.get("1.0", "end-1c")))
    global clean_data_check
    clean_data_check = create_dataframe_main(data_check)
    tokenize(clean_data_check)


def find_accuracy(obj, label_accuracy):
    give_text(obj)
    text = pd.concat([clean_data, clean_data_check], axis=0)

    from sklearn.feature_extraction.text import CountVectorizer
    text_vec = CountVectorizer().fit_transform(text['text'])

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(text_vec, text['class_label'],
                                                        test_size=clean_data_check.size / (clean_data_check.size + clean_data.size)
                                                        , random_state=0, shuffle=False)

    from sklearn import ensemble
    classifier = ensemble.GradientBoostingClassifier(
        n_estimators=1000,
        learning_rate=0.5,
        max_depth=2,
    )

    classifier.fit(X_train, y_train)
    predictions = classifier.predict(X_test)

    from sklearn import metrics
    label_accuracy["text"] = "Точность: " + str(metrics.accuracy_score(y_test, predictions))







