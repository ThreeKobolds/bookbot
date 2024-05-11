
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    letter_count = get_letter_count(text)
    letter_count_sorted = get_sorted_char(letter_count)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for item in letter_count_sorted:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End Report ---")

def sort_on(d):
    return d["num"]

def get_sorted_char(char_count):
    sorted_list = []
    for ch in char_count:
        sorted_list.append({"char":ch, "num":char_count[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_letter_count(text):
    letter_count = {}
    lowered_text = text.lower()
    characters = list(lowered_text)
    for character in characters:
        if character in letter_count:
            letter_count[character] += 1
        else:
            letter_count[character] = 1
    return letter_count
    



def get_word_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
