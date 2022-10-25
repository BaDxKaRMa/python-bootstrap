#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import sys

from dotenv import load_dotenv
from loguru import logger

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--debug", action="store_true", default=False, help="Enable debug logging"
    )
    args = parser.parse_args()
    # Remove all handlers
    logger.remove()
    # Set loguru format
    fmt = (
        "<level>{time:YYYY-MM-DD hh:mm:ss A}</level> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{"
        "function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level> "
    )

    # Set Debug level if --debug is passed
    if args.debug:
        logger.add(sys.stderr, format=fmt, level="DEBUG")
    else:
        logger.add(sys.stderr, format=fmt, level="INFO")

    # Load .env file
    logger.debug("Loading .env file")
    load_dotenv()

    # Load environment variables
    EXAMPLE_VARIABLE = os.getenv("EXAMPLE_VARIABLE")

    # Start here
    logger.success("Template Generated!")
