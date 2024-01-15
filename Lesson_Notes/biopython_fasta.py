def SimpleFastaParser(handle):
    """Iterate over Fasta records as string tuples.

    Arguments:
     - handle - input stream opened in text mode

    For each record a tuple of two strings is returned, the FASTA title
    line (without the leading '>' character), and the sequence (with any
    whitespace removed). The title line is not divided up into an
    identifier (the first word) and comment or description.

    >>> with open("Fasta/dups.fasta") as handle:
    ...     for values in SimpleFastaParser(handle):
    ...         print(values)
    ...
    ('alpha', 'ACGTA')
    ('beta', 'CGTC')
    ('gamma', 'CCGCC')
    ('alpha (again - this is a duplicate entry to test the indexing code)', 'ACGTA')
    ('delta', 'CGCGC')

    """
    # Skip any text before the first record (e.g. blank lines, comments)
    for line in handle:
        if line[0] == ">":
            title = line[1:].rstrip()
            break
    else:
        # no break encountered - probably an empty file
        return

    # Main logic
    # Note, remove trailing whitespace, and any internal spaces
    # (and any embedded \r which are possible in mangled files
    # when not opened in universal read lines mode)
    lines = []
    for line in handle:
        if line[0] == ">":
            yield title, "".join(lines).replace(" ", "").replace("\r", "")
            lines = []
            title = line[1:].rstrip()
            continue
        lines.append(line.rstrip())

    yield title, "".join(lines).replace(" ", "").replace("\r", "")



### Using it 
fasta = open("/Users/lemon/Desktop/Programming/learning-python/Rosalind/GRPH_input.txt", "r")
for title, sequence in SimpleFastaParser(fasta):
    print(title, sequence)


### Testing return vs. yield
def add_numbers(a, b):
    result = a + b
    return result

def generate_numbers():
    for i in range(5):
        yield i

add_numbers(1, 2)
#for c in generate_numbers():
#    print(c)


### Testing \r
text = "Hello\rWorld!"
#print(text)
