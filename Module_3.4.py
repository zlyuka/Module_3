def single_root_words(root_word, *other_words):
    same_words = []
    for root_words in other_words:
        other_words_lower = root_words.lower()
        if root_word.lower() in other_words_lower or other_words_lower in root_word.lower():
            same_words.append(root_words)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
