"""
Scrapes tweets from twitter
"""
# This will import the Twarc2 client and expansions class from twarc library and also the json
# library
from twarc import Twarc2, expansions
import json


def scrapeto(filewrite: str, num: int, token: str):
    """
    Scrapes sports tweets from twitters API and saves them within file. file must already be created
    :param filewrite: The name of the json file to write to
    :param num: Number of tweets wanted to be scraped
    :param token: Bearer Token from twitters api to scrape with
    """
    client = Twarc2(bearer_token=token)
    filename = filewrite

    # Remove existing rules
    existing_rules = client.get_stream_rules()
    if 'data' in existing_rules and len(existing_rules['data']) > 0:
        rule_ids = [rule['id'] for rule in existing_rules['data']]
        client.delete_stream_rule_ids(rule_ids)

    # Add new rules
    # Replace the rules below with the ones that you want to add as discussed in module 5
    new_rules = [
        {"value": "Soccer OR Football lang:en", "tag": "soccer-related-tweets"},
        {"value": "Basketball OR NBA lang:en", "tag": "basketball-related-tweets"},
        {"value": "Football OR Superbowl OR American Football lang:en", "tag": "football-related"
                                                                               "-tweets"},
        {"value": "Hockey OR Stanley Cup lang:en", "tag": "hockey-related-tweets"},
        {"value": "Baseball OR World Series lang:en", "tag": "baseball-related-tweets"}
    ]
    added_rules = client.add_stream_rules(rules=new_rules)

    # Connect to the filtered stream
    for count, result in enumerate(client.stream()):
        # The Twitter API v2 returns the Tweet information and the user, media etc.  separately
        # so we use expansions.flatten to get all the information in a single JSON
        tweet = expansions.flatten(result)  # flattens each result

        # 1. Read file contents
        with open(filename, "r") as file:
            data = json.load(file)

        # 2. Update json object
        data.extend(tweet)

        # 3. Write json file
        with open(filename, "w") as file:
            json.dump(data, file)

        # Replace with the desired number of Tweets
        if count > num:
            break

    # Delete the rules once you have collected the desired number of Tweets
    rule_ids = [rule['id'] for rule in added_rules['data']]
    client.delete_stream_rule_ids(rule_ids)
