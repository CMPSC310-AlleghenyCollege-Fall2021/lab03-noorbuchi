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
for show_name in dataset["shows"]:
    show_id = ia.search_movie("westworld")[0].movieID
    movie = ia.get_movie(show_id)
    ia.update(movie, "episodes")
    show_episodes = movie.data["episodes"]
    for season_num, season in show_episodes.items():
        for episode_num, episode in season.items():
            episode = ia.get_movie(episode.movieID)
            try:
                out_data[f"{show_name}_S{season_num}_E{episode_num}"] = episode.data[
                    "plot"
                ]
                print(f"done getting {show_name}_S{season_num}_E{episode_num}")
            except KeyError as e:
                print(
                    f"couldn't get plot for {show_name}_S{season_num}_E{episode_num}. Moving on..."
                )

# store dataset
with open("raw_data.json", "w+", encoding="utf8") as outfile:
    json.dump(out_data, outfile, indent=4)


print("Done")
