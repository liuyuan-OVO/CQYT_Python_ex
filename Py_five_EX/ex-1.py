def count_words(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

sentence = input("输入一个英文句子：")
result = count_words(sentence)
print("每个单词出现的次数：")
for word, count in result.items():
    print(f"{word}: {count}")