from argparse import Namespace

from yamlpack.local.user_data import init_user_data
from yamlpack.local.builders import add_builder

def init_action(_: Namespace):
    exit_code = init_user_data()


def add_builder_action(args: Namespace):
    exit_code = add_builder(args.remote, args.name)