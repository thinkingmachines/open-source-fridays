from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split


def run_pipeline():
    """MNIST classification pipeline that we will refactor"""

    # Step 1
    # Load and split the dataset
    # Task: Create a function, load(), with the ff specs:
    # Input: train_size (float) with default value of 0.8
    # Output: 4-tuple of numpy.ndarrays
    digits = datasets.load_digits()
    n_samples = len(digits.images)
    data = digits.images.reshape((n_samples, -1))
    X_train, X_test, y_train, y_test = train_test_split(data, digits.target)

    # Step 2
    # Train the model
    # For the time being we'll just use a simple SVM clasifier
    # Task: Create a function, train(), with the ff specs
    # Inputs:
    #         X_train (numpy.ndarray), input images for training
    #         y_train (numpy.ndarray), input labels for training
    #         C (float), C value for SVM default is 1.0
    #         gamma (float), gamma value for SVM default is 0.001
    # Output:
    #         svm.SVC, the trained model
    #         float, the training accuracy score
    classifier = svm.SVC(C=1, gamma=0.001)
    classifier.fit(X_train, y_train)
    train_preds = classifier.predict(X_train)
    train_score = metrics.accuracy_score(y_train, train_preds)
    print("Training accuracy score {:.3f}".format(train_score))

    # Step 3
    # Predict and evaluate the model
    # Task: Create a function, evaluate(), with the ff specs
    # Inputs:
    #         classifier (svm.SVC), a trained SVM classifier
    #         X_test (numpy.ndarray), input images to test
    #         y_test (numpy.ndarray), ground-truth labels
    # Output:
    #         float, the accuracy score
    test_preds = classifier.predict(X_test)
    test_score = metrics.accuracy_score(y_test, test_preds)
    print("Test accuracy score {:.3f}".format(test_score))

    return train_score, test_score


def refactored_pipeline():
    """You should import the refactored methods here"""

    # Step 1
    # You should put the `load` method here:
    # X_train, X_test, y_train, y_test = src.load()

    # Step 2
    # You should put the `train` method here:
    # model, train_score = src.train(X_train, y_train)

    # Step 3
    # You should put the `evaluate` method here:
    # test_score = src.evaluate(model,X_test, y_test)

    # Final Step
    # Return the train_score and test_score
    # return train_score, test_score

    pass
