#!/bin/env python3

import re

class token(str):
    def __init__(self, arbitrary_token):
        self.arbitrary_token = arbitrary_token

        def list_tokenizer(arbitrary_token: str) -> list:
            """Sub tokenizes a list token."""

            list_tokenizer_regex = r"^ *(?:[\+\-\*]|\d+.).*(?:\n^(?! *(?:[*+-]|\d)).*)*"

            list_tokenizer_result = list()

            list_tokenizer_finditer = re.finditer(list_tokenizer_regex, arbitrary_token,
                                                  re.IGNORECASE | re.MULTILINE)

            for token in list_tokenizer_finditer:
                list_tokenizer_result.append(token.group())

            return list_tokenizer_result

        self.tokens = list_tokenizer(self.arbitrary_token)

class item(str):
    item_regex = r"^(\s*)([*+-]|\d+).{,1} (.*\n(?:.+(?:\n|\Z))*)"

    def __init__(self, item):   
        self.item = item
        item_search = re.search(self.item_regex, self.item,
                                re.IGNORECASE | re.MULTILINE)
        self.item_level = len(item_search.group(1))
        try:
            int(item_search.group(2))
            self.is_ordered = True
        except ValueError:
            self.is_ordered = False
        self.content = (" ".join(item_search.group(3).split())).replace('. ', '.\n')

advanced_regex = r"^ *(?:(?:[\+\-\*]|\d+.) )(.*)(?:\n^(?! *(?:[*+-]|\d)) *(.*))*"

if __name__ == "__main__":
    test_str = """+ This is a list item
    + This too is a list item
    * this is as well
- List item can be broken into
multiple lines, like so.
* but also like so
  This is still in the same item
    1. They can be mixed with orderd lsits
    2. This is a ordered list
       Here iss soem stuff"""

    x = token(test_str)
    print(x.arbitrary_token)
    print(x.tokens)
