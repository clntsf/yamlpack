from argparse import Namespace

from yamlpack.local.user_data import init_user_data
from yamlpack.local.builders import add_builder
from yamlpack.make_pack import make_pack

def init_action(_: Namespace):
    exit_code = init_user_data()

def add_builder_action(args: Namespace):
    exit_code = add_builder(args.remote_link, args.builder_name)

def make_action(args: Namespace):
    make_pack(args.package_path, args.schema_path)