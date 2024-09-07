from language_matching.is_japanese_or_english import is_japanese_or_english

class Lemma():
    def __init__(self,lemma,language="Klingon"):
        # Initialise class variables
        self.lemma = lemma
        
        if language == "Klingon":
            self.language = is_japanese_or_english(lemma)
        else:
            self.language = language

    
    def sentence_length(self):

        # Method to calculate length of lemma

        # Copy lemma
        lemma_copy = self.lemma

        # Remove double spaces
        for i in range(0,2):
            lemma_copy = lemma_copy.replace('  ',' ')

        # Remove spaces at the front or end of the string
        lemma_copy = lemma_copy.strip()

        # Compare length before and after removing spaces
        init_len = len(lemma_copy)
        fin_len = len(lemma_copy.replace(' ',''))

        # Number of words definition
        num_words = init_len - fin_len + 1

        # Initialise length
        self.length = num_words

        return num_words

    def is_japanese(word):
        for char in word:
            # Check for Japanese characters (Hiragana, Katakana, Kanji)
            if ('\u3040' <= char <= '\u309F' or  # Hiragana
                '\u30A0' <= char <= '\u30FF' or  # Katakana
                '\u4E00' <= char <= '\u9FBF'):   # Kanji
                return 'Japanese'
        
        # If no Japanese characters were found, assume the word is English
        return 'English'

class Sentence(Lemma):
    def __init__(self,lemma,language="Klingon"):
        super().__init__(lemma,language)
        super().sentence_length()

if __name__ == '__main__':
    print("oi!")