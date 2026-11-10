# netflix_movies
I started this project in DataCamp, with the following instructions:

> Perform exploratory data analysis on the netflix_data.csv data to understand more about movies from the 1990s decade.
>
> What was the most frequent movie duration in the 1990s? Save an approximate answer as an integer called duration (use 1990 as the decade's start year).
>
> A movie is considered short if it is less than 90 minutes. Count the number of short action movies released in the 1990s and save this integer as short_movie_count.

Afterwards, I decided to expand upon this project, with a few further questions to answer:
1. Who stars in the most Netflix movies for each country?
2. Who stars in the most movies for each genre? Who is the top director for each genre?
3. Which non-US countries are most represented here?
4. Which genres are most available on Netflix?
5. Which actors have worked on the most movies together? Which director-actor pairs have worked on the most movies together?

With this framework in mind, I set out to answer all these questions.

The results have been uploaded here. I don't intend to comment on all of my findings, here are some quick notes I have to share:
- I have removed the results from any of these lists where the number of movies is only 1. When that is the maximum number of movies that any actor/director has been involved in for a given country or genre then it is not necessary to show here. Likewise with actor pairs or actor-director pairs, as including values where the movie count is 1 would include any two actors who had ever worked on a film together.
- Anupam Kher is very clearly in the most movies in this dataset, with 39 movies on Netflix. The non-Indian actor with the next highest number of movies is Adam Sandler, with 19 movies on Netflix. A quick Google search can tell you that Anupam Kher has acted in over 500 movies, while very successful American actors rarely act in more than 100.
- Furthermore, since Anupam Kher has been in 39 movies, it makes sense that he has also starred in both the most comedies and the most action movies. You may note that Paresh Rawal, also a renowned Indian actor, has tied Anupam Kher for comedies on Netflix. Since they are both very prolific Bollywood actors, it is no wonder that they each star in many of the 858 Indian movies available on Netflix. A quick look at the actor pairs will show you that they haven't starred in very many movies together, at least not of their movies available on Netflix.
- Raúl Campos and Jan Suter have directed most, if not all, of the South American stand-up comedy specials available on Netflix.
- Looking at the actor pairs that have starred in multiple movies together, it is easy to see which franchises have many movies available on Netflix. Nearly all of the first 50 results in this set can be attributed to the Trailer Park Boys franchise, the Monster High franchise, or Monty Python.

<img width="496" height="560.5" alt="genre_barplot" src="https://github.com/user-attachments/assets/043098cf-cdd1-4648-93b0-08f2fc03134e" />

<img width="496" height="560.5" alt="country_barplot" src="https://github.com/user-attachments/assets/6c628e61-1a2c-40c2-826a-c623e56b1a40" />

