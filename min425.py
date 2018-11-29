#!/usr/bin/python3

"""
List of countries from Example web scraping website.
"""
import html
from urllib.request import urlopen, Request

EXAMPLE_URL = "http://example.webscraping.com/"

# getting page from server
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64;)'}
example_request = Request(EXAMPLE_URL, headers=headers)
example_page = urlopen(example_request).read()
example_page = example_page.decode('utf-8')

for number in range(1, 11):
    number = str(number)
    EXAMPLE_TAG = '-' + number + '">'
    example_tag_size = len(EXAMPLE_TAG)
    example_tag_index = example_page.find(EXAMPLE_TAG)
    example_value_start = example_tag_index - 1
    example_rev = ''
    for char in range(example_value_start, 0, -1):
        if example_page[char] != '/':
            example_rev += example_page[char]
        else:
            break
    example_new = example_rev[::-1]

    for char in '-':
        example_new = example_new.replace(char, ' ')

    print(f'{example_new}\n')