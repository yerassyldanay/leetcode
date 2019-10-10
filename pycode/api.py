from flask import Flask
from flask import request as r
import re

application = Flask(__name__)

@application.route("/str/")
def manupulate_over_string():
    string = r.args.get("man")
    string = re.sub("[ ]+", "_", string).lower()
    print(string)
    return string

if __name__ == '__main__':
    application.run(port = "6600")
