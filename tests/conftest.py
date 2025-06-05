import pytest
import requests
from path_constants import RESOURCES_DIR
import os.path
from zipfile import ZipFile

base_url = r'https://github.com/khzrx/test_files/raw/refs/heads/main/'
file_names = ['git-cheat-sheet.pdf', 'deniro.csv', 'terry_okizeme.xlsx']


@pytest.fixture(scope='session', autouse=True)
def download_files():
    for name in file_names:
        file_content = requests.get(url=f'{base_url}{name}').content

        with open(os.path.join(RESOURCES_DIR, name), 'wb') as file:
            file.write(file_content)

    yield

    for name in file_names:
        os.remove(os.path.join(RESOURCES_DIR, name))


@pytest.fixture(scope='session', autouse=True)
def make_zip_file():
    with ZipFile(os.path.join(RESOURCES_DIR, 'acrhive.zip'), mode='w') as zip_file:
        for name in file_names:
            zip_file.write(os.path.join(RESOURCES_DIR, name), name)

    yield

    os.remove(os.path.join(RESOURCES_DIR, 'acrhive.zip'))