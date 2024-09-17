from ccartao.views.view import View
from pytest import mark

@mark.test_views
def test_view():
    view = View(name="View")
    assert view is not None
    assert view.name == "View"

