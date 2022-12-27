"""
File to test filtered topic tweets
Randomly selects tweets
Returned 7 tweets when count=5

problem currently only writes last tweet. Probably because it overwrites the old ones each iter.
"""
# This will import the Twarc2 client and expansions class from twarc library and also the json
# library
from twarc import Twarc2, expansions
import json

# This is where you initialize the client with your own bearer token (replace the XXXXX with your
# own bearer token)
client = Twarc2(bearer_token="AAAAAAAAAAAAAAAAAAAAAJ46kwEAAAAApwXbyK%2FcsdlbNx0RDHOnTsbyhFI%3DqYBc"
                             "S2NQTtWp2FykUd82mAzRx3I2l6HXxGRqMl87QYDuUl8yVu")


def main():
    filename = 'big_data.json'

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
        {"value": "Baseball OR MLB lang:en", "tag": "baseball-related-tweets"}
    ]
    added_rules = client.add_stream_rules(rules=new_rules)

    # Connect to the filtered stream
    for count, result in enumerate(client.stream()):
        # The Twitter API v2 returns the Tweet information and the user, media etc.  separately
        # so we use expansions.flatten to get all the information in a single JSON
        tweet = expansions.flatten(result)  # flattens each result
        # Here we are printing the full Tweet object JSON to the console
        json_string = json.dumps(tweet)
        # print(json_string)

        # # Using a JSON string
        # with open('new_data.json', 'a') as outfile:
        #     outfile.write(json_string)

        # with open('tweets.txt', 'a+') as filehandle:
        #     for t in tweet:
        #         filehandle.write('%s\n' % json.dumps(t))

        # 1. Read file contents
        with open(filename, "r") as file:
            data = json.load(file)

        # 2. Update json object
        data.extend(tweet)

        # 3. Write json file
        with open(filename, "w") as file:
            json.dump(data, file)

        # Replace with the desired number of Tweets
        if count > 15000:
            break

    # Delete the rules once you have collected the desired number of Tweets
    rule_ids = [rule['id'] for rule in added_rules['data']]
    client.delete_stream_rule_ids(rule_ids)


# Need to clean json file s.t. after each dictionary object insert comma remove brackets signifying
# end of dictionary on both sides
if __name__ == "__main__":
    main()
