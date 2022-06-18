class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #         if s == "":
        #             return 0

        #         d = set()
        #         result, head, tail = 0, 0, 0

        #         while head < len(s) and tail < len(s):
        #             if s[head] not in d:

        #                 d.add( s[head] )
        #                 head += 1
        #                 result = max( result, head - tail + 1 )

        #             else:

        #                 d.remove( s[tail] )
        #                 tail += 1

        #         return result

        if not s:
            return 0

        d = {}
        result, head, tail = 0, 0, 0

        while head < len(s):
            print(d)
            if s[head] not in d:

                d[s[head]] = head
                result = max(result, head - tail + 1)
                head += 1

            else:
                tail = max(tail, d[s[head]] + 1)
                del d[s[head]]

        return result

s = Solution()
print(s.lengthOfLongestSubstring("abba"))
