"""
Title: Generate secure passphrases using diceware.
Author: Primus27
Version: 1.0
"""

# Import packages
import argparse
from pathlib import Path
from sys import exit
from Passphrase import PassphraseGen

# Current program version
current_version = 1.0


def main():
    """
    Main method
    """
    # Title card
    print("Diceware Password Generation Tool")
    print(f"Current version: {current_version}\n")

    # Open wordlist and read data
    with open(wordlist_path, "r") as wordlist_data:
        wordlist_data = wordlist_data.readlines()

    # Create passphrase object containing user params
    passphrase_obj = PassphraseGen(n_words, n_symbols, n_numbers, append_flag, wordlist_data, word_separator)

    print(f"Generating {quantity} passphrases:\n")

    # Output passphrases
    for i in range(quantity):
        print(f"{i+1}) {passphrase_obj.get_pass()}\n")


if __name__ == '__main__':
    # Define argument parser
    parser = argparse.ArgumentParser()
    # Remove existing action groups
    parser._action_groups.pop()

    # Create a required and optional group
    optional = parser.add_argument_group("optional arguments")

    # Define arguments
    optional.add_argument("-nW", "--words", action="store", default="6",
                          dest="arg_n_words",
                          help="Specify number of words to be generated")
    optional.add_argument("-nS", "--symbols", action="store", default="2",
                          dest="arg_n_symbols",
                          help="Specify number of symbols to be generated")
    optional.add_argument("-nN", "--numbers", action="store", default="2",
                          dest="arg_n_numbers",
                          help="Specify number of numbers to be generated")
    optional.add_argument("-a", "--append", action="store_true", dest="arg_append_flag",
                          help="Append numbers to words/symbols (rather than treating as a separate word)")
    optional.add_argument("-w", "--wordlist", action="store", default="",
                          dest="arg_wordlist", help="Declare a custom wordlist")
    optional.add_argument("-s", "--separator", action="store",
                          default=" ", dest="arg_separator",
                          help="Declare a character as the word separator")
    optional.add_argument("-q", "--quantity", action="store",
                          default="1", dest="arg_quantity",
                          help="Specify number of passphrases to generate")
    optional.add_argument("--version", action="version",
                          version=f"%(prog)s {current_version}",
                          help="Display program version")
    args = parser.parse_args()

    try:
        n_words = int(args.arg_n_words)
    except ValueError:
        exit("Number of words not an integer.")

    try:
        n_symbols = int(args.arg_n_symbols)
    except ValueError:
        exit("Number of symbols not an integer.")

    try:
        n_numbers = int(args.arg_n_numbers)
    except ValueError:
        exit("Number of numbers not an integer.")

    append_flag = args.arg_append_flag

    # Wordlist
    default_wordlist = "eff_large_wordlist.txt"
    user_wordlist_path = args.arg_wordlist
    if user_wordlist_path and Path(user_wordlist_path).is_file():
        wordlist_path = Path(user_wordlist_path)
    else:
        if user_wordlist_path:
            print(f"Wordlist not found. Program using default file: {default_wordlist}")
        wordlist_path = Path(default_wordlist).absolute()

    word_separator = args.arg_separator

    try:
        quantity = int(args.arg_quantity)
    except ValueError:
        exit("Quantity not an integer.")

    # Run main method
    main()
