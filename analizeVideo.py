from pytubefix import YouTube

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

print(get_info(URL))
