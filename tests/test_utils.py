from ccartao.utils.util import Util
from pytest import mark
from datetime import datetime

@mark.test_utils
def test_utils():
    util = Util()
    assert Util is not None

@mark.test_utils
def test_utils_get_date():
    assert Util.get_date() is not None
    data_atual = datetime.now().strftime('%Y-%m-%d')
    assert Util.get_date() == data_atual