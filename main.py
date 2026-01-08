import sys

if len(sys.argv) == 2:
    print("Usage: python3  main.py <path_to_book>")

    def get_book_text(file_path):
        with open(file_path) as f:
            file_text = f.read()
            return file_text

    def main():
        file_path = sys.argv[1]
        file_text = get_book_text(file_path)
        from stats import word_counter
        from stats import character_counter
        from stats import sorted_dic_lists
        word_counter = word_counter(file_text)
        char_counter = character_counter(file_text)
        sorted_dic_lists = sorted_dic_lists(char_counter)
        print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...")
        print(f"----------- Word Count ----------\n{word_counter}")
        print(f"--------- Character Count -------")

        for dic in sorted_dic_lists:
            good_boy = dic["char"]
            check_for_good_boy = good_boy.isalpha()
            if check_for_good_boy == True:
                print(f"{dic["char"]}: {dic["nums"]}")

        print("============= END ===============")

    main()
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)