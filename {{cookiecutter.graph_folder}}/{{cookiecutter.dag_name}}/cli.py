import argparse
from luigi import build
from tasks.tasks import Run_lui_gui

# DEFAULT ENTRY, JUST IN CASE:
#parser = argparse.ArgumentParser(description='Command description.')
#parser.add_argument('names', metavar='NAME', nargs=argparse.ZERO_OR_MORE,
#                    help="A name of something.")


#def main_script(args=None):
#    args = parser.parse_args(args=args)
#    print(args.names)

#######################

#DO NOT NEED TO PARSE ARGUMENTS, SINCE WE ARE AUTOFILLING THE COOKIECUTTER
parser = argparse.ArgumentParser(description='Command description.')
#parser.add_argument("-f", "--file", default="luigi.jpg") # what torch model to use
#parser.add_argument("-r", "--root", default="data") # subdirectory for model


def main_script(args=None):
    args = parser.parse_args(args=args)

    build([
        Run_lui_gui(args.file, args.root) #execute wrapper task
    ], local_scheduler=True)

