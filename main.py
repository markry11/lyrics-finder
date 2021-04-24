from windows_media_control.media_manager import MediaManager
from gui import Gui
from lyrics_finder import LyricsFinder
from threading import Timer

gui = Gui(15, 70)
lf = LyricsFinder()
timer = None

def set_timer(*args):
    global timer
    if timer and timer.is_alive():
        timer.cancel()
    timer = Timer(3.0, on_song_changed, args=args)
    timer.start()
    gui.set_text('searching...')

def on_song_changed(session, args):
    if args.title and args.artist:
        lyrics = lf.find_lyrics(args.title, args.artist)
        gui.set_text(lyrics)

if __name__ == '__main__':
    MediaManager.set_on_media_properties_changed(set_timer)
    MediaManager.start(send_mpc_after_csc=True)
    gui.run()