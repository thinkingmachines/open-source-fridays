import pipeline


def test_pipeline_return_types():
    """Test that pipeline returns the correct types"""
    train_score, test_score = pipeline.refactored_pipeline()
    assert isinstance(train_score, float)
    assert isinstance(test_score, float)
