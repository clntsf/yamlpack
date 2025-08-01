from argparse import ArgumentParser, _SubParsersAction

import yamlpack.cli.actions as parser_actions

def make_init_subparser(subparser_factory: _SubParsersAction) -> None:
    """Make subparser for the `yamlpack init` command"""

    init_parser: ArgumentParser = subparser_factory.add_parser(
        "init", help="initialize user data directory and add default builder plugin"
    )
    init_parser.set_defaults(func=parser_actions.init_action)

def make_add_builder_subparser(subparser_factory: _SubParsersAction) -> None:
    """Make subparser for the `yamlpack add-builder REMOTE_LINK [name]` command """

    add_builder_parser: ArgumentParser = subparser_factory.add_parser(
        "add-builder", help="add a new builder for generating project files"
    )
    add_builder_parser.add_argument(
        "remote_link", type=str, metavar="remote-link",
        help="link of remote repository to clone"
    )
    add_builder_parser.add_argument(
        "builder_name", type=str, metavar="builder-name", nargs="?", default=None,
        help="(optional) custom name for the builder"
    )

    add_builder_parser.set_defaults(func=parser_actions.add_builder_action)

def make_update_builder_subparser(subparser_factory: _SubParsersAction) -> None:
    """Make subparser for the `yamlpack update-builder BUILDER_NAME` command"""

    update_builder_parser: ArgumentParser = subparser_factory.add_parser(
        "update-builder", help="update builder with given name"
    )
    update_builder_parser.add_argument(
        "builder_name", type=str, metavar="builder-name",
        help="name of the builder to update"
    )

    update_builder_parser.set_defaults(func=parser_actions.update_builder_action)

def make_rm_builder_subparser(subparser_factory: _SubParsersAction) -> None:
    """Make subparser for the `yamlpack rm-builder BUILDER_NAME` command"""

    rm_builder_parser: ArgumentParser = subparser_factory.add_parser(
        "rm-builder", help="delete builder with given name"
    )
    rm_builder_parser.add_argument(
        "builder_name", type=str, metavar="builder-name",
        help="name of the builder to delete"
    )

    rm_builder_parser.set_defaults(func=parser_actions.rm_builder_action)

def make_make_subparser(subparser_factory: _SubParsersAction) -> None:
    """Make subparser for the `yamlpack make PACKAGE_PATH SCHEMA_PATH` command"""

    make_subparser: ArgumentParser = subparser_factory.add_parser(
        "make", help="make a package at package-path with schema at schema-path. Paths can be absolute or relative to cwd."
    )
    make_subparser.add_argument(
        "package_path", type=str, metavar="package-path",
        help="path to folder which should be the toplevel of the new package"
    )
    make_subparser.add_argument(
        "schema_path", type=str, metavar="schema-path",
        help="path to the schema to use in constructing the package."   
    )
    make_subparser.set_defaults(func=parser_actions.make_action)

def make_update_config_subparser(subparser_factory: _SubParsersAction) -> None:
    update_config_subparser: ArgumentParser = subparser_factory.add_parser(
        "update-config", help="Access and update user configuration settings"
    )
    update_config_subparser.set_defaults(func=parser_actions.update_config_action)

def make_parser():
    subparsers = [
        make_init_subparser,
        make_add_builder_subparser,
        make_update_builder_subparser,
        make_rm_builder_subparser,
        make_make_subparser,
        make_update_config_subparser,
    ]

    parser = ArgumentParser()
    subparser_factory = parser.add_subparsers(required=True)
    parser.set_defaults()

    for make_subparser in subparsers:
        make_subparser(subparser_factory)

    return parser

    