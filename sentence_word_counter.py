paragraph = "here are some words. there can be more than one sentence in this text. you will count them using python."

sentences = paragraph.split(".")
print(len(sentences) - 1)
word_count = 0
for i in sentences:
    word_count = word_count + len(i.split())

print(word_count)