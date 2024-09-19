from ccartao.models.model import Model
from pytest import mark

@mark.test_models
def test_model():
    model = Model(id=1)
    assert model is not None