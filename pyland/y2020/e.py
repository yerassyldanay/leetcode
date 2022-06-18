
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

    def search_string(self, string: str):
        node = self.root
        for character in string:
            if character not in node.children:
                return False

            node = node.children[character]

        return len(node.children) == 0

    def add_value_to_node(self, character: chr, node: TrieNode) -> TrieNode:
        if character not in node.children:
            node.children[character] = TrieNode(character)

        return node.children[character]

    def get_all_node_combinations(self, node: TrieNode) -> list:
        if len(node.children) == 0:
            return [node.value]

        result = []
        for child in node.children.values():
            for suff in self.get_all_node_combinations(child):
                result.append(node.value + suff)

        return result

    def get_string_by_pattern(self, index: int, pattern: str, node: TrieNode) -> set:
        if index >= len(pattern):
            return set()

        result = set()
        character = pattern[index]

        if character == "-":
            for child in node.children.values():
                for each in self.get_string_by_pattern(index + 1, pattern, child):
                    result.add(each)
        else:
            if node.value != character:
                return set()

            result = self.get_all_node_combinations(node)

        return result

    def generate_trie(self, old_string: str, prefixes: list, suffixes: list):

        self.efficiently_add_string(0, old_string, self.root)

        if prefixes:
            self.add_prefixes(old_string, prefixes, suffixes)

        self.add_suffixes(suffixes)

    def add_suffixes(self, suffixes: list):
        for suffix, _ in suffixes:
            self.efficiently_add_string(0, suffix, self.root)

    def add_prefixes(self, old_string: str, prefixes: list, suffixes: list):
        maxp = max([x[1] for x in prefixes])

        dp = dict()
        dp[0] = ['']

        for pindex in range(1, maxp + 1):

            result = set()
            for suffix, _ in suffixes:
                suffix_character = suffix[pindex * (-1)]
                if suffix_character == "-":
                    continue

                result.add(suffix[(-1) * pindex:])

                # print("suffix_character: ", suffix_character, suffix, pindex)

            for prefix, _ in prefixes:

                if pindex > 1 and (prefix[(-1) * pindex] == "-" or prefix[(-1) * pindex + 1] != "-"):
                    continue

                prefix_character = prefix[pindex * (-1)]

                if prefix_character == "-":
                    continue

                for dp_suffix in dp[pindex - 1]:
                    result.add(prefix_character + dp_suffix)

            dp[pindex] = result

        # for key, value in dp.items():
        #     print(key, sorted(value))

        self.efficiently_add_string(0, old_string, self.root)

        for prefix, counter in prefixes:
            for dp_suffix in dp[counter]:
                word = prefix[:-counter] + dp_suffix
                self.efficiently_add_string(0, word, self.root)

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
    old_word = ""

    while len(old_word) < length:
        old_word += std.readline().strip()

    #print(old_word)

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
            suffixes.append( (line, sum( [1 for character in line if character == "-"] )) )
        elif line[-1] == "-":
            prefixes.append((line, sum([1 for character in line if character == "-"])))

    suffixes.append((old_word, 0))

    # sort
    suffixes = sorted(suffixes, key=lambda x: x[1])
    prefixes = sorted(prefixes, key=lambda x: x[1])

    # new words
    num_new_words = int(std.readline().strip())
    new_words = []
    for _ in range(num_new_words):
        line = std.readline().strip()
        new_words.append(line)

    # print(old_word, new_words, prefixes, suffixes)

    # # logic
    t = Trie()
    t.generate_trie(old_word, prefixes, suffixes)

    for each in new_words:
        if t.search_string(each):
            print("YES", each)
        else:
            print("NO ", each)

    std.close()
