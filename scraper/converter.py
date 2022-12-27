"""File to convert tweet data json into csv"""
import csv
import json
from cleantext import clean


def convert(file: str, newfile: str):
    """
    Reads from json file, file and then converts to csv using the tweet and sport to newfile.
    Cleans tweet of emojis as well
    :param file: File to read from
    :param newfile: File to write to
    """
    # Opening JSON file
    f = open(file)

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    with open(newfile, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Tweet", "Sport"])
        for dict in data:
            tweet = dict["text"]
            tweet = clean(tweet, no_emoji=True)

            sport = dict["sport"]

            writer.writerow([tweet, sport])
