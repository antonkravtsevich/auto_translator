import nltk
import pandas as pd
import sys
from tqdm import tqdm

from docx import Document
from nltk.corpus import stopwords 
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize 



class DictionaryGenerator():

    def __init__(self, df, document, words_count):
        self.df = df
        self.document = document
        self.words_count = words_count
        self.lemmatizer = WordNetLemmatizer()
        self.dictionary_words = set()
        self.stop_words = set(stopwords.words('english'))
        self.process_document()
        

    def get_word_position(self, word):
        """
        Get place of word in frequency dictionary
        The more this word is mentioned in english language = the higher the place will be
        """
        try:
            return self.df[self.df['word']==word].index.tolist()[0]    
        except IndexError:
            # word not in dictionary
            return 0


    def get_word_normal_form(self, word):
        return self.lemmatizer.lemmatize(word, 'v')


    def update_words_set_by_article(self, article):
        """
        Clean article data and add all new words to words set
        """
        to_replace = '(){}[],.!?"'
        for symbol in to_replace:
            article = article.replace(symbol, ' ')
        article = article.strip()
        article = article.lower()
        article_words = word_tokenize(article)
        filtered_article_words = [word for word in article_words if word not in self.stop_words]
        normalized_words = [self.get_word_normal_form(word) for word in filtered_article_words]
        self.dictionary_words.update(normalized_words)
    

    def process_document(self):
        table = self.document.tables[0]
        for row in tqdm(table.rows):
            article = row.cells[0].text
            self.update_words_set_by_article(article)


    # TODO: remove this function
    def show_words_debug(self):
        words = list(self.dictionary_words)
        words = sorted(words, key=lambda a: self.get_word_position(a))
        for word in words:
            print('{}: {}'.format(word, self.get_word_position(word)))


    def get_rearest_words(self):
        words = list(self.dictionary_words)
        words = sorted(words, key=lambda a: self.get_word_position(a), reverse=True)[:self.words_count]
        return words


def main():
    try:
        filename = sys.argv[1]
        words_count = int(sys.argv[2])
    except IndexError:
        print('Use "python3 auto_dictionary_generator.py %filename%" %words_count%')
        sys.exit()

    nltk.download('stopwords')

    df = pd.read_csv('./data/unigram_freq.csv')
    document = Document(filename)

    dictionary_generator = DictionaryGenerator(df, document, words_count)

    print(dictionary_generator.show_words_debug())



if __name__ == '__main__':
    main()