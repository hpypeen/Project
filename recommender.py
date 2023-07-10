# import requried dependicies
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# read the data
df = pd.read_csv("data/song-dataset.csv", low_memory=False)[:1000]

# remove duplicates
df = df.drop_duplicates(subset="Song Name")

# drop Null values
df = df.dropna(axis=0)

# Removing space from "Artist Name" column
df["Artist Name"] = df["Artist Name"].str.replace(" ", "")

# Drop the non-required columns
df = df.drop(df.columns[3:], axis=1)

# Combine all columns and assgin as new column
df["data"] = df.apply(lambda value: " ".join(value.astype("str")), axis=1)

# models
vectorizer = CountVectorizer()
vectorized = vectorizer.fit_transform(df["data"])
similarities = cosine_similarity(vectorized)

# Assgin the new dataframe with `similarities` values
df_tmp = pd.DataFrame(similarities, columns=df["Song Name"], index=df["Song Name"]).reset_index()

true = True
while true:
    print("The Top 10 Song Recommendation System")
    print("-------------------------------------")
    print("This will generate the 10 songs from the database thoese are similar to the song you entered.")

    while True:
        input_song = input("Please enter the name of song: ")

        if input_song in df_tmp.columns:
            recommendation = df_tmp.nlargest(11, input_song)["Song Name"]
            break
        
        else:
            print("Sorry, there is no song name in our database. Please try another one.")
    
    print("You should check out these songs: \n")
    for song in recommendation.values[1:]:
        print(song)

    print("\n")
    while True:
        next_command = input("Do you want to generate again for the next song? [yes, no] ")

        if next_command == "yes":
            break

        elif next_command == "no":
            true = False
            break

        else:
            print("Please type 'yes' or 'no'")
