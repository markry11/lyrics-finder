import re
from lyrics_extractor import SongLyrics

class LyricsFinder:
    __extract_lyrics = None
    def __init__(self):
        self.__extract_lyrics = SongLyrics()
    def find_lyrics(self, title, artist):
        title = re.sub('\(.*\)', '', title)
        result = self.__extract_lyrics.get_lyrics(f'{title} {artist}')
        lyrics = result.get('lyrics')
        return lyrics