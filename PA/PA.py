from collections import Counter

def import_data(filename='albums_data.txt'):
    f = open(filename, "r")
    list = []
    for line in f:
        x = line.strip("\n").split(",")
        list.append(x)

    f.close()

    """
    Import data from a file to a list. Expected returned data format:
        ["David Bowie", "Low", "1977", "rock", "38:26"],
        ["Britney Spears", "Baby One More Time", "1999", "pop", "42:20"],
        ...]

    :param str filename: optional, name of the file to be imported

    :returns: list of lists representing albums' data
    :rtype: list
    """
    return list


def export_data(albums, filename='albums_data.txt', mode='a'):
    album_str = ""
    for x in range(len(albums)):
        if x < len(albums) - 1:
            album_str += albums[x] + ","
        else:
            album_str += albums[x] + "\n"
    if mode != "a" and mode != "w":
        raise ValueError("Wrong write mode")
    elif mode == "a":

        f = open(filename, "a")
        f.write(album_str)
        f.close()

    elif mode == "w":
        f = open("PA/albums_data.txt", "w")
        f.write(album_str)
        f.close()
    """
    Export data from a list to file. If called with mode 'w' it should overwrite
    data in file. If called with mode 'a' it should append data at the end.

    :param list albums: albums' data
    :param str filename: optional, name of file to export data to
    :param str mode: optional, file open mode with the same meaning as\
    file open modes used in Python. Possible values: only 'w' or 'a'

    :raises ValueError: if mode other than 'w' or 'a' was given. Error message:
        'Wrong write mode'
    """
    pass


def get_albums_by_genre(albums, genre):
    genres = []
    music_by_genre_list = []
    for lines in albums:
        genres.append(lines[3])
    if genre not in genres:
        raise ValueError("Genre not present in list")

    for lines in albums:
        if lines[3] == genre:
            music_by_genre_list.append(lines)



    """
    Get albums by genre

    :param list albums: albums' data
    :param str genre: genre to filter by

    :raises ValueError: if given genre is not present in the list. Error message: 'Genre not present in list'
    :returns: all albums of given genre
    :rtype: list
    """
    return music_by_genre_list


def get_genre_stats(albums):
    genres = []
    for lines in albums:
        genres.append(lines[3])
    count = Counter(genres)



    """
    Get albums' statistics showing how many albums are in each genre
    Example: { 'pop': 2, 'hard rock': 3, 'folk': 20, 'rock': 42 }

    :param list albums: albums' data
    :returns: genre stats
    :rtype: dict
    """
    return count


def get_longest_album(albums):
    time = []
    for lines in albums:
        temp_time = lines[4].split(":")
        temp_time[0] = int(temp_time[0]) * 60
        time.append(temp_time[0] + int(temp_time[1]))

    max_time = max(time)
    index = time.index(max_time)


    """
    Get album with biggest value in length field.
    If there are more than one such album return the first (by original lists' order)

    :param list albums: albums' data
    :returns: longest album
    :rtype: list
    """
    return albums[index]


def get_last_oldest(albums):
    years = []
    for lines in albums:
        years.append(int(lines[2]))
    max_time = min(years)
    index = years.index(max_time)
    """
    Get last album with earliest release year.
    If there is more than one album with earliest release year return the last
    one of them (by original list's order)

    :param list albums: albums' data
    :returns: last oldest album
    :rtype: list
    """
    return albums[index]


def get_last_oldest_of_genre(albums, genre):
    years = []
    genre_music = []
    for lines in albums:
        if lines[3] == genre:
            genre_music.append(lines)
    # print(genre_music)
    for lines in genre_music:
        years.append(int(lines[2]))

    max_time = min(years)
    index = years.index(max_time)
    """
    Get last album with earliest release year in given genre

    :param list albums: albums' data
    :param str genre: genre to filter albums by

    :raises ValueError: if given genre is not present in the list. Error message: 'Genre not present in list'
    :returns: last oldest album in genre
    :rtype: list
    """
    return genre_music[index]


def to_time(string):
    temp_time = string.split(":")
    temp_time[0] = int(temp_time[0]) * 60
    time = temp_time[0] + int(temp_time[1])

    """
    converts time in format "minutes:seconds" (string) to seconds (int)
    """
    return time


def get_total_albums_length(albums):
    time = []
    total_time = 0
    for lines in albums:
        temp_time = lines[4].split(":")
        temp_time[0] = int(temp_time[0]) * 60
        time.append(temp_time[0] + int(temp_time[1]))
    for lines in time:
        total_time += int(lines)
    print(total_time)
    """
    Get sum of lengths of all albums in minutes, rounded to 2 decimal places
    Example: 3:51 + 5:20 = 9.18
             231 + 320 seconds = 551 seconds

    :param list albums: albums' data
    :returns: total albums' length in minutes
    :rtype: float
    """
    pass


# data = ['Massive Attack', 'Blue Lines', '1991', 'hip hop', '45:02']
# export_data(data,"PA/albums_data.txt")
album_date = import_data("PA/albums_data.txt")
#print(get_albums_by_genre(album_date, "pop"))
#print(get_genre_stats(album_date))
#get_longest_album(album_date)
# print(get_last_oldest(album_date))
#print(get_last_oldest_of_genre(album_date, "pop"))
#to_time("45:02")
#get_total_albums_length(album_date)