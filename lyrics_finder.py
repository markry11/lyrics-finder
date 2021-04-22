from lyrics_extractor import SongLyrics
class LyricsFinder:
    __extract_lyrics = None
    def __init__(self, api_key, engine_id):
        self.__extract_lyrics = SongLyrics(api_key, engine_id)
    def find_lyrics(self, title, artist):
        result = self.__extract_lyrics.get_lyrics(f'{title} {artist}')
        lyrics = result.get('lyrics')
        return lyrics