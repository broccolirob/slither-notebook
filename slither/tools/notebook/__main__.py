import argparse
import logging
from crytic_compile import cryticparser
from slither import Slither

logging.basicConfig()
logging.getLogger("Slither").setLevel(logging.INFO)

logging.getLogger("Slither-Notebook").setLevel(logging.INFO)
logger = logging.getLogger("Slither-Notebook")


def parse_args():
    """
    Parse the underlying arguments for the program.
    :return: Returns the arguments for the program.
    """
    parser = argparse.ArgumentParser(description="slither-notebook", usage="slither-notebook filename")

    parser.add_argument(
        "filename", help="The filename of the contract or truffle directory to analyze."
    )

    # Add default arguments from crytic-compile
    cryticparser.init(parser)

    return parser.parse_args()


def main():
    args = parse_args()

    # Perform slither analysis on the given filename
    _slither = Slither(args.filename, **vars(args))

    logger.info("Notebook setup and installed correctly!")


if __name__ == "__main__":
    main()
