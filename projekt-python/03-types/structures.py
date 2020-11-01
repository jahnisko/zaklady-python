def charFrequency(text):
    result = [(char, text.count(char)) for char in set(text)]
    return sorted(result, key=lambda polozka: polozka[1], reverse=True)

text = "Tři sta třicet tři stříbrných stříkaček přestříkalo přes tři sta třicet tři stříbrných střech."
print(f'Věta: {text}')
print('Četnost výskytu písmen:')
print('-----------------------')
print(charFrequency(text))