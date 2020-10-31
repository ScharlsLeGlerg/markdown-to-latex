#!/bin/env python3
#-*- coding: utf-8 -*-

import re

class token(str):
    regex = r"^(#{1,6}) (.*)$"

    def __init__(self, arbitrary_token):
        self.arbitrary_token = arbitrary_token
        search = re.search(self.regex, self.arbitrary_token,
                           re.IGNORECASE | re.MULTILINE)
        level_match = search.group(1)
        self.level = len(level_match)
        self.content = search.group(2)

def assembler(header_token: token) -> str:
    sub_count = "sub" * (header_token.level - 1)
    section = f"\\{sub_count}section{{{header_token.content}}}\n"
    print(section)
