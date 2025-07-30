from argparse import ArgumentParser, _SubParsersAction

import yamlpack.cli.actions as parser_actions

def make_init_subparser(subparser_factory: _SubParsersAction) -> None:
    init_parser: ArgumentParser = subparser_factory.add_parser("init")
    init_parser.set_defaults(func=parser_actions.init_action)

def make_parser():
    subparsers = [make_init_subparser, ]
    parser = ArgumentParser()
    subparser_factory = parser.add_subparsers()

    for make_subparser in subparsers:
        make_subparser(subparser_factory)

    