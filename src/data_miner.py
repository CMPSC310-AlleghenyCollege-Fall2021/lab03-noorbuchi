import yaml

from imdb import IMDb
import json
from pprint import pprint

# create an instance of the IMDb class
ia = IMDb()

out_data = {}

with open("dataset.yaml", "r") as input_file:
    dataset = yaml.safe_load(input_file)


# geting movies
for movie_name in dataset["movies"]:
    found_movie = ia.search_movie(movie_name)[0]
    found_movie = ia.get_movie(found_movie.movieID)
    out_data[movie_name] = found_movie.data["plot"]
    print(f"done getting {movie_name}")

# getting shows
for show_id in dataset["shows"]:
    movie = ia.get_movie(show_id)
    ia.update(movie, "episodes")
    show_episodes = movie.data["episodes"]
    for season in show_episodes.values():
        for episode in season.values():
            episode = ia.get_movie(episode.movieID)
            pprint(vars(episode))
            break
        break

# pprint(vars(episode[1][1]))

# store dataset
with open("raw_data.json", "w+", encoding="utf8") as outfile:
    json.dump(out_data, outfile, indent=4)


print("Done")
