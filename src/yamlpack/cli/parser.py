from argparse import ArgumentParser, _SubParsersAction

import yamlpack.cli.actions as parser_actions

def make_init_subparser(subparser_factory: _SubParsersAction) -> None:
    init_parser: ArgumentParser = subparser_factory.add_parser("init")
    init_parser.set_defaults(func=parser_actions.init_action)

def make_add_builder_subparser(subparser_factory: _SubParsersAction) -> None:
    add_builder_parser: ArgumentParser = subparser_factory.add_parser(
        "add-builder", help="Add a new builder for generating project files"
    )
    add_builder_parser.add_argument(
        "remote-link", type=str,
        help="link of remote repository to clone"
    )
    add_builder_parser.add_argument(
        "builder-name", type=str, nargs="?", default=None,
        help="(optional) custom name for the builder"
    )

    add_builder_parser.set_defaults(func=parser_actions.add_builder_action)

def make_parser():
    subparsers = [make_init_subparser, make_add_builder_subparser]
    parser = ArgumentParser()
    subparser_factory = parser.add_subparsers()

    for make_subparser in subparsers:
        make_subparser(subparser_factory)

    