from datetime import datetime
my_data = [{
    'id': 472992592,
    'readable': True,
    'title': 'Moonlight',
    'title_short': 'Moonlight',
    'title_version': '',
    'link': 'https://www.deezer.com/track/472992592',
    'duration': 135,
    'rank': 895696,
    'explicit_lyrics': True,
    'explicit_content_lyrics': 1,
    'explicit_content_cover': 0,
    'preview': 'https://cdns-preview-e.dzcdn.net/stream/c-efe84e57a61d55f279c9f0c988eb4534-6.mp3',
    'md5_image': '9b6da786cd3ca8b286a04186b3c9079c',
    'artist': {'id': 9822974, 'name': 'XXXTENTACION', 'tracklist': 'https://api.deezer.com/artist/9822974/top?limit=50', 'type': 'artist'},
    'album': {
        'id': 58972642,
        'title': '?',
        'cover': 'https://api.deezer.com/album/58972642/image',
        'cover_small': 'https://e-cdns-images.dzcdn.net/images/cover/9b6da786cd3ca8b286a04186b3c9079c/56x56-000000-80-0-0.jpg',
        'cover_medium': 'https://e-cdns-images.dzcdn.net/images/cover/9b6da786cd3ca8b286a04186b3c9079c/250x250-000000-80-0-0.jpg',
        'cover_big': 'https://e-cdns-images.dzcdn.net/images/cover/9b6da786cd3ca8b286a04186b3c9079c/500x500-000000-80-0-0.jpg',
        'md5_image': '9b6da786cd3ca8b286a04186b3c9079c',
        'tracklist': 'https://api.deezer.com/album/58972642/tracks',
        'type': 'album'
    }, 'type': 'track'}]

#print(my_data[0])


def get_track_name():
    track_name = my_data[0]["title"]
    return track_name


#print(get_track_name())


def get_album_title():
    album_title = my_data[0]["album"]["title"]
    return album_title


#print(get_album_title())


def get_duration_in_minutes():
    duration_in_minutes = int(135/60) 
    return duration_in_minutes

print(get_duration_in_minutes())
print(135%60)

def get_link_to_the_song():
    link = my_data[0]["link"]
    return link


print(get_link_to_the_song())


def get_artist_name():
    artist_name = my_data[0]["artist"]["name"]
    return artist_name


print(get_artist_name())
