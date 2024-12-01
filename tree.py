from argparse import ArgumentParser, ArgumentTypeError
from pathlib import Path
from utils import initialize, process_tree


def level(raw_val):
    lvl = int(raw_val)
    if lvl < 1:
        raise ArgumentTypeError('Level must be greater than or equal to 1.')
    return lvl


def directory(raw_path):
    p = Path(raw_path)
    if p.is_dir():
        return raw_path
    else:
        raise ArgumentTypeError('Invalid value for directory.')


def parse_args():
    parser = ArgumentParser(prog='tree')

    parser.add_argument("dir", nargs="?", default=".", type=directory)
    parser.add_argument("-d", action='store_true', default=False)
    parser.add_argument("-L", default=None, type=level)

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    initialize(dir_name=args.dir, only_dirs=args.d, max_level=args.L)
    process_tree()
