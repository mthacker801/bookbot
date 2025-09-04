def get_book_text(text):
    with open(text) as f:
        return f.read()
    
def get_word_count(text):
    doc = get_book_text(text)
    words = doc.split()
    num_words = len(words)
    
    #return num_words
    print(f"Found {num_words} total words")

def get_char_count(text):
    char_counts = {}
    doc = (get_book_text(text).lower())
    for i in doc:
        if i.isalpha():
            char_counts[i] = char_counts.get(i, 0) + 1
    return char_counts
    
def sort_on(char_dict):
    lst = [{'char': key, 'num': value}
           for key, value in char_dict.items()
           ]
    lst.sort(key=lambda d: d['num'], reverse=True)
    for item in lst:
        print(f"{item["char"]}: {item["num"]}")





