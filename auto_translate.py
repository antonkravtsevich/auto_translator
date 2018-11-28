from docx import Document
from py_translator import Translator
from tqdm import tqdm
import sys


def main():
    try:
        filename = sys.argv[1]
    except IndexError:
        print('Use "python3 auto_translate.py %filename%"')
        sys.exit()

    translator = Translator()

    document = Document(filename)
    table = document.tables[0]
    for row in tqdm(table.rows):
        eng_cell = row.cells[0]
        ru_cell = row.cells[1]
        if eng_cell.text:
            if not ru_cell.text:
                text = translator.translate(eng_cell.text, src='en', dest='ru').text
                ru_cell.text = text

    document.save('auto_translated__'+filename)
    print('Done')
    
if __name__ == '__main__':
    main()