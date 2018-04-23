from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlencode

def read_text():
    quotes = open("C:\\Users\\Windows\\Desktop\\Udacity_web_Developer\\movies_quotes.txt")
    contents = quotes.read()
    print(contents)
    quotes.close()
    check_profanity()

def check_profanity():
    url = "http://www.wdylike.appspot.com/?q="
    valor = urlencode("Shit")
    valor = valor.encode('utf-8')
    connection = Request(url,valor)
    html = urlopen(connection)
    the_page = html.read()
    print(the_page)


read_text()

