from windows_media_control.media_manager import MediaManager
from gui import Gui
from lyrics_finder import LyricsFinder
from threading import Timer

gui = Gui(15, 70)
lf = LyricsFinder()
timer = None
suspended = False

def set_timer(*args):
    global timer
    if timer and timer.is_alive():
        timer.cancel()
    timer = Timer(3.0, on_song_changed, args=args)
    timer.start()
    gui.set_text('searching...')

def on_song_changed(session, args):
    if args.title:
        try:
            lyrics = lf.find_lyrics(args.title, args.artist)
            gui.set_text(lyrics)
        except:
            query = f'{args.title}{f" by {args.artist}" if args.artist else ""}'
            gui.set_message('Something went wrong. You can try to modify the query:', query)

def search_manually(*args):
    global suspended
    suspended = True
    set_event_listening(not suspended)
    timer.cancel()
    gui.set_message('Find song:', '')

def toggle_event_listening(*args):
    global suspended
    suspended = not suspended
    set_event_listening(not suspended)

def set_event_listening(listen: bool):
    if listen:
        MediaManager.start(send_mpc_after_csc=True)
    else:
        MediaManager.stop()

if __name__ == '__main__':
    MediaManager.set_on_media_properties_changed(set_timer)
    set_event_listening(True)
    gui.set_on_enter_callback(set_timer)
    gui.set_on_control_f_callback(search_manually)
    gui.set_on_control_r_callback(toggle_event_listening)
    gui.run()