#!/usr/bin/python3

"""
Weather app project.
"""
import html
from urllib.request import urlopen, Request

EXAMPLE_URL = "http://example.webscraping.com/"

# getting page from server
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64;)'}
example_request = Request(EXAMPLE_URL, headers=headers)
example_page = urlopen(example_request).read()
example_page = example_page.decode('utf-8')

EXAMPLE_TAG = '<a href="/places/default/view/'
example_tag_size = len(EXAMPLE_TAG)
example_tag_index = example_page.find(EXAMPLE_TAG)
example_value_start = example_tag_index + example_tag_size
example_ = ''
for char in example_page[example_value_start:]:
	if char != '-':
		example_ += char
	else:
		break


	

print(f'{html.unescape(example_)}\n')
print(f'{example_}\n')