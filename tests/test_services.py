from ccartao.services.service import Service
from pytest import mark

@mark.test_services
def test_service():
    service = Service(name="Service")
    assert service is not None
    assert service.name == "Service"