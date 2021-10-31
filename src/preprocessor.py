import json
import re


with open("raw_data.json", "r", encoding="utf-8") as input_file:
    full_dataset = json.load(input_file)

processed_data = []

for movie_name, plots in full_dataset.items():
    for plot in plots:
        # TODO: remove commas periods and other stuff?
        # remove the :: and the data that follows
        if "::" in plot:
            plot = plot[: plot.index("::")]
        # remove underscores
        plot = plot.replace("_", "")
        # remove everything between parenthesis
        plot = re.sub("\(.*?\)", "", plot)
        plot = plot.replace(")", "")
        plot = plot.replace("(", "")
        processed_data.append(plot)

with open("processed_data.json", "w+", encoding="utf-8") as output_file:
    json.dump({"data": processed_data}, output_file)
