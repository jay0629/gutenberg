#!/usr/bin/python3.5

import re
import requests


def bookRunner():
    num = 10
    print('start')
    while num <= 20:
        bs = "/"
        extension = ".txt"
        url = "http://www.gutenberg.org/files/"
        file = (url + str(num) + bs + str(num) + extension)
        page = requests.get(str(file))
        #  pop = len(page.content)
        with open('movie.csv', 'a') as the_file:
            ser = re.findall(r'Title\:\s.*', page.text)
            the_file.write(str(num))
            the_file.write(", ")
            the_file.write(str(ser))
            the_file.write(", ")
            the_file.write("\n")
        num = num + 1
    print("Done")


bookRunner()
