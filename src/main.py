import argparse
import utils


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Vietnamese text extractor')
    parser.add_argument('files', metavar='FILE', type=str, nargs='+',
                        help='Files containing the data')
    args = parser.parse_args()
    
    for file_name in args.files:
        utils.filter_trash(file_name)

