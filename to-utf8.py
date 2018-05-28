#!/usr/bin/env python
import glob
import sys

import chardet


def main(pattern):
    for file in glob.glob(pattern):
        with open(file, 'r+') as f:
            data = f.read()
            encoding = chardet.detect(data)['encoding']
            decoded_data = data.decode(encoding).encode('utf-8')
            f.seek(len(data))
            f.truncate(0)
            f.write(decoded_data)

if __name__ == '__main__':
    main(sys.argv[1])
