from difflib import SequenceMatcher

def similar(a,b):
    return SequenceMatcher(None, a, b).ratio()

DB = ['릴파']
f = open('data.txt', encoding='utf-8')
for text in f:
    words = text.split()
    for word in words:
        print(word, "sim : ", similar(word,'릴파'))
        
