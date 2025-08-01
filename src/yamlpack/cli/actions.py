from argparse import Namespace

import yamlpack.local.builders as builders
from yamlpack.local.user_data import init_user_data
from yamlpack.local.util import open_file, get_local_resource
from yamlpack.make_pack import make_pack

def init_action(_: Namespace):
    exit_code = init_user_data()

def add_builder_action(args: Namespace):
    exit_code = builders.add_builder(args.remote_link, args.builder_name)

def update_builder_action(args: Namespace):
    builders.update_builder(args.builder_name)

def rm_builder_action(args: Namespace):
    builders.delete_builder(args.builder_name)

def make_action(args: Namespace):
    make_pack(args.package_path, args.schema_path)

def update_config_action(_: Namespace):
    open_file(get_local_resource("settings.yml"))