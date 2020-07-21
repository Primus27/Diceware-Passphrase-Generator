"""
Title: Class to generate secure passphrases using diceware
Author: Primus27
Version: 1.0
"""
import secrets
import itertools


class PassphraseGen:
    """
    Create a password object
    """
    def __init__(self, n_words, n_symbols, n_numbers, append_flag, wordlist_data, word_separator):
        """
        Initialiser
        """
        self.n_words = n_words
        self.n_symbols = n_symbols
        self.n_numbers = n_numbers
        self.append_flag = append_flag
        self.wordlist_data = wordlist_data
        self.word_separator = word_separator
        self.secretGen = secrets.SystemRandom()
        self.symbol_list = ["!", "@", "#", "%", "^", "&", "*", "-", "+", "?"]
        if self.word_separator in self.symbol_list:
            self.symbol_list.remove(self.word_separator)

    def get_n_dice_roll(self, n=5):
        """
        :param n: Number of dice to roll
        :return: String containing x dice rolls concatenated
        """
        dice_concat = ""
        for _ in range(n):
            # Value between 1 and 6
            dice_concat += str(self.secretGen.randrange(1, 7))
        return dice_concat

    def get_set(self):
        """
        :return: Tuple containing randomly selected number and word from wordlist
        """
        dice_roll = self.get_n_dice_roll()
        for line in self.wordlist_data:
            if dice_roll in line:
                # Return tuple containing dice number [0] and associated word [1]
                return str(line).strip().split("\t")

    def get_symbol(self):
        """
        :return: Random symbol from list
        """
        return self.secretGen.choice(self.symbol_list)

    def get_number(self):
        """
        :return: Number between 0 and 9 (inclusive)
        """
        return str(self.secretGen.randrange(10))

    def get_pass(self):
        """
        :return: Passphrase based on user params
        """
        # Create a list containing a placeholder for each item and shuffle
        word_allowance_list = ["w"]*self.n_words
        number_allowance_list = ["n"]*self.n_numbers
        symbol_allowance_list = ["s"]*self.n_symbols
        pass_order = list(itertools.chain(word_allowance_list, number_allowance_list, symbol_allowance_list))
        self.secretGen.shuffle(pass_order)

        # Replace placeholders with randomly generated items
        passphrase = ""
        for index, placeholder in enumerate(pass_order):

            # Word
            if placeholder == "w":
                # Not first index AND append is true -> add separator
                if self.append_flag and index != 0:
                    passphrase += self.word_separator

                passphrase += self.get_set()[1]

            # Number
            elif placeholder == "n":
                passphrase += self.get_number()

            # Symbol
            elif placeholder == "s":
                # Not first index and append is true, add separator
                if self.append_flag and index != 0:
                    passphrase += self.word_separator

                passphrase += self.get_symbol()

            # Not last index AND append is false -> add separator
            if index != len(pass_order) - 1 and not self.append_flag:
                passphrase += self.word_separator

        return passphrase
