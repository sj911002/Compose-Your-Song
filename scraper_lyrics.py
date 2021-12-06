import lyricsgenius as lg

file_path = "C:/Users/Shania/Desktop/lyrics.txt"
file = open(file_path, "w")

artists = ["Frank Sinatra", "Paul Anka", "Ella Fitzgerald", "Don Williams", 
           "Roy Orbison", "Charles Pride", "Stevie Wonder","Willie Nelson", 
           "Frankie Valli", "Holly Dunn", "Carpenters", "Matt Monro"]


genius = lg.Genius("####", #Genius API Token goes here
                    skip_non_songs=True, 
                    excluded_terms=["(Live)"], 
                    remove_section_headers=True)

def get_lyrics(artists, k):
    counter = 0
    for name in artists:
        try:
            songs = (genius.search_artist(name, max_songs=k)).songs
            song_lyrics = [song.lyrics for song in songs]
            file.write("\n".join(song_lyrics))
            counter += 1
            print(f"Songs grabbed: {len(song_lyrics)}")
        except:
            print(f"Some exception at {name}: {counter}")    

get_lyrics(artists, 22)
