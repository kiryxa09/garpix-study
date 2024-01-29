def longest_words(file):
  with open(file, 'r', encoding='utf-8') as f:
    words = f.read().split()
    max_length = max(len(word) for word in words)
    return [word for word in words if len(word) == max_length]

print(longest_words('c://Users/bkd/dev/garpix-study/Тема 7/poem.txt'))