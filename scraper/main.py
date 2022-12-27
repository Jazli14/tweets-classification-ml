"""
Main to call all functions from
"""
import TwitterScrape as ts
import SportClassification as sc
import converter
if __name__ == "__main__":
    # Fill in bearer token given from twitter API
    token = ""
    ts.scrapeto("SportsTweets.json", 10000, token)
    sc.classify("SportsTweets.json")
    converter.convert("SportsTweets.json", "SportsTweets.csv")
