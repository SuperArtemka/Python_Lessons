# Подсчет разделенных пробелом слов в тексте

text = "She sells sea shells on the sea shore The shells that she sells are sea shells "\
"I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"

text = set(text.split(' '))

print(len(text))
print(text) 