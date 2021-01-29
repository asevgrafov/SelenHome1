import pytest


@pytest.fixture(scope="session")
def log(file_name="log.txt", text="All tests passed"):
    with open(file_name, 'w') as f_obj:
        f_obj.write(text)
