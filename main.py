import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

TIMETRAVEL = input("which year do you want to travel to? Type in this format: YYYY-MM-DD: ")
URL = "https://www.billboard.com/charts/hot-100/"+TIMETRAVEL
#Spotify
SPOTIFY_CLIENTID = "48cd0bbcd5f342dc977328f9d3971c1e"
SPOTIFY_SECRET = "67599e2d234640b8a6d6a4bb23cb8d3a"
PLAYLIST_ID = "4dzsRiEjzshLcuUQybwHVD"

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
billboard_hot100_songs = billboard_song_list_plus_extras[:index]
print(billboard_hot100_songs)

#Create a new list of artists
billboard_hot100_artists_almost_done = []

for n in billboard_artist_list_plus_extras:
    if not n.isdigit() and n != "-" and n != "NEW" and n !='' and n != 'RE-\nENTRY':
         billboard_hot100_artists_almost_done.append(n)
 
billboard_hot100_artists_almost_done = billboard_hot100_artists_almost_done[15:115]
billboard_hot100_artists = []
  
for artist in billboard_hot100_artists_almost_done:
    # Split the string at " Featuring " (with spaces)
  parts = artist.split(" Featuring ", 1)
  # use just the first artist
  modified_artist = parts[0]
  # Append the modified artist to the new list
  billboard_hot100_artists.append(modified_artist)

print(billboard_hot100_artists)


#Spotify API
sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope = "playlist-modify-public",
            redirect_uri="http://example.com",
            client_id = SPOTIFY_CLIENTID,
            client_secret = SPOTIFY_SECRET,
            show_dialog=True,
            cache_path="token.txt"
        )
)
user_id = sp.current_user()["id"]
print(user_id)

URIs=[]
for song in billboard_hot100_songs:
    index= billboard_hot100_songs.index(song)
    result = sp.search(q=f"track:{song} artist:{billboard_hot100_artists[index]}",type="track")
    try:
        uri = result['tracks']['items'][0]['uri']
        URIs.append(uri)
    except:
        print(f"cannot find {song} by {billboard_hot100_artists[index]} in spotify, skipping")
    
    
pprint.pprint(URIs)

#create a playlist and get its ID - ONLY FIRST TIME
playlist = sp.user_playlist_create(user=user_id, name=f"{TIMETRAVEL} Hott 100 songs", public=True, description='AS hot 100 songs no meu aniversario em 2012')
#pprint.pprint(playlist)
playlist_id = playlist['id']
#print(playlist_id)

#once playlist is created... to get back to it is:
#playlist = sp.playlist(playlist_id)

#Add songs to playlist using playlist id
sp.playlist_add_items(playlist_id = playlist_id, items=URIs)
