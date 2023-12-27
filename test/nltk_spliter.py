# This is a long document we can split up.
with open("./testfile/state_of_the_union.txt") as f:
    state_of_the_union = f.read()

from langchain.text_splitter import NLTKTextSplitter

text_splitter = NLTKTextSplitter(chunk_size=1000) # How the chunk size is measured: by number of characters.

texts = text_splitter.split_text(state_of_the_union)
print(texts[0])