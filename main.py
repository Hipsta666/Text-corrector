def special_char(text):
    """The function places a space after the “,” sign and removes the space before it."""
    line = ""
    if text[-1:] == ",":
        text = text[:-1] + "."
    for char in range(len(text)):
        if text[char] == "," and text[char - 1] == " " and text[char + 1] != " ":
            line = line[:line.find(" ", line.find(" ") + char)]
        if text[char] == "," and text[char + 1] == " " and text[char - 1] == " ":
            line = text[:text.find(",") - 1]
        if text[char] == "," and text[char + 1] != " ":
            line += "," " "
        else:
            line += text[char]
    return line


def special_point_before(text):
    """The function places deletes a space before the sign "."."""
    line = ""
    for letter in range(len(text)):
        if text[letter] == "." and text[letter - 1] == " ":
            line = line[:line.find(" ", line.find(" ") + letter)]
        if text[letter] == "!" and text[letter - 1] == " ":
            line = line[:line.find(" ", line.find(" ") + letter)]
        if text[letter] == "?" and text[letter - 1] == " ":
            line = line[:line.find(" ", line.find(" ") + letter)] + "?"
        else:
            line += text[letter]
    return line


def special_point_after(text):
    """The function places a space after the “.” sign."""
    line = ""
    text += " "
    for letter in range(len(text)):
        if text[letter - 1] == "." and text[letter] != " ":
            line += " "
        if text[letter - 1] == "?" and text[letter] != " ":
            line += " "
        if text[letter - 1] == "!" and text[letter] != " ":
            line += " " + text[letter]
        else:
            line += text[letter]
    return line


def capital_letters(text):
    """The function starts a sentence with a capital letter."""
    line = ""
    text = text[0].upper() + text[1:]
    for letter in range(len(text)):
        if text[letter - 2] in "!.?":
            line += text[letter].upper()
        else:
            line += text[letter]
    print("\n" + line)

def correct_transfer(string, length):
    """The function makes the text from the entered string, making a transfer to a new one after 60 characters."""
    lines = ""
    scorer = 1
    reduction = 0
    for num in range(len(string)):
        if num > length * scorer + reduction and string[num] == " ":
            lines += "\n"
            reduction = len(string[:num]) - length * scorer
            scorer += 1
        else:
            lines += string[num]
    return lines


try:
    def main():
        """Main function performing all operations."""
        string = str(input("Enter a string of any length: "))
        string_length = int(input("Enter the length of the text line: "))
        strip_1 = special_char(string)
        strip_2 = special_point_before(strip_1)
        strip_3 = special_point_after(strip_2)
        strip_4 = correct_transfer(strip_3, string_length)
        capital_letters(strip_4)

    if __name__ == '__main__':
        main()

except ValueError:
    print("Please enter integer values.\nGoodbye!")