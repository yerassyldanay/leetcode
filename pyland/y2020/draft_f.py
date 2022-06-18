
if __name__ == "__main__":
    old = "cccc"
    prefixes = [("aaa-", 1), ("bb--", 2), ("d---", 3)]
    suffixes = [("cccc", 0), ("-ggg", 1), ("--ff", 2), ("---e", 3) ]
    maxp = 3

    dp = dict()
    dp[0] = ['']

    for pindex in range(1, maxp + 1):

        result = set()
        for suffix, _ in suffixes:
            suffix_character = suffix[pindex * (-1)]
            if suffix_character == "-":
                continue

            result.add(suffix[(-1) * pindex:])

            print("suffix_character: ", suffix_character, suffix, pindex)

        for prefix, _ in prefixes:

            if pindex > 1 and (prefix[(-1) * pindex] == "-" or prefix[(-1) * pindex + 1] != "-"):
                continue

            prefix_character = prefix[pindex * (-1)]

            if prefix_character == "-":
                continue

            for dp_suffix in dp[pindex - 1]:
                result.add( prefix_character + dp_suffix )

        dp[pindex] = result

    for key, value in dp.items():
        print(key, sorted(value))

    print("--------------------------------")
    for prefix, counter in prefixes:
        for dp_suffix in dp[counter]:
            print(prefix[:-counter] + dp_suffix)

