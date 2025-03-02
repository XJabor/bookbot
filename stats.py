def word_counting(text):
    words = text.split()
    return len(words)

def character_count(text):
    working = {}
    text = text.lower()
    for character in text:
        if character not in working:
            working[character] = 1
        else:
            working[character] += 1
    return working

def sort_on(char_counts):
        chars_list = []
        for char, count in char_counts.items():
            char_dict = {"char": char, "count": count}
            chars_list.append(char_dict)
        chars_list.sort(reverse=True, key=lambda x: x["count"])
        return chars_list
