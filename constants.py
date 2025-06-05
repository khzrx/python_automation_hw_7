import os.path

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR =  os.path.dirname(CURRENT_FILE)
RESOURCES_DIR = os.path.join(CURRENT_DIR, 'resources')
BASE_URL = r'https://github.com/khzrx/test_files/raw/refs/heads/main/'
ARCHIVE_NAME = 'archive.zip'
FILE_NAMES = {
    'pdf': 'git-cheat-sheet.pdf',
    'csv': 'deniro.csv',
    'xlsx': 'terry_okizeme.xlsx'
}