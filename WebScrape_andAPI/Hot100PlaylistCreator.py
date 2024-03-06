import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

TIMETRAVEL = input("which year do you want to travel to? Type in this format: YYYY-MM-DD: ")   
URL = "https://www.billboard.com/charts/hot-100/"+TIMETRAVEL  #Hot100 Week you will scrape
#Spotify; remember you have to create an app through Spotify to make it work "https://developer.spotify.com/dashboard/"
SPOTIFY_CLIENTID = #"Enter your Spotify Client ID"
SPOTIFY_SECRET = #"Enter your Spotify Secret"
PLAYLIST_ID = #"Enter your Spotify playlist ID if you just want to update it"

#Scrapping Billboard
response = requests.get(URL)
billboard_website = response.text
soup = BeautifulSoup(billboard_website, "html.parser")
songs = soup.select(selector="li h3", class_ = "c-title")
artists = soup.select(selector="li span")

billboard_song_list_plus_extras = [song.get_text().strip() for song in songs]
billboard_artist_list_plus_extras = [artist.get_text().strip() for artist in artists]

# Create a new list of songs
index = billboard_song_list_plus_extras.index("Account")
billboard_hot100_songs = billboard_song_list_plus_extras[:index] #Your list with the songs

#Create a new list of artists
billboard_hot100_artists_almost_done = []

for n in billboard_artist_list_plus_extras:
    if not n.isdigit() and n != "-" and n != "NEW" and n !='' and n != 'RE-\nENTRY':
         billboard_hot100_artists_almost_done.append(n)
 
billboard_hot100_artists_almost_done = billboard_hot100_artists_almost_done[15:115]
billboard_hot100_artists = []   #Your list with the artirs
  
for artist in billboard_hot100_artists_almost_done:
    # Split the string at " Featuring " (with spaces)
  parts = artist.split(" Featuring ", 1)
  # use just the first artist
  modified_artist = parts[0]
  # Append the modified artist to the new list
  billboard_hot100_artists.append(modified_artist)



#Spotify API 
sp = spotipy.Spotify(    
        auth_manager=SpotifyOAuth(
            scope = "playlist-modify-public", #You can add multiple scopes depending on your goal. check the scopes on the spotofy api documentation https://developer.spotify.com/documentation/web-api/concepts/scopes
            redirect_uri="http://example.com",   #Needs to be exact the same as you enter when creating the App
            client_id = SPOTIFY_CLIENTID,
            client_secret = SPOTIFY_SECRET,
            show_dialog=True,
            cache_path="token.txt"
        )
) #login, and get the token
user_id = sp.current_user()["id"] #save UserID for later
print(user_id)

URIs=[]  #You will transfor the songs from the hot100 into URIs to later create and/or update the playlist
for song in billboard_hot100_songs:
    index= billboard_hot100_songs.index(song)
    result = sp.search(q=f"track:{song} artist:{billboard_hot100_artists[index]}",type="track")
    try:
        uri = result['tracks']['items'][0]['uri']
        URIs.append(uri)
    except:
        print(f"cannot find {song} by {billboard_hot100_artists[index]} in spotify, skipping") #some of them are not on spotify, other times the name is slightly different in spotify vs billboard
    
    
pprint.pprint(URIs)

#create a playlist and get its ID - ONLY FIRST TIME
playlist = sp.user_playlist_create(user=user_id, name=f"{TIMETRAVEL} Hott 100 songs", public=True, description='AS hot 100 songs no meu aniversario em 2012')
#pprint.pprint(playlist)
playlist_id = playlist['id']
#print(playlist_id)

#If your playlist already exists and you just want to get back to it:
#playlist = sp.playlist(playlist_id)

#Add songs to playlist using playlist id
sp.playlist_add_items(playlist_id = playlist_id, items=URIs)
