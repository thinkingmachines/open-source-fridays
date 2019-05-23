import src
import pytest
from sklearn import svm


def test_load_return_length():
    """Test that load return an iterable of length 4"""
    output = src.load()
    assert output


@pytest.mark.parametrize("size", [0.25, 0.50, 0.75])
def test_load_return_shape(size):
    """Test that the return shapes are correct"""
    X_train, X_test, y_train, y_test = src.load(train_size=size)
    num_samples = 1797
    assert X_train.shape == (int(num_samples * size), 64)
    assert X_test.shape == (int(num_samples * (1 - size)) + 1, 64)


@pytest.mark.parametrize("C", [1.0, 10, 100])
@pytest.mark.parametrize("gamma", [0.1, 0.01, 0.001])
def test_train(C, gamma):
    """Test that train returns the expected types"""
    X_train, X_test, y_train, y_test = src.load()
    clf, score = src.train(X_train, y_train)
    assert isinstance(clf, svm.SVC)
    assert isinstance(score, float)


def test_evaluate():
    """Test that evaluate returns a float"""
    X_train, X_test, y_train, y_test = src.load()
    clf, score = src.train(X_train, y_train)
    test_score = src.evaluate(clf, X_test, y_test)
    assert isinstance(test_score, float)
