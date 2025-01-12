def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    lowered_string = text.lower()
    num_characters = count_characters(lowered_string)
    print(num_characters)

def count_characters(text):
    counter = {}
    for character in text:
        if character in counter:
            counter[character] += 1
        else:
            counter[character] = 1
        
    return counter


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

