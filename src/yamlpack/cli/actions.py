from argparse import Namespace

from yamlpack.local.user_data import init_user_data

def init_action(_: Namespace):
    exit_code = init_user_data()