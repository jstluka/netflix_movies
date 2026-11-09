import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

netflix_df = pd.read_csv("netflix_data.csv")

# Filter out TV shows
movies = netflix_df[netflix_df["type"] == "Movie"]


### Most common duration of '90s movies
# Filter to find '90s movies
movies_1990s = movies[(movies["release_year"] >= 1990) & (movies["release_year"] < 2000)]

# Find the most common duration of '90s movies
duration = movies_1990s["duration"].mode()[0]
print(duration)


### Number of short'90s action movies
# Filter to find action movies from the '90s that are shorter than 90 minutes
short_action_movies = movies_1990s[(netflix_df["duration"] < 90) & (netflix_df["genre"] == "Action")]

# Count the number of short '90s action movies
count_short_action_movies = len(short_action_movies)
print(count_short_action_movies)


### Plot of top ten countries by number of movies on Netflix (excl. US)
# Filter to find all non-US movies
movies_non_US = netflix_df[netflix_df["type"] == "Movie"][netflix_df["country"] != "United States"]

# Count how many movies per country
country_counts = movies_non_US["country"].value_counts()

# Create a barplot of the top 10 non-US countries by number of movies on Netflix
country_barplot = country_counts.head(10).plot(kind="bar")
plt.bar_label(country_barplot.containers[0])

# Add titles, labels, rotate country names, prevent cut-off text, show plot
plt.title("Top 10 Non-US Countries by Number of Netflix Movies")
plt.xlabel("Country")
plt.ylabel("Number of Movies")
plt.xticks(rotation=45, ha ='right')
plt.tight_layout()
plt.show()


### Plot of top ten genres of movies on Netflix
# Show plot separately from above plot
plt.figure()

# Count how many movies per genre
genre_counts = movies["genre"].value_counts()

# Create barplot, add labels to each bar
genre_barplot = genre_counts.head(10).plot(kind="bar")
plt.bar_label(genre_barplot.containers[0])

# Add titles, labels, rotate genre names, prevent cut-off text, show plot
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Genre")
plt.ylabel("Number of Movies")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


### Actor(s) in the most Netflix movies by country
# Separate cast lists into unique actors, count movies
actor_counts = (
    movies
    .dropna(subset=["cast", "country"])
    .assign(cast=lambda df: df["cast"].str.split(", "))
    .explode("cast")
    .groupby(["country", "cast"])
    .size()
    .reset_index(name="movie_count")
)

# Find the actor(s) with the most movies by country
top_actors_by_country = actor_counts[
    (actor_counts["movie_count"] == actor_counts.groupby("country")["movie_count"].transform("max"))
    & (actor_counts["movie_count"] > 1)
].sort_values(["movie_count", "country", "cast"], ascending = [False, True, True]).reset_index(drop=True)
print(top_actors_by_country.head(15))


### Actors/Directors of the most Netflix movies by genre
# Separate cast lists into unique actors, count movie genres
genre_actor_counts = (
    movies
    .dropna(subset=["cast", "genre"])
    .assign(cast=lambda df: df["cast"].str.split(", "))
    .explode("cast")
    .groupby(["genre", "cast"])
    .size()
    .reset_index(name="movie_count")
)

# Count movie genres for each director
genre_director_counts = (
    movies
    .dropna(subset=["director", "genre"])
    .groupby(["genre", "director"])
    .size()
    .reset_index(name="movie_count")
)

# Find the actor(s) with the most movies by country
top_actors_by_genre = genre_actor_counts[
    (genre_actor_counts["movie_count"] == genre_actor_counts.groupby("genre")["movie_count"].transform("max"))
    & (genre_actor_counts["movie_count"] > 1)
].sort_values(["movie_count", "genre", "cast"], ascending = [False, True, True]).reset_index(drop=True)
print(top_actors_by_genre.head(15))

top_directors_by_genre = genre_director_counts[
    (genre_director_counts["movie_count"] == genre_director_counts.groupby("genre")["movie_count"].transform("max"))
    & (genre_director_counts["movie_count"] > 1)
].sort_values(["movie_count", "genre", "director"], ascending = [False, True, True]).reset_index(drop=True)
print(top_directors_by_genre.head(15))


### Pairs of actors that have starred in multiple movies together
from collections import defaultdict
from itertools import combinations

# Remove rows without cast information
movie_casts = movies.dropna(subset=["cast"])

# Initialize tracking dictionaries
actor_pair_counts = defaultdict(int)
actor_pair_movies = defaultdict(list)

# Find all actor pairs
for _, row in movie_casts.iterrows():
    title = row["title"]

    # Split cast into individual actors
    actors = [actor.strip() for actor in row["cast"].split(",")]

    # Remove duplicates and empty names
    actors = list(set(actor for actor in actors if actor))

    # Generate all possible actor pairs
    for pair in combinations(sorted(actors), 2):
        actor_pair_counts[pair] += 1
        actor_pair_movies[pair].append(title)

# Convert the actor pairs to a DataFrame
actor_collabs = pd.DataFrame([
    {
        "Actor 1": pair[0],
        "Actor 2": pair[1],
        "Number of Movies Together": count,
        "Movies": ", ".join(actor_pair_movies[pair])
    }
    for pair, count in actor_pair_counts.items()
])

# Filter pairs for multiple movies together, sort by number of collabs
actor_collabs = (actor_collabs[actor_collabs["Number of Movies Together"] > 1]
.sort_values(by=["Number of Movies Together", "Movies", "Actor 1", "Actor 2"], ascending=[False, True, True, True]))


### Actor-Director pairs that have worked on multiple movies together
# Remove rows without cast or director information
movie_director_casts = movies.dropna(subset=["cast", "director"])

# Initialize tracking dictionaries
actor_director_pair_counts = defaultdict(int)
actor_director_pair_movies = defaultdict(list)

# Find all actor-director pairs
for _, row in movie_director_casts.iterrows():
    title = row["title"]

    # Split cast and director columns
    actors = [actor.strip() for actor in row["cast"].split(",")]
    directors = [director.strip() for director in row["director"].split(",")]

    # Remove duplicates and empty names
    actors = set(actor for actor in actors if actor)
    directors = set(director for director in directors if director)

    # Generate actor-director pairs
    for actor in actors:
        for director in directors:
            pair = (actor, director)
            actor_director_pair_counts[pair] += 1
            actor_director_pair_movies[pair].append(title)

# Convert actor-director pairs to a DataFrame
actor_director_collabs = pd.DataFrame([
    {
        "Actor": pair[0],
        "Director": pair[1],
        "Number of Movies Together": count,
        "Movies": ", ".join(actor_director_pair_movies[pair])
    }
    for pair, count in actor_director_pair_counts.items()
])

# Filter pairs for multiple movies together, sort by number of collabs
actor_director_collabs = (actor_director_collabs[actor_director_collabs["Number of Movies Together"] > 1]
.sort_values(by=["Number of Movies Together", "Movies", "Actor", "Director"], ascending=[False, True, True, True]))
