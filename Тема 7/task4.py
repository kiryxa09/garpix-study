def word_in_text(textfile, word):
  with open(textfile, 'r', encoding='utf-8') as f:
    counter = 0
    for line in f:
      if word.lower() in line.lower():
        counter += 1
  return counter


print(word_in_text('c://Users/bkd/dev/garpix-study/Тема 7/poem.txt', 'таракан'))