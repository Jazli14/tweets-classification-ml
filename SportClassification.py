"""
File to create a machine learning model that distinguishes between sports given a tweet

Data Cleaning/Editing
Using context annotations determine which sport the tweet is referencing
Append information to dictionary
Use this info to train model



"""

import json


def main():
    # Opening JSON file
    f = open('new_data_copy.json')

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    print("Before loop")
    for dict in data:
        print("In loop")
        # check if context annotations exist
        # if so then iterate through and find domain name of sport
        # save the entity value related to that dict
        if "context_annotations" in dict:
            for context_dict in dict["context_annotations"]:
                dict["sport"] = "NA"
                domain_dict = context_dict["domain"]
                if domain_dict["name"] == "Sport":
                    entity_dict = context_dict["entity"]
                    sport = entity_dict["name"]
                    dict["sport"] = sport  # adds a sport parameter to main dictionary with the
                    # sport
                    break
            print(dict["sport"])

    # 3. Write json file
    with open("new_data_copy.json", "w") as file:
        json.dump(data, file)


# Right now the sport can only be determined with the specific sports annotation
# To accomodate a wider range of tweets it may be helpful to create a list of words
# that relate to a certain sport
if __name__ == "__main__":
    main()
