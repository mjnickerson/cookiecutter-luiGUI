import argparse
from luigi import build
from tasks.tasks import Run_lui_gui


#WE ARE AUTOFILLING THE COOKIECUTTER, BUT WE MAY NEED TO SEND ARGUMENTS FOR THE FILE NAME TO BE PROCESSED HERE!
parser = argparse.ArgumentParser(description='Command description.')
parser.add_argument("-f", "--file", default="luigi.jpg") # what file to process
parser.add_argument("-r", "--root", default="data") # subdirectory for process


def main_script(args=None):
    args = parser.parse_args(args=args)

    build([
        Run_lui_gui(args.file, args.root) #execute wrapper task
    ], local_scheduler=True)

