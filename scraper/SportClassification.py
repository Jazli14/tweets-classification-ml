"""
Using context annotations determine which sport the tweet is referencing
Append information to dictionary
Use this info to train model
"""

import json


def classify(file: str):
    """
    Takes in a json file with tweet data. Uses context annotations the main sport being discussed
    and creates a new kvp that states the sport being discussed
    :param file: file needed to be mutated with the sports parameter
    """
    events = ["Sports Event", "Sports League", "Sports Series", "Basketball Game"]

    soccer = ["2022 FIFA World Cup", "FIFA Men\'s World Cup", "Premier League", "Champions League",
              "Euros", "Ligue 1", "La Liga", "Copa América"]
    basketball = ["NCAA Men\'s Basketball", "Basketball Game", "NCAA", "NBA"]
    football = ["Super Bowl", "NFL", "The Super Bowl"]
    hockey = ["Stanley Cup", "NHL", "The Stanley Cup"]
    baseball = ["MLB", "World Series", "World Baseball Classic", "Premier12 World Championship"]

    # Opening JSON file
    f = open(file)

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    for dict in data:
        # check if context annotations exist
        # if so then iterate through and find domain name of sport
        # save the entity value related to that dict
        dict["sport"] = "NA"
        if "context_annotations" in dict:
            for context_dict in dict["context_annotations"]:
                domain_dict = context_dict["domain"]
                if domain_dict["name"] == "Sport":
                    entity_dict = context_dict["entity"]
                    sport = entity_dict["name"]
                    dict["sport"] = sport  # adds a sport parameter to main dictionary with the
                    # sport
                    break
                if domain_dict["name"] in events:
                    entity_dict = context_dict["entity"]
                    sport = entity_dict["name"]

                    if sport in soccer:
                        dict["sport"] = "Soccer"
                    elif sport in basketball:
                        dict["sport"] = "Basketball"
                    elif sport in hockey:
                        dict["sport"] = "Hockey"
                    elif sport in football:
                        dict["sport"] = "American Football"
                    elif sport in baseball:
                        dict["sport"] = "Baseball"

    # 3. Write json file
    with open(file, "w") as file:
        json.dump(data, file)

# Right now the sport can only be determined with the specific sports annotation
# To accommodate a wider range of tweets it may be helpful to create a list of words
# that relate to a certain sport
