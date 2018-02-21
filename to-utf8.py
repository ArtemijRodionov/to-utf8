#!/usr/bin/env python
import glob
import sys

import chardet


def main(pattern):
    for file in glob.glob(pattern):
        with open(file, 'rb') as f:
            data = f.read()
            encoding = chardet.detect(data)['encoding']
            decoded_data = data.decode(encoding)
        with open(file, 'bw') as f:
            f.write(decoded_data.encode('utf-8'))


if __name__ == '__main__':
    main(sys.argv[1])
