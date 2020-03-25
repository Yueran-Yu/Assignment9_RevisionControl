from html.parser import HTMLParser
import urllib.request


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        pass
        # print("Found a start tag:", tag)

    def handle_endtag(self, tag):
        pass
        # print("Found end tag:", tag)

    def handle_data(self, data):
        print(data[20:34])


myparser = MyHTMLParser()
with urllib.request.urlopen('http://checkip.dyndns.org/') as response:
    html = str(response.read())
myparser.feed(html)

