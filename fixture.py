import pytest

file = "log.txt"


@pytest.fixture()
def log(file_name, text):
    with open(file_name, 'w') as f_obj:
        f_obj.write(text)

