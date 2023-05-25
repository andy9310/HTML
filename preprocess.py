import csv
def load_data():
    with open('Spotify_Youtube.csv', newline='') as csvfile:
        rows = csv.reader(csvfile)
        for i in rows:
            print(i)
def preprocess(): # d
    # change to dataframe 
    pass
load_data()