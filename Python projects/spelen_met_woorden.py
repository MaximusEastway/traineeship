"""Function to do the following activities with the woorden.txt set of Dutch words:
        Aantal woorden in dit bestand (zie voorbeeld hierna)
        Het woord met de meeste letters
        Alle palindromen, zoals lepel
        Alle woorden die ‘omgekeerd’ ook voorkomen in de lijst
        Of een ingevoerd woord voorkomt in de lijst, of als onderdeel van woorden
        Alle woorden uit de woordenlijst die je kunt maken van de letters van een ingevoerd woord (anagrammen)
        Woorden die rijmen op een ingevoerd woord
        Maak een raadspel, waarbij je alle letters van het woord in alfabetische volgorde plaatst en waar de gebruiker het oorspronkelijke woord moet raden
"""

def file_reader(filePath):
    """Parse file into list of lines

    Args:
        filePath (string): path to file

    Returns:
        list[string]: list of lines found in file
    """
    try:
        word_file = open(filePath, "rt")
        word_list = word_file.read().splitlines()
        word_file.close()
        return word_list
    except Exception:
        print(f"An error has occured when reading the file.")

    return
    
def character_count(word_list):
    """Find longest word in list, and output length and word itself

    Args:
        word_list (list[string]): list of words

    Returns:
        tuple: tuple of (word_length, word)
    """
    max_len = 0
    max_len_word = ""
    for word in word_list:
        word_len = len(word)
        if word_len > max_len: 
            max_len = word_len
            max_len_word = word
    
    return (max_len, max_len_word)

def find_palindromes(word_list):
    """Find and return all palindromes in the word list

    Args:
        word_list (list[string]): list of words to parse

    Returns:
        list[string]: list of words that are palindromes
    """
    palindrome_list = []

    for word in word_list:
        if check_palindrome(word):
            palindrome_list.append(word)

    return palindrome_list

def check_palindrome(inp_string):
    """Check if the string is the same as the reverse string

    Args:
        inp_string (string): string to asses

    Returns:
        bool: True when string is a palindrome, False if it is not
    """
    if len(inp_string) <= 2:
        return False
    elif inp_string == inp_string[::-1]:
        return True
    else:
        return False

def find_reversed(word_list):
    """Find all the words in the list that also occur in reversed form

    Args:
        word_list (list[string]): list of words to check

    Returns:
        list[string]: list of words that occure reversed in the original list
    """
    reversed_list = []
    word_set = set(word_list)
    for word in word_list:
        if word[::-1] in word_set and not check_palindrome(word):
            reversed_list.append(word)
    return reversed_list

def word_in_list(word_list):
    """Interactive prompt for a word to check if it is in the list of words provided

    Args:
        word_list (list[string]): list of words/strings to check against
    """
    word_set = set(word_list)
    inp_word = ""
    while inp_word != "/q":
        if inp_word == "/q":
            break
        inp_word = input("What word do you want to check? ('/q' to stop) > ")
        if inp_word in word_set:
            print(f"Word '{inp_word}' is in the list!")
        else:
            print(f"Cannot find word '{inp_word}' in the list.")

if __name__ == "__main__":
    word_list = file_reader("woorden.txt")

    print(f"Word count:", len(word_list))

    max_len, max_len_word = character_count(word_list)
    print(f"The longest word is", max_len, "characters long, being", max_len_word)

    palindrome_list = find_palindromes(word_list)
    palindromes_line = "Palindromes in the list:"
    for pal_word in palindrome_list: palindromes_line = f"{palindromes_line}, {pal_word}"
    print(palindromes_line)

    reversed_list = find_reversed(word_list)
    reversed_line = "Reversed in the list: "
    for rev_word in reversed_list: reversed_line = f"{reversed_line}, {rev_word}"
    print(reversed_line)

    word_in_list(word_list)

    print("end of code")