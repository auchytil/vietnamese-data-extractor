import argparse
import utils
from wordlist_filter import WordlistFilter

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Vietnamese text extractor')
    parser.add_argument('files', metavar='FILE', type=str, nargs='+',
                        help='Files containing the data')
    parser.add_argument('--wordlist', metavar='PATH', type=str, help='File which will be used to create wordlist')
    args = parser.parse_args()

    output_list = []
    for file_name in args.files:
        output_list.append(utils.filter_trash(file_name))

    if args.wordlist:
        filter = WordlistFilter(args.wordlist)
        for file in output_list:
            for sentence in file:
                if filter.check_valid(sentence):
                    print(sentence)
    else:
        print(output_list)