import os
import re
import sys
import logging

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

logger = logging.getLogger()

STARTDIR = ""
WRITETODIR = "/tmp/testing.log"
FILENAMEPATTERN = "^.*\.js$"
EXCLUDETHIS = ["^node_modules$", "^.git$"]
LOOKFORSTRING = ".*this\.menu.*$"

matched_files = []
strings_found_in_files = [tuple()]


def checkForExcluded(content):
    for exclude in EXCLUDETHIS:
        if re.match(exclude, content):
            logger.debug(f"{content} is excluded, return")
            return True


def processDirectory(path):
    contents = os.listdir(path)
    logger.debug(f"Path {path} has following entries: {','.join(contents)}")
    for content in contents:
        if checkForExcluded(content):
            continue
        new_path = os.path.join(path, content)
        if os.path.isdir(new_path):
            logger.debug(f"{content} is a directory, iterating...")
            processDirectory(new_path)
        elif re.match(FILENAMEPATTERN, content):
            logger.info(f"Found a match @{content}")
            logger.debug(f"Storing for later analyzis")
            matched_files.append(new_path)
        else:
            logger.debug(f"{content} is a not matched file")


def parseFileForString(path):
    with open(path) as file:
        row_count = 0
        for row in file.readlines():
            row_count += 1
            if re.match(LOOKFORSTRING, row):
                logger.debug(f"Found refrence in {path} ({row_count})-> {row}")
                strings_found_in_files.append((path, str(row_count)))


if STARTDIR is not None:
    logger.info(f"Start path is {STARTDIR}")
    processDirectory(STARTDIR)
else:
    logger.debug(f"No directory provided, starting from {os.getcwd()}")
    processDirectory(os.getcwd())

logger.info(f"Found total of {len(matched_files)} matches")

for match in matched_files:
    parseFileForString(match)

logger.info(f"Found total of matches from files {len(strings_found_in_files)}")

with open(WRITETODIR, "w") as file:
    logger.debug(f"Writing to {WRITETODIR}")
    for entry in strings_found_in_files:
        file.write(",".join(entry) + "\n")
