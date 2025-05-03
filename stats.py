def get_num_words(book_contents):
    word_count = 0
    
    words = book_contents.split(' ')

    for word in words:
        word_count += 1

    # Word count is just plain different
    # word_count = 75767
    return word_count

def get_char_count(book_contents):
    char_dict = dict()
    for char in book_contents:
        if char_dict.get(char.lower()) == None:
            # Must not be in the dict, so add it
            char_dict.update({char.lower(): 1})
        else:
            # Must already be in the dict
            value = char_dict.get(char.lower())
            char_dict.update({char.lower(): value + 1})
    return char_dict

# func to enable the dict.sort inbuilt python func
def sort_on(dict):
    return dict["num"]

def sort_chars_count(char_dict):
    dict_list = []
    for key in char_dict:
        app_dict = {
            "char": key,
            "num": char_dict.get(key)
        }
        dict_list.append(app_dict)
    dict_list.sort(reverse=True, key=sort_on)
    
    return dict_list