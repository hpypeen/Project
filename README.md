# spotify-recommendation-system

Building the recommendation system for Spotify using Scikit-Learn

## Messages

I also ignored `csv` files, because it has over 1 gb.

## Data

https://www.kaggle.com/datasets/andrewmvd/spotify-playlists?select=spotify_dataset.csv

## Requirements

* Pandas
* NumPy
* Scikit-Learn

## Install

```commandline
pip install -r requirements.txt
```

## Algorithms

- [CountVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html) -
  Convert a collection of text documents to a matrix of token counts.
- [cosine_similarity](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html) -
  Compute cosine similarity between samples in X and Y.

## To do about documentation & blog

- [ ] need to write about `Data` section on the `README` file.
- [ ] need some resource to reference

## To do about coding

- [ ] Clean the data
- [ ] remove `user_id` (we don't need because that will not make helpful)
- [ ] Combine the `artistname` (remove spaces)
- [ ] Combine all columns to form a single column
- [x] Choose the algorithm

## PROJECT SECTIONS

1. DATA IMPORT
2. DATA DESCRIPTION
3. MOST POPULAR TRACKS
4. CLUSTER USERS INTO GENRE PREFERENCES
5. ARTIST RECOMMENDATION
6. CONCLUSION

## Resources

- [How to Build a Recommendation System in Python?](https://365datascience.com/tutorials/how-to-build-recommendation-system-in-python/)

## Logs

*(Daily updates)*

* 20 Jan 2023 - Started this project by [@tensorcist](https://github.com/idontcalculate)
  and [@iukt](https://github.com/iukt).
