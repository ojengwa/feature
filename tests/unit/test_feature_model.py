"""
This file (test_feature_model.py) contains the unit tests for the Feature model.
"""


def test_new_feature_request(new_feature_request):
    """
    GIVEN a FeatureRequest model
    WHEN a new FeatureRequest is created
    THEN check the title, client_priority, requested_by, 
    description fields are defined correctly
    """
    assert new_feature_request.title == 'Lorem Ipsum'
    assert new_feature_request.client_priority == 1
    assert new_feature_request.requested_by == 1
    assert 'Palladium, promethium,' in new_feature_request.description


def test_feature_request_id(new_feature_request):
    """
    GIVEN an existing FeatureRequest
    WHEN the ID of the feature_request is defined to a value
    THEN check the feature_request ID returns a string (and not an integer) as needed by Flask-WTF
    """
    new_feature_request.id = 17
    assert isinstance(new_feature_request.get_id(), str)
    assert not isinstance(new_feature_request.get_id(), int)
    assert new_feature_request.get_id() == "17"
