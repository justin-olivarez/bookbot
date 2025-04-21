def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_dict(text):
    chars = {}
    for char in text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_on(item):
    return item["number"]

def get_sorted_dict(char_dict):
    sorted_list = []
    for char in char_dict:
        sorted_list.append({
            "character": char,
            "number": char_dict[char]
        })
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list