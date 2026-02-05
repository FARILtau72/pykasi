import sys
import argparse
from . import run_file, run_text

def main(argv=None):
    parser = argparse.ArgumentParser(prog='pykasi')
    parser.add_argument('file', nargs='?', help='PyKasi script to run (.bks)')
    parser.add_argument('-e', '--eval', help='Run a snippet of PyKasi code')
    args = parser.parse_args(argv)
    try:
        if args.eval:
            run_text(args.eval)
        elif args.file:
            run_file(args.file)
        else:
            parser.print_help()
    except Exception as exc:
        print(exc)
        sys.exit(1)

if __name__ == '__main__':
    main()
