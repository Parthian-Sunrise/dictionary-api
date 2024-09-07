from language_matching.is_japanese_or_english import is_japanese_or_english
from japanese_specific.japanese_num_words import count_japanese_words

class Lemma():
    def __init__(self,lemma,language="Klingon"):
        # Initialise class variables
        self.lemma = lemma
        
        if language == "Klingon":
            self.language = is_japanese_or_english(lemma)
        else:
            self.language = language

        self.length = self.sentence_length()

    
    def sentence_length(self):
        if self.language == "English":
            # Method to calculate length of lemma
    
            # Copy lemma
            lemma_split = self.lemma.split()
    
            num_words = len(lemma_split)
    
            return num_words

        elif self.language == "Japanese":
            num_words = count_japanese_words(self.lemma)

            return num_words

        def list_of_words(self):
            if language == "English":
                word_list = self.lemma.split()
            else:
                word_list = 

class Sentence(Lemma):
    def __init__(self,lemma,language="Klingon"):
        super().__init__(lemma,language)

if __name__ == '__main__':
    print("oi!")