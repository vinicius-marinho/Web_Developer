from urllib.request import urlopen
from urllib.parse import urlencode


def read_text():
    quotes = open("C:\\Users\\Windows\\Desktop\\Udacity_web_Developer\\movies_quotes.txt")
    contents = quotes.read()
    quotes.close()
    check_profanity(contents)

def check_profanity(texto):
    params = urlencode({'q': texto})
    url = urlopen("http://www.wdylike.appspot.com/?" + params)
    output = url.read()
    if output:
        print("Melhor consertar esse texto ai")
    else:
        print("Pode mandar o e-mail")

read_text()

