import argparse
from luigi import build
from .lui_gui.io.{{cookiecutter.node4_run_target}} import {{cookiecutter.node4_run_target}}


# DEFAULT ENTRY, JUST IN CASE:
#parser = argparse.ArgumentParser(description='Command description.')
#parser.add_argument('names', metavar='NAME', nargs=argparse.ZERO_OR_MORE,
#                    help="A name of something.")


#def main_script(args=None):
#    args = parser.parse_args(args=args)
#    print(args.names)


parser = argparse.ArgumentParser(description='Command description.')
parser.add_argument("-i", "--image", default="luigi.jpg") # what torch model to use
parser.add_argument("-m", "--model", default="mosaic.pth") # what image to stylize
parser.add_argument("-r", "--root", default="data") # subdirectory for model


def main_script(args=None):
    args = parser.parse_args(args=args)

    build([
        {{cookiecutter.node4_run_target}}(args.model, args.image, args.root)
    ], local_scheduler=True)

