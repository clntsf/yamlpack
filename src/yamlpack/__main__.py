from yamlpack.make_pack import make_pack
from sys import argv

from yamlpack.cli.parser import make_parser

def main():
    parser = make_parser()
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()