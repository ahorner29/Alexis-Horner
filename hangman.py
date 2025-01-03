"""
hangman but the computer doesn't pick a secret word until it has to.
"""
# Name: Alexis Horner
# EID 1: ash4226
# Name 2: Jenna Nega
# EID 2: jn29322
import random

# Name of the dictionary file.
# Change to dictionary.txt for full version of the game.
# DICTIONARY_FILE = "smallDictionary.txt"
DICTIONARY_FILE = "dictionary.txt"

class Hangman:
    """
    Manages the details of Evil Hangman. This class keeps
    tracks of the possible words from a dictionary during
    rounds of hangman, based on guesses so far.
    """

    def __init__(self, words, debug=True):
        """
        Create a new Hangman from the provided set of words and phrases.
        :param words: A set with the words for this instance of Hangman.
        :param debug: True if we should print out debugging to terminal.
        """
        self.__difficulty = None
        self.__num_guesses = None
        self.__word_len = None
        self.__player_guesses = []
        self.__word_options = []
        self.__patterns = {}
        self.__pattern_options = []
        self.__pattern = ""
        self.__debug = debug
        self.__words = words

    def num_words(self, length):
        """
        Get the number of words in this Hangman of the given length.
        :param length: The given length to check.
        :return: the number of words in the original Dictionary
        with the given length
        """
        equal_len = 0
        for i in self.__words:
            if len(i) == length:
                equal_len += 1
        return equal_len

    def prep_for_round(self, word_len, num_guesses, diff):
        """
        Get for a new round of Hangman.
        :param word_len: the length of the word to pick this time.
        :param num_guesses: the number of wrong guesses before the
                            player loses the round.
        :param diff: The difficulty for this round.
        """
        self.__word_len = word_len
        self.__num_guesses = num_guesses
        self.__difficulty = diff.lower()
        self.__player_guesses = []

        self.__word_options = []
        for i in self.__words:
            if len(i) == self.__word_len:
                self.__word_options.append(i)

        self.__pattern = ""
        for i in range(self.__word_len):
            self.__pattern += "-"

    def num_words_current(self):
        """
        The number of words still possible (active) based on the guesses so far.
        :return: the number of words that are still possibilities based on the
        original dictionary and the guesses so far.
        """
        return len(self.__word_options)

    def get_guesses_left(self):
        """
        Get the number of wrong guesses the user has left in
        this round (game) of Hangman.
        :return: the number of wrong guesses the user has left
                in this round (game) of Hangman.
        """
        correct = []
        for char in self.__pattern:
            if char != "-" and char not in correct:
                correct.append(char)
        difference = len(self.__player_guesses) - len(correct)
        return self.__num_guesses - difference


    def get_guesses_made(self):
        """
        Return a string that contains the letters the user has guessed so far during this round.
        The characters in the string are in alphabetical order.
        The string is in the form [let1, let2, let3, ... letN].
        For example, if the user has guessed 'a', 'c', 'e', 's', 't', and 'z', 
        the string would be '[a, c, e, s, t, z]'.
        
        :return: A string that contains the letters the user has guessed so far during this round.
        """
        return self.sort(self.__player_guesses)

    def already_guessed(self, guess):
        """
        Check the status of a character.
        :param guess: The character to check.
        :return: true if guess has been used or guessed this round of Hangman,
                 false otherwise.
        """
        return guess in self.__player_guesses

    def get_pattern(self):
        """
        Get the current pattern. The pattern contains '-''s for
        unrevealed (or guessed) characters and the actual character
        for "correctly guessed" characters.
        :return: the current pattern.
        """
        return self.__pattern

    def make_guess(self, guess):
        """
        Update the game status (pattern, wrong guesses, word list),
        based on the given guess.
        :param guess: the current guessed character
        :return: a dict with the resulting patterns and the number of
        words in each of the new patterns.
        The return value is for testing and debugging purposes.
        """
        if self.__debug:
            self.debugging(guess)
        self.__player_guesses.append(guess)

        self.__pattern_options = []
        for i in self.__word_options:
            if self.make_dash_pattern(i, guess) not in self.__pattern_options:
                self.__pattern_options.append(self.make_dash_pattern(i, guess))
        self.__patterns = self.get_map_pattern(guess)

        return_patterns = self.order_entries(self.__patterns)
        self.__pattern = return_patterns[self.get_difficulty(return_patterns)][2]
        self.__word_options = return_patterns[self.get_difficulty(return_patterns)][3]

        test_return = {}
        for pattern, word_list in self.__patterns.items():
            test_return[pattern] = len(word_list)
        return test_return

    def get_map_pattern(self, guess):
        """
        Precondition: guess has not been guessed before in this round.
        Postcondition: Returns a dictionary that maps patterns to a list of words that 
                       follow said pattern.
        
        :param guess: The current guessed character.
        :return: A dictionary that maps patterns to a list of words that follow said pattern.
        """
        patterndict = {}
        for pattern in self.__pattern_options:
            patterndict[pattern] = []
            for i in self.__word_options:
                if self.make_dash_pattern(i, guess) == pattern:
                    patterndict[pattern].append(i)
        return patterndict

    def make_dash_pattern(self, word, guess):
        """
        Precondition: guess has not been guessed before in this round, word is not None.
        Postcondition: Builds possible word patterns for each word based on the user's guess and 
                       the previous pattern.
        
        :param word: The word to build the pattern for.
        :param guess: The current guessed character.
        :return: The dash pattern for the given word based on the user's guess and the previous 
                 dash pattern.
        """
        secretchrs = set()
        secretchrs.add(guess)
        for letter in self.__pattern:
            if letter != "-":
                secretchrs.add(letter)

        return_pattern = ""
        for letter in word:
            if letter in secretchrs:
                return_pattern += letter
            else:
                return_pattern += "-"
        return return_pattern

    def sort(self, entries):
        '''
        Return sorted data. When called by order_entries, entries will be tuples sorted 
        by the number of words in the word list, then the number of dashes in the pattern, 
        then the pattern, and finally the word list itself. 
        Otherwise, entries will be any sortable list. 
        You must make sure that your merge_sort method is generalized with the ability 
        to also sort lists. You must implement merge sort.

        Precondition: entries must be a list of tuples 
        (-size word list, -dash count, pattern, word list) OR any sortable list
        Postcondition: return sorted list of entries. If tuple, first sort by number of 
        words in word list, then the dash amount in the pattern, next the lexicographic 
        ordering for the pattern, and finally the word list itself
        :param entries: The Family tuples to sort or any sortable list.
        :returns: a new sorted list.
        '''
        if len(entries) <= 1:
            return entries
        mid = len(entries) // 2

        entries1 = entries[:mid]
        entries2 = entries[mid:]

        entries1 = self.sort(entries1)
        entries2 = self.sort(entries2)

        result = []
        i = 0
        j = 0

        while i < len(entries1) and j < len(entries2):
            for x in range(3):
                if entries1[i][x] < entries2[j][x]:
                    result.append(entries1[i])
                    i += 1
                    break
                if entries1[i][x] > entries2[j][x]:
                    result.append(entries2[j])
                    j += 1
                    break
        for y in range(i, len(entries1)):
            result.append(entries1[y])
        for y in range(j, len(entries2)):
            result.append(entries2[y])
        return result

    def order_entries(self, word_family):
        """
        
        Precondition: word_family is not None.
        Postcondition: For each key-value pair of (pattern, word list) in word_family, a Family 
        tuple (-size word list, -dash count, pattern, word list) is created and added to a list. 
        The entry list is then sorted based on the size of each word list, the number
        of characters revealed in the pattern, and the lexicographical ordering of the patterns.
        
        :param word_family: A dictionary containing patterns as keys and lists of words as values.
        :return: A sorted list of Entry tuples (-size word list, -dash count, pattern, word list).
        """
        tuples_list = []
        for pattern in word_family:
            wordlistlen = -1 * len(word_family[pattern])
            dashes = 0
            for letter in pattern:
                if letter == "-":
                    dashes -= 1
            tuples_list.append((wordlistlen, dashes, pattern, word_family[pattern]))
        tuples_list = self.sort(tuples_list)
        return tuples_list


    def get_diff(self, entries):
        """
        Precondition: entries is not None.
        Postcondition: Returns an integer that describes the state of the selection process 
        of word list based on a player's turn and game difficulty.
        Returns a 2 if the AI CAN pick the 2nd hardest word list. For easy mode, it's
        every other valid guess. For medium, it's every 4th valid guess.
        Returns 1 if the AI SHOULD pick the 2nd hardest word list on easy/medium mode,
        but entries.size() <= 1, so it picks the hardest.
        Returns 0 if the AI is picking the hardest list.
        
        :param entries: A list of tuples () representing patterns and associated word lists.
        :return: An integer representing the state of the selection process.
        """
        if entries is None:
            raise ValueError("Entries can't be None")
        medium_guess = 4
        easy_mode = "easy"
        medium_mode = "medium"
        if ((self.__difficulty == medium_mode and len(self.__player_guesses) % medium_guess == 0) or
            (self.__difficulty == easy_mode and len(self.__player_guesses) % 2 == 0)):
            if len(entries) > 1:
                return 2
            return 1
        return 0

    def get_difficulty(self, entries):
        """
        Precondition: entries is not None.
        Postcondition: Returns the index of the Entry tuple from the list that the AI 
        will choose for its word list/family depending on the state of the selection process.
        
        :param entries: A list of Entry tuples representing patterns and associated word lists.
        :return: The index of the Entry tuple that the AI will choose.
        """
        if entries is None:
            raise ValueError("Entries can't be None")
        diff = self.get_diff(entries)
        if diff == 2:
            return 1
        return 0

    def get_secret_word(self):
        """
        Return the secret word this Hangman finally ended up picking 
        for this round. You must sort your word list before picking a 
        secret word. If there are multiple possible words left, one is 
        selected at random. The seed should be initialized to 0 before picking.

        :return: return the secret word the manager picked.
        """
        random.seed(0)
        return random.choice(self.__word_options)

    def debugging(self, entries):
        """
        Precondition: entries is not None.
        Postcondition: Prints out custom debugging messages about which word family 
        and pattern is chosen depending on difficulty and player's turn.
        """
        message = []
        diff = self.get_diff(entries)
        message.append("DEBUGGING: ")
        if diff == 2:
            message.append("Difficulty second hardest pattern and list.\n\n")
        elif diff == 1:
            message.append("Should pick second hardest pattern this turn, "
                    + "but only one pattern available.\n")
            message.append("\nDEBUGGING: Picking hardest list.\n")
        else:
            message.append("Picking hardest list.\n")

        message.append("DEBUGGING: New pattern is: ")
        message.append(self.get_pattern())
        message.append(". New family has ")
        message.append(str(self.num_words_current()))
        message.append(" words.")
        print(''.join(message))
