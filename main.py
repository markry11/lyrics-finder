from windows_media_control.media_manager import MediaManager
from gui import Gui
from lyrics_finder import LyricsFinder
gui = Gui(15, 70)
api_key = ''
engine_id = ''
lf = LyricsFinder(api_key, engine_id)

def on_song_changed(session, args):
    if args.title and args.artist:
        lyrics = lf.find_lyrics(args.title, args.artist)
        gui.set_text(lyrics)

if __name__ == '__main__':
    MediaManager.set_on_media_properties_changed(on_song_changed)
    MediaManager.start(send_mpc_after_csc=True)
    gui.run()