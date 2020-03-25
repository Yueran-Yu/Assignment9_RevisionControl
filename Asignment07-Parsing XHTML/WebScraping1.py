from html.parser import HTMLParser
import urllib.request


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.colors = []
        self.is_tbody = False
        self.is_a = False
        self.is_class = False
        self.is_href = False
        self.is_td = False

    def handle_starttag(self, tag, attrs):
        if tag == 'tbody':
            self.is_tbody = True
        if tag == 'a':
            self.is_a = True
        if tag == 'td':
            self.is_td = True

        for attr in attrs:
            if attr[0] == 'class':
                self.is_class = True

            if attr[0] == 'href':
                self.is_href = True

    def handle_endtag(self, tag):
        if tag == 'tbody':
            self.is_tbody = False
        if tag == 'a':
            self.is_a = False
        if tag == 'td':
            self.is_td = False

    def handle_data(self, data):
        if self.is_tbody and self.is_td and self.is_a and self.is_class and self.is_href:
            self.colors.append(data)


myparser = MyHTMLParser()
with urllib.request.urlopen('https://www.colorhexa.com/color-names') as response:
    html = str(response.read())

myparser.feed(html)


def color_dict():
    color_dic = {}
    items = myparser.colors
    for index, item in enumerate(items):
        if index % 2 != 0:
            color_dic[items[index-1]] = item
    return color_dic


dc = color_dict()
print(len(dc))
for k, v in dc.items():
    print("{0:30} {1}".format(k, v))
