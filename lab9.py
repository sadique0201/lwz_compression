# -*- coding: utf-8 -*-
import sys
message="Cows graze in groves on grass which grows in grooves in groves"

if (len(sys.argv)>1):
        message=str(sys.argv[1])


def compress(uncompressed):
    """Compress a string to a list of output symbols."""

    # Build the dictionary.
    dict_size = 256
    dictionary = dict((chr(i), chr(i)) for i in range(dict_size))
    # in Python 3: dictionary = {chr(i): chr(i) for i in range(dict_size)}
    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c

    # Output the code for w.
    if w:
        result.append(dictionary[w])

    return result

print("Input: ",message)
compressed = compress(message)
print("\nCompressed:\n",compressed)

