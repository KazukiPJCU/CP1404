import wikipedia


def main():
    title = input("Enter search word: ")
    while title != "":
        try:
            page = wikipedia.page(title, auto_suggest=False)
            print(page.title)
            print(page.url)
            print(page.summary)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
        title = input("Enter search word: ")


if __name__ == '__main__':
    main()
