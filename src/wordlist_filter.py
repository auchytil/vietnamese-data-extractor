import utils


class WordlistFilter:
    """
    Class which filters data according to the wordlist
    """
    def __init__(self, file_name: str):
        """
        Initialization

        :param file_name: path to the file which will be used to build a wordlist
        """
        self.list = None # List of words
        self._build_wordlist(file_name)

    def _build_wordlist(self, file_name: str):
        """
        Builds a wordlist from provided file
        :param file_name: path to the file which will be used to build a wordlist
        :return: None
        """
        with open(file_name, "r") as f:
            content = utils.remove_special_chars(f.read())
            words = content.split()
            self.list = set(words)

    def check_valid(self, sentence: str):
        """
        Checks whether all of the words in the sentence are in the wordlist
        :param sentence: string data
        :return: True if the sentence is valid
        """
        words = sentence.split()
        diff = set(words).difference(self.list)
        return len(diff) == 0