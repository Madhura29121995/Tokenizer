import gzip, re, sys

def tokenize(l):
    # A very simple whitespace-based tokenizer. You will need to
    # improve this function for your assignment. You will probably
    # need some regular expressions, so I've already imported the re
    # module for you :-)

    return l.split()

# The first argument is the filename to work with
fname = sys.argv[1]

# Use gzip.open to open a compressed file
with gzip.open(fname, mode='rt', encoding='utf-8') as infile:
    for line in infile:
        # Tokenize each sentence/line
        tokens = tokenize(line)
        # Print each token on a separate line, with a blank line between
        # sentences
        
        for t in tokens:
            word = re.split(r"(\$?[\w\-\']+|[^\s*S+\W*S]|[^\w\s]+)", t)
            for ele in word:
                if ele.strip():
                    print(ele.encode('ascii', 'ignore').decode('utf-8'))
            print()