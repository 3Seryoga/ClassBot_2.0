from utils import edits


def main():
    while True:
        user_input = input("Введіть команду: ")
        res = edits(user_input)
        print(res)
        if res == "До наступної зустрічі":
            break

if __name__ == "__main__":
    main()