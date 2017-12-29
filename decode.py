import argparse
import random
import sys

def decode(seed, start, offset):
    random.seed(seed)
    for _ in range(start):
        random.randint(0, 255)

    result = b''
    for _ in range(offset):
        c = random.randint(0, 255)
        result += bytes([c])

    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='3 Int Compressor decode demo')
    parser.add_argument('seed', metavar='SEED', type=int,
                        help='seed calculate by the encoder')
    parser.add_argument('start', metavar='START', type=int,
                        help='start value calculate by the encoder')
    parser.add_argument('offset', metavar='OFFSET', type=int,
                        help='offset value calculate by the encoder')

    args = parser.parse_args()
    result = decode(args.seed, args.start, args.offset)
    print(result)
