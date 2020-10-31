#!/bin/env python3

import re

class blockquote(str):
    def __init__(self, source):
        self.source = source

        def blockquote_tokenizer(source):
            blockquote_tokenizer_regex = r"^>+ .*(?:\n|\Z)?(?:[^>].+(?:\n|\Z))*"

            blockquote_tokenizer_result = list()

            blockquote_tokenizer_finditer = re.finditer(blockquote_tokenizer_regex, source,
                                                        re.IGNORECASE | re.MULTILINE)

            for token in blockquote_tokenizer_finditer:
                blockquote_tokenizer_result.append(token.group())

            return blockquote_tokenizer_result

        self.blockquote_tokens = blockquote_tokenizer(self.source)

class blockquote_item(str):
    blockquote_item_regex = r"^(>+) (.*)$"

    def __init__(self, blockquote_item):
        self.blockquote_item = blockquote_item
        blockquote_item_search = re.search(self.blockquote_item_regex, self.blockquote_item,
                                           re.IGNORECASE | re.MULTILINE)
        blockquote_item_level = blockquote_item_search.group(1)
        self.level = len(blockquote_item_level)
        self.content = blockquote_item_search.group(2)

def assembler(blockquote: blockquote) -> str:
    ided_tokens = []

    for token in blockquote.blockquote_tokens:
        ided_tokens.append(blockquote_item(token))

    begin_quote = "\\begin{displayquote}"
    end_quote = "\\end{displayquote}"

    for ided_token in ided_tokens:
        if ided_tokens.index(ided_token) < 1:
            prev_ided_token = None
            next_ided_token = ided_tokens[ided_tokens.index(ided_token) + 1]
        elif ided_tokens.index(ided_token) == ided_tokens.index(ided_tokens[-1]):
            prev_ided_token = ided_tokens[ided_tokens.index(ided_token) - 1]
            next_ided_token = None
        else:
            prev_ided_token = ided_tokens[ided_tokens.index(ided_token) - 1]
            next_ided_token = ided_tokens[ided_tokens.index(ided_token) + 1]

        begin_tabs = "\t" * (ided_token.level - 1)

        if prev_ided_token == None:
            print(begin_tabs + begin_quote)
        elif prev_ided_token.level > ided_token.level:
            pass
        elif prev_ided_token.level < ided_token.level:
            print(begin_tabs + begin_quote)
        else:
            pass

        print(begin_tabs + ided_token.content)


        if next_ided_token == None:
            level_difference  = 0
            while level_difference < ided_token.level:
                end_tabs = "\t" * (ided_token.level - 1 - level_difference)
                print(end_tabs + end_quote) 
                level_difference += 1
            # print(tabs + end_quote)
        elif next_ided_token.level < ided_token.level:
            level_difference = 0 
            while level_difference < ided_token.level - next_ided_token.level:
                end_tabs = "\t" * (ided_token.level - 1 - level_difference)
                print(end_tabs + end_quote) 
                level_difference += 1
       # print((tabs + end_quote + "\n") * (ided_token.level - next_ided_token.level))
        elif next_ided_token.level > ided_token.level:
            pass
        else:
            pass


if __name__ == "__main__":
    source = "> Hello\n>> World."
    x = blockquote(source)
    assembler(x)
