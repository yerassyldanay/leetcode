
class Solution:

	def lengthOfLongestSubstringTwoDistinct(s: str) -> str:
		if len(s) < 2:
			return ""

		first, last = 0, 0
		result, arr = '', []
		mlen = -1

		for i, letter in enumerate(s):
			if len(arr) == 0:
				arr.append(letter)
				head, tail = i, i
				continue

			if letter not in arr and len(arr) == 2:
				if mlen < head - tail:
					result = s[tail : head + 1]
					mlen = head - tail
					arr = [letter]
					head, tail = i, i

				continue

			tail = i
			if letter not in arr
