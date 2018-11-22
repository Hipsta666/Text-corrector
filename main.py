def special_char(text):
    """The function places a space after the “,” sign and removes the space before it."""
    line = ""
    if text[-1:] == "," :
        text = text[:-1] + "."
    for char in range(len(text)):
        if text[char] == "," and text[char - 1] == " ":
            line = line[:line.find(" ", line.find(" ")+char)] + ","
        if text[char] == "," and text[char + 1] != " " and text[char - 1] != " ":
            line += ","
        if text[char] == "," and text[char + 1] != " ":
            line += " "
        else:
            line += text[char]
    line = line.replace(",,", ",")
    print(line)


def main():
    string = input()
    special_char(string)


if __name__ == '__main__':
    main()

main()
