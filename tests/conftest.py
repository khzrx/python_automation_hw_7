import pytest
import requests
import constants as c
import os.path
from zipfile import ZipFile


@pytest.fixture(scope='session', autouse=True)
def download_files_and_delete():
    if not os.path.exists(c.RESOURCES_DIR):
        os.mkdir(c.RESOURCES_DIR)

    for name in c.FILE_NAMES.values():
        file_content = requests.get(url=f'{c.BASE_URL}{name}').content

        with open(os.path.join(c.RESOURCES_DIR, name), 'wb') as file:
            file.write(file_content)

    yield

    for name in c.FILE_NAMES.values():
        os.remove(os.path.join(c.RESOURCES_DIR, name))


@pytest.fixture(scope='session', autouse=True)
def make_zip_file_and_delete():
    with ZipFile(os.path.join(c.RESOURCES_DIR, c.ARCHIVE_NAME), mode='w') as zip_file:
        for name in c.FILE_NAMES.values():
            zip_file.write(os.path.join(c.RESOURCES_DIR, name), name)

    yield

    os.remove(os.path.join(c.RESOURCES_DIR, c.ARCHIVE_NAME))

@pytest.fixture(scope='session')
def zip_file():
    with ZipFile(os.path.join(c.RESOURCES_DIR, c.ARCHIVE_NAME)) as file:
        yield file