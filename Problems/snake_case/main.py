import string

word = input()
final_word = ''
for i in word:
    if i in string.ascii_lowercase:
        final_word += i
    else:
        final_word += '_' + i.lower()
print(final_word)
