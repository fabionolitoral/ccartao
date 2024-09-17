from ccartao.controllers.controller import Controller
from pytest import mark

@mark.test_controllers
def test_controller():
    controller = Controller(name="Controller")
    assert controller is not None
    assert controller.name == "Controller"