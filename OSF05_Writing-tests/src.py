from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split


def load(train_size=0.8):
    digits = datasets.load_digits()
    n_samples = len(digits.images)
    data = digits.images.reshape((n_samples, -1))
    X_train, X_test, y_train, y_test = train_test_split(
        data, digits.target, train_size=train_size
    )
    return (X_train, X_test, y_train, y_test)


def train(X_train, y_train, C=1.0, gamma=0.001):
    classifier = svm.SVC(C=C, gamma=gamma)
    classifier.fit(X_train, y_train)
    train_preds = classifier.predict(X_train)
    train_score = metrics.accuracy_score(y_train, train_preds)
    print("Training accuracy score {:.3f}".format(train_score))
    return classifier, train_score


def evaluate(classifier, X_test, y_test):
    test_preds = classifier.predict(X_test)
    test_score = metrics.accuracy_score(y_test, test_preds)
    print("Test accuracy score {:.3f}".format(test_score))
    return test_score
