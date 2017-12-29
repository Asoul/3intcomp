import sys
import os.path
import argparse
import random

MAX_SIZE = sys.maxsize

def kmp(pattern):
    ret = [0]
    for i in range(1, len(pattern)):
        j = ret[i - 1]
        while j > 0 and pattern[j] != pattern[i]:
            j = ret[j - 1]
        ret.append(j + 1 if pattern[j] == pattern[i] else j)
    return ret

def find(target):
    partial = kmp(target)
    for seed in range(MAX_SIZE):
        random.seed(seed)
        j = 0
        for i in range(MAX_SIZE):
            c = random.randint(0, 255)
            while j > 0 and c != target[j]:
                j = partial[j - 1]

            if c == target[j]:
                j += 1

            if j == len(target):
                return (seed, i - (j - 1))

    return (None, None)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='3 Int Compressor encode demo')
    parser.add_argument('path', metavar='FILE_PATH', type=str,
                        help='file path for encode')

    args = parser.parse_args()
    if not os.path.isfile(args.path):
        print('Wrong file path', file=sys.stderr)
        sys.exit(1)

    with open(args.path, 'rb') as f:
        target = bytearray(f.read())
        result = find(target)
        if not result:
            print('Sorry, not found')
        else:
            print('Found, seed = {seed}, start = {start}, length = {length}'.format(
                seed=result[0],
                start=result[1],
                length=len(target)
            ))
