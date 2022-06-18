
class TrieNode:
    def __init__(self, value):
        self.value = value
        self.children = dict()

    def __repr__(self):
        a = "trie: " + str(self.value) + " | children(" + str(self.value) + "): "
        children = []
        for child in self.children:
            children.append(str(self.children[child]))
        return a


class Trie:
    def __init__(self):
        self.root = TrieNode(None)

    def add_string(self, string: str):
        node = self.root
        for character in string:
            if character not in node.children:
                node.children[character] = TrieNode(character)

            node = node.children[character]

    def search_string(self, string: str):
        node = self.root
        for character in string:
            if character not in node.children:
                return False

            node = node.children[character]

        return True

    def add_value_to_node(self, character: chr, node: TrieNode) -> TrieNode:
        if character not in node.children:
            node.children[character] = TrieNode(character)

        return node.children[character]

    def add_prefixes_and_suffixes(self, old_string: str, prefixes: list, suffixes: list):
        # this builds a skeleton
        self.add_string(old_string)

        # add prefixes
        node = self.root
        for prefix in prefixes:
            self.__add_prefix(0, prefix, node, old_string, suffixes)

        # add suffixes
        node = self.root
        for suffix in suffixes:
            self.__add_suffix(0, suffix, node)

    def __add_prefix(self, index: int, prefix: str, node: TrieNode, old_string: str, suffixes: list):
        if index >= len(prefix):
            return

        character = prefix[index]

        # create a branch with characters of old_string and every suffix at this index
        if character == "-":

            # suffixes become [], as it cannot be mixed at the end
            character = old_string[index]
            self.add_value_to_node( character, node )
            self.__add_prefix(index + 1, prefix, node.children[character], old_string, [])

            # create branch with characters of suffixes
            for suffix in suffixes:
                character = suffix[index]
                self.add_value_to_node(character, node)
                self.__add_prefix(index + 1, prefix, node.children[character], "", [suffix])

            return

        # create a branch if it does not exist
        if character not in node.children:
            node.children[ character ] = TrieNode(character)

        node = node.children[ character ]

        # further addition
        self.__add_prefix(index + 1, prefix, node, old_string, suffixes)

    def __add_suffix(self, index: int, prefix: str, node: TrieNode):
        if index >= len(prefix):
            return

        character = prefix[index]

        if character == "-":
            for child in node.children.values():
                self.__add_suffix(index + 1, prefix, child)
        else:
            self.add_value_to_node( character, node)
            self.__add_suffix( index + 1, prefix, node.children[ character ] )


    def generate_trie(self, old_string: str, prefixes: list, suffixes: list):
        node = self.root

        # add prefixes (trie stops where prefix has '-')
        skips = set()
        for prefix in prefixes:
            count = 0
            # count
            for character in prefix:
                if character == "-":
                    count += 1
            skips.add(count)

            # add
            self.efficiently_add_string(0, prefix, node)

        # finish prefixes (in place of '-' we can put old_string characters)
        for skip in skips:
            for word in suffixes + [old_string]:
                point = (len(word) - skip)
                new_string = "-" * point + word[point:]
                self.efficiently_add_string(0, new_string, node)

        # add old string
        self.efficiently_add_string(0, old_string, node)

        # add suffixes
        for suffix in suffixes:
            self.efficiently_add_string(0, suffix, node)

        # print()

    def efficiently_add_string(self, index: int, string: str, node: TrieNode):
        if index >= len(string):
            return

        if string[index] == "-":
            for child in node.children.values():
                self.efficiently_add_string(index + 1, string, child)
        else:
            character = string[index]
            self.add_value_to_node(character, node)
            self.efficiently_add_string(index + 1, string, node.children[character])


# t = Trie()
# t.generate_trie("ccc", ["ab-"], ["-ab"])
# print(t.search_string("abb"))

if __name__ == "__main__":
    std = open("e.txt", "r")

    line = std.readline().strip().split()
    length = int(line[0])
    num_presuf = int(line[1])

    # old word
    old_word = std.readline().strip()

    # prefixes and suffixes
    prefixes = []
    suffixes = []

    for _ in range(num_presuf):
        line = std.readline().strip()
        if len(line) <= 1:
            continue
        elif line[0] == line[-1]:
            continue

        if line[0] == "-":
            suffixes.append(line)
        elif line[-1] == "-":
            prefixes.append(line)

    # new words
    num_new_words = int(std.readline().strip())
    new_words = []
    for _ in range(num_new_words):
        line = std.readline().strip()
        new_words.append(line)

    # print(old_word, new_words, prefixes, suffixes)

    # logic
    t = Trie()
    t.add_prefixes_and_suffixes(old_word, prefixes, suffixes)

    for each in new_words:
        print(t.search_string(each))

    std.close()
