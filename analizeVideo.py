from pytubefix import YouTube
from pytubefix import Playlist

URL = "https://www.youtube.com/watch?v=sNcLm2MtvwE&list=PLQLz3vJxwofh8KSaJ7FoA5Bw2Zdvyo4S_&index=6"


def get_info(url: str) -> dict:
    """Fetches basic info about a YouTube video.

    Note:
        Returns 1.title, 2.views, etc...

    Args:
        url (str): The URL of the YouTube video.

    Returns:
        dict: A dictionary containing the video's title, view, etc...
    """
    yt = YouTube(url)
    data = {
        "title": yt.title,
        "views": yt.views,
        "length_seconds": yt.length
    }
    return data

#print(get_info(URL))

#PlayList

URL = "https://www.youtube.com/playlist?list=PLQLz3vJxwofh8KSaJ7FoA5Bw2Zdvyo4S_"


def info_about_videos (pl_url):
    pl = Playlist(pl_url)
    for video in pl.videos:
        print(video.title)
        print(video.views)
        #video duration (mins, secs)
        print(video.length // 60 ,'mins,', video.length - video.length // 60 * 60, 'secs' )
        print("------------")

info_about_videos(URL)

