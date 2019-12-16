import argparse
from luigi import build
from tasks.tasks import Run_{{cookiecutter.graph_folder}}

#WE ARE AUTOFILLING THE COOKIECUTTER, BUT IF NEEDED ARGUMENTS FOR THE WRAPPER TASK MAY BE PROCESSED HERE!
parser = argparse.ArgumentParser(description='Command description.')

def main_script(args=None):
    args = parser.parse_args(args=args)

    build([
        Run_{{cookiecutter.graph_folder}}() #execute wrapper task Run_{{cookiecutter.graph_folder}}
    ], local_scheduler=True)

