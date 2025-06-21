from pytubefix import YouTube

URL = "https://www.youtube.com/watch?v=tvZzjcaGs1U&list=PLfLD2TpGxVUwNhdJWh3lpAJLFBjV6ilqv&index=17"
yt = YouTube(URL)
print(yt.title)