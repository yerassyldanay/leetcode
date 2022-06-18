import hashlib
import base64

url_dict = {}

class Codec:
    def encode(self, longUrl: str):
        enUrl = hashlib.md5(longUrl.encode()).hexdigest()
        url_dict[enUrl[:7]] = longUrl[len("https://leetcode.com/"):]
        return "http://tinyurl.com/" + enUrl[:7]

    def decode(self, shortUrl: str):
        shortUrl = url_dict[ shortUrl[len("http://tinyurl.com/"):] ]
        return "https://leetcode.com/" + shortUrl

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

c = Codec()
a = c.encode("https://leetcode.com/problems/design-tinyurl")
print(a)
print(c.decode(a))
#
# enUrl = hashlib.md5('longUrl'.encode())
# print(enUrl.hexdigest())
# print(type(enUrl.hexdigest()))