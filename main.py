def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)

    word_count = get_word_count(text)
    character_count = get_character_count(text)
    sorted_character_count = sort_char_list(character_count)
    

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in document")
    print("")

    for char in sorted_character_count:
        if char['char'].isalpha():
            print(f"The '{char['char']}' found in the document {char['num']} times")

    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(sentence):
    return(len(sentence.split()))

def get_character_count(sentence):
    char_counts = {}

    for char in sentence:
        lower_char = char.lower()
        if lower_char in char_counts:
            char_counts[lower_char] += 1
        else:
            char_counts[lower_char] = 1
    
    return char_counts

def sort_on(key):
    return key["num"]

def sort_char_list(characters):
    sorting_list = []

    for char in characters:
        sorting_list.append({"char": char, "num": characters[char]})
    
    sorting_list.sort(reverse=True, key=sort_on)
    return sorting_list

main()