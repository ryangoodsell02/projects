import json


# must contain multiple functions
# must have one main() function that calls all other functions


# read the JSON file
# hand exception if file is not found
# print user-friendly message if file not found

# display data as a list of songs to choose from
# create a playlist variable that is list data type
# allow the user to choose one or more songs.  Use loop
# print the output to a csv file with row headers

def read_json_file():
    open_file = open('songs1.JSON', 'r')
    outer_dictionary = json.load(open_file)
    song_list = outer_dictionary.get("songlist")
    open_file.close()
    return song_list


def allow_users_choice(song_list1):

    global song
    the_playlist = list()

    while True:


        number = 1

        for song in song_list1:
            title = song.get("title")
            artist = song.get("artist")
            print(str(number) + ".", title, "by", artist)
            number += 1

        print("\n Choose a song to add to your playlist")
        num_chosen = int(input("Enter the song number: "))


        selected_song = song_list1[num_chosen]
        song_id = song.get("id")
        title = song.get("title")
        artist = song.get("artist")
        year = song.get("year")



        inner_list = list()
        inner_list.append(song_id)
        inner_list.append(title)
        inner_list.append(artist)
        inner_list.append(year)

        # inner_list = [id, title, artist, year]

        the_playlist.append(inner_list)

        next_choice = input("Do you want to choose another song? Y or N: ").upper()
        if next_choice == "N":
            break
    return the_playlist


def write_to_csv(structure_of_songs):
    final_file = open('my_playlist.txt', 'w')
    final_file.write("ID, Song Title, Artist, Year\n ")

    for song_inner_list in structure_of_songs: #final_file:
        song_id = str(song_inner_list[0])
        title = song_inner_list[1]
        artist = song_inner_list[2]
        year = str(song_inner_list[3])
        final_file.write(song_id + "," + title + "," + artist + "," + year + "\n")
    final_file.close()

def main():
    song_list1 = read_json_file()
    structure_of_songs = allow_users_choice(song_list1)
    write_to_csv(structure_of_songs)


main()