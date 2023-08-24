
import pytest 
from api_4 import ReqList

@pytest.fixture 
def setup():
    yield

def test1():
    ReqList.testAPI()