import json 
from pytubefix import YouTube
from pytubefix import Playlist

URL = "https://www.youtube.com/watch?v=sNcLm2MtvwE&list=PLQLz3vJxwofh8KSaJ7FoA5Bw2Zdvyo4S_&index=6"
URLPL = "https://www.youtube.com/playlist?list=PLQLz3vJxwofh8KSaJ7FoA5Bw2Zdvyo4S_"

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

#PlayList

def some_info_about_videos (pl_url: str):
    """Fetches basic info about a YouTube video.

    Note:
        Prints some info about videos

    Args:
        url (str): The URL of the YouTube playList.

    """
    pl = Playlist(pl_url)
    for video in pl.videos:
        print(video.title)
        print(video.views)
        #video duration (mins, secs)
        print(video.length // 60 ,'mins,', video.length - video.length // 60 * 60, 'secs' )
        print("------------")

def sorting_playlist_by_views (url_pl: str) -> list:
    """Fetches basic info about a YouTube video.

    Note:
        Makes and returns sorted dictonary by views of videos

    Args:
        url (str): The URL of the YouTube playList.

    Returns:
        dict: A dictionary containing the videos sorted by views
    """
    pl = Playlist(url_pl)
    all_videos = []

    for video in pl.video_urls:
        all_videos.append(get_info(video))

    all_videos.sort(key=lambda x: x['views'], reverse=True)
    return all_videos


if __name__ == '__main__':
    #print(get_info(URL))
    # info_about_videos(URLPL)
    print(sorting_playlist_by_views(URLPL))

    with open("sorted_by_view.json", 'w') as f:
        json.dump(sorting_playlist_by_views(URLPL), f, indent = 4) #  4 spaces of indentation per level
    
  