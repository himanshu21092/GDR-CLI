"""
Usage:
    main.py [--help | -h]
    main.py list [-a]
    main.py (--path=<path>)...
    main.py <file> <file>

Options:
    -h --help   Show this screen.
    -a          Show all files.
"""
from docopt import docopt
from Commands.list import List

if __name__ == '__main__':
    arguments = docopt(__doc__)
    print(arguments)

    # if arguments['list']:
    #     List.listAll()