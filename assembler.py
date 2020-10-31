#!/bin/env python3
#-*- coding: utf-8 -*-

import re

# better-pandoc modules
import header
import blockquote


test_string = """# Lorem ipsum dolor

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.
At vero eos et accusam et justo duo dolores et ea rebum. 
Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.
At vero eos et accusam et justo duo dolores et ea rebum.
Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.

> Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.
>> At vero eos et accusam et justo duo dolores et ea rebum. 
Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
>>> Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.
>> Lore ipsum dolor sit amet, consetetur sadipscig
> At vero eos et accusam et justo duo dolores et ea rebum.
Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.

# Section Heading

Here is a paragraph."""

def id_header(arbitrary_tokens: list) -> list:
    """Identifies an arbitrary token as a header if it matches."""
    
    header_regex = r"^#{1,6} .*$"
    
    id_header_result = list()

    for token in arbitrary_tokens:
        header_match = re.search(header_regex, token,
                                  re.IGNORECASE | re.MULTILINE)
        if header_match:
            id_header_result.append(header.token(token))
        else:
            id_header_result.append(token)

    return id_header_result

def id_blockquote(arbitrary_tokens: list) -> list:
    """Identifies an arbitrary token as a blockquote if it matches."""

    blockquote_regex = r"^>+ (?:.+$(\n|\Z))+"

    id_blockquote_result = list()

    for token in arbitrary_tokens:
        blockquote_match = re.search(blockquote_regex, token,
                                     re.IGNORECASE | re.MULTILINE)
        if blockquote_match:
            id_blockquote_result.append(blockquote.blockquote(token))
        else:
            id_blockquote_result.append(token)

    return id_blockquote_result

def arbitrary_tokenizer(source: str) -> list:
    """Tokenizes a markdown file

    First the file gets tokenized into arbitrary tokens at empty lines.
    The arbitrary tokens then get identified.
    """

    # Arbitrary tokenizer
    arbitrary_token_regex = r"^.+$(?:\n.+)*"

    arbitrary_tokeninzer_finditer = re.finditer(arbitrary_token_regex, source,
                                                re.IGNORECASE | re.MULTILINE)

    arbitrary_tokenizer_result = list()

    for token in arbitrary_tokeninzer_finditer:
        arbitrary_tokenizer_result.append(token.group())

    return arbitrary_tokenizer_result

def id_tokens(arbitrary_tokens: list) -> list:
    # Identify arbitrary tokens
    ided_tokens_result = id_header(arbitrary_tokens)
    ided_tokens_result = id_blockquote(ided_tokens_result)

    return ided_tokens_result

def final_assembler(tokenized_source: list) -> str:
    """Combines all assmblers to assembel a latex file"""

    for token in tokenized_source:
        if type(token) == header.token:
            header.assembler(token)
        elif type(token) == blockquote.blockquote:
            blockquote.assembler(token)
        else:
            print(token + "\n")

if __name__ == "__main__":
    x = arbitrary_tokenizer(test_string)
    y = id_tokens(x)
    final_assembler(y)
