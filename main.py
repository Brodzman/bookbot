def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    lowered_string = text.lower()
    num_characters = count_characters(lowered_string)
    for char_dict in num_characters:
        print(f'The \'{char_dict["char"]}\' character was found {char_dict["num"]} times')


def count_characters(text):
    counter = {}
    for character in text:
        if character in counter:
            counter[character] += 1
        else:
            counter[character] = 1
    chars_list = []
    for char, count in counter.items():
        if char.isalpha():
            char_dict = {'char': char, 'num': count}
            chars_list.append(char_dict)
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

def sort_on(dict):
    return dict["num"]


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

