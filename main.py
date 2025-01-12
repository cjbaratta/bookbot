def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    return report(book_path, text)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def find_word_count(x):
    wc = 0
    t = x.split()
    for word in t:
        wc += 1
    return wc

def count_characters(text):
    text = text.lower()
    char_counts = {}
    for char in text:
        if char in char_counts and char.isalpha():
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def report(bookpath, text):
    print(f"--- Begin report of {bookpath} ---")
    wc = find_word_count(text)
    print(f"{wc} words found in the document")
    print()
    chars = count_characters(text)
    sorted = chars_dict_to_sorted_list(chars)
    for item in sorted:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End Report ---")


main()