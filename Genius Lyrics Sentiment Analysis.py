#Import LyricsGenius library as genius (since LyricsGenius is a library based off the Genius website)

import lyricsgenius as genius

#Import API for sentiment analysis
from textblob import TextBlob

#Import re
import re

#Arist Dictionary - EDIT THIS LIST FOR NEW SAMPLE SIZE!
Artists_List = {'Smino', 'Mick Jenkins', 'Taylor Bennett'}

#Input Selection for Artists - MAKE SURE TO EDIT THE INPUTS!
while True:
    artist_search = input("Please input either Smino, Mick Jenkins, or Taylor Bennett --> \n")
    if artist_search.title() in Artists_List:
        break
    else:
        print("Please try again in the line below! \n")

#API Collection Token - ENTER YOURS HERE!
API_Key = 'x5iyfMSswgMyYjBfiT8TrbuUHFaX4lMqQNMINNeU8oLfjBvqJOCGTv8upNY1soJi'
API = genius.Genius(API_Key)

#Searches for the artist inputted
artist = API.search_artist(artist_search, max_songs=5)


#Input Selection for Songs
New_Song = input("Search one of the new songs in output \n")

Song = API.search_song(New_Song.title(),artist.name)

#To generate new list out of the Song variable
New_Song_List = [Song]

while True:
    if New_Song.title() in New_Song_List:
        print("Retrieving... \n")
        break
    else:
        print("Please try again in the line below! \n")
        break
print(Song)





#wiki = TextBlob("i am so happy")
#print(wiki.sentiment.polarity)