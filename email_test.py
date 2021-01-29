from conftest import *
from func import *


@pytest.mark.usefixtures("log")
@pytest.mark.parametrize('email, result', (
        ["test@test.ru", True],
        ["w@w.com", True],
        ["123QWE@mmm.mmm", True],
        ["test@test.", False],
        ["w@.", False],
        ["@tt.", False]
))
def test_valid_email(email, result):
    assert valid_email(email) == result
