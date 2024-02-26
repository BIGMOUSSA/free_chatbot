import json
import pandas as pd

def reporting(folder, rubrique):
    with open(f"gridresults/{folder}/{rubrique}_report.json", "r") as file :
        report = json.load(file)
    pd.DataFrame(report).to_excel(f"gridresults/{folder}_{rubrique}.xlsx")


if __name__ == "__main__":
    #reporting("config-labse", "intent")
    #reporting("config-labse", "response_selection")
    reporting("config1", "intent")
    reporting("config2", "response_selection")
    #reporting("config-spacy", "intent")
    #reporting("config-camembert", "intent")
    reporting("config3", "intent")
    reporting("config4", "response_selection")
