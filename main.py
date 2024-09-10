def main():
    path = "books/frankenstein.txt"
    text = get_text(path)

    word_count = count_words(text)
    characters = count_characters(text)
    characters_list = [{"name": char, "num": characters[char]} for char in characters]
    characters_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print("")
    for item in characters_list:
        c = item["name"]
        n = item["num"]
        if c.isalpha():
            print(f"The '{c}' character was found {n} times")
    print("--- End report ---")


def get_text(path):
    with open(path) as f:
        text = f.read()
    return text


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    characters = {}
    words = text.lower().split()

    for word in words:
        for char in word:
            if char not in characters:
                characters[char] = 1
            else:
                characters[char] += 1

    return characters


def sort_on(dict):
    return dict["num"]


main()
