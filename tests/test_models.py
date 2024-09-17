from ccartao.models.model import Model
from pytest import mark

@mark.test_models
def test_model():
    model = Model(name="Model")
    assert model is not None