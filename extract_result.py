import json
import pandas as pd

def reporting(folder, rubrique):
    with open(f"gridresults/{folder}/{rubrique}_report.json", "r") as file :
        report = json.load(file)
    pd.DataFrame(report).to_excel(f"gridresults/{folder}_{rubrique}.xlsx")


if __name__ == "__main__":
    #reporting("config-labse", "intent")
    #reporting("config-labse", "response_selection")
    reporting("config-regex", "intent")
    reporting("config-regex", "response_selection")
    #reporting("config-spacy", "intent")
    #reporting("config-camembert", "intent")
    reporting("config-Count", "intent")
    reporting("config-Count", "response_selection")
