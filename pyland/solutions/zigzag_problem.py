
class Solution:
    def convertToStr(self, arr: list):
        return "".join(arr)

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        inx = 0
        index = 0
        returnList = [""] * numRows
        while True:
            if index == len(s):
                return self.convertToStr(returnList)

            if inx == 0:
                iny = 0
                while iny != numRows:
                    if index == len(s):
                        return self.convertToStr(returnList)

                    returnList[iny                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      ] = returnList[iny] + s[index]
                    index = index + 1
                    iny = iny + 1

            else:
                if index == len(s):
                    return self.convertToStr(returnList)
                # print(iny)
                iny = numRows - 1 - inx
                returnList[iny] = returnList[iny] + s[index]
                index = index + 1

            # print(inx, numRows - 1)
            inx = (inx + 1) % (numRows - 1)
            # print("inx:", inx)

s = Solution()
a = s.convert("PAYPALISHIRING", 1)
print(a)
print(a == "PINALSIGYAHRPI")
