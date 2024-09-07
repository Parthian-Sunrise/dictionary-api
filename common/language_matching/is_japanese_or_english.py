def is_japanese_or_english(word):
    for char in word:
        # Check for Japanese characters (Hiragana, Katakana, Kanji)
        if ('\u3040' <= char <= '\u309F' or  # Hiragana
            '\u30A0' <= char <= '\u30FF' or  # Katakana
            '\u4E00' <= char <= '\u9FBF'):   # Kanji
            return 'Japanese'
    
    # If no Japanese characters were found, assume the word is English
    return 'English'