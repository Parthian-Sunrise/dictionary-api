from janome.tokenizer import Tokenizer

def count_japanese_words(sentence):
    # Initialize the tokenizer
    tokenizer = Tokenizer()
    
    # Tokenize the sentence and count the words (tokens)
    tokens = list(tokenizer.tokenize(sentence))
    
    # Return the number of tokens (words)
    return len(tokens)