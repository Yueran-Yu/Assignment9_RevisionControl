# Use a web browser to visit:
# https://www.colorhexa.com/color-names
# Use the HTMLParser code from the class example to visit the site and look at all the tags.
# With your knowledge of the HTMLParse and urllib modules, write code to extract the color names and hex values from the website.
# Store the extracted values in a dictionary named “colors”, where the color name is the key and the hex code is the value.
# Print out the dictionary so you get the following output:
# Alice blue #f0f8ff
# Almond #efdecd
# Amber #ffbf00
# Android Green #a4c639
# Anti-flash white #f2f3f4
# Antique brass #cd9575
# Antique white #faebd7
# Apple green #8db600
# Apricot #fbceb1
# Aqua #00ffff
# Aquamarine #7fffd4
#
# You can leave out any HTMLParser methods you don’t use, for easier to read code.
# Work with a partner to accomplish the task.

from html.parser import HTMLParser
import urllib.request
import string


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.colors = []

    def handle_starttag(self, tag, attrs):
        pass
        # print("Start tag:", tag)
        # for attr in attrs:
        #     print(" attr:", attr)

    def handle_data(self, data):
        if data[0].isalpha() or data.startswith('#'):
            self.colors.append(data)


myparser1 = MyHTMLParser()
with urllib.request.urlopen('https://www.colorhexa.com/color-names') as response:
    html = str(response.read())

myparser1.feed(html)


def color_dict():
    color_dic = {}
    items = myparser1.colors
    for index, item in enumerate(items):
        if 17 <= index <= 1508 and index % 2 != 0:
            color_dic[items[index]] = items[index+1]
            # print(str(index) + " === " + items[index ])
    return color_dic


dc = color_dict()
print(len(dc))
for k, v in dc.items():
    print("{0:20} {1}".format(k, v))



