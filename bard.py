import json

def read_json_file():
    with open('songs1.json', 'r') as f:
        outer_dictionary = json.load(f)
        song_list = outer_dictionary.get("songlist")
    return song_list

def allow_users_choice(song_list1):
    global song
    the_playlist = []

    while True:
        number = 1

        for song in song_list1:
            title = song.get("title")
            artist = song.get("artist")
            print(f"{number}. {title} by {artist}")
            number += 1

        print("\nChoose a song to add to your playlist")
        num_chosen = int(input("Enter the song number: ")) - 1

        selected_song = song_list1[num_chosen]
        song_id = selected_song.get("id")
        title = selected_song.get("title")
        artist = selected_song.get("artist")
        year = selected_song.get("year")

        inner_list = [song_id, title, artist, year]
        the_playlist.append(inner_list)

        next_choice = input("Do you want to choose another song? Y or N: ").upper()
        if next_choice == "N":
            break

    return the_playlist

def write_to_csv(structure_o_songs):
    with open("my_playlist.csv", "w") as f:
        f.write("ID, Song Title, Artist, Year\n")

        for inner_list in structure_o_songs:
            song_id, title, artist, year = inner_list
            f.write(f"{song_id},{title},{artist},{year}\n")

if __name__ == "__main__":
    song_list1 = read_json_file()
    structure_of_songs = allow_users_choice(song_list1)
    write_to_csv(structure_of_songs)
