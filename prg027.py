def analyze_text(text):
    words = text.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

text = "Dnes jsem vstal a najedl jsem se."
word_count_result = analyze_text(text)
print("Word count analysis:")
for word, count in word_count_result.items():
    print(f"'{word}' occurs {count} times")