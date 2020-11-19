"""
Shoutout to Pramod on stackoverflow
Related thread can be found on 
https://stackoverflow.com/questions/28440708/python-vlc-binding-playing-a-playlist
"""

import vlc
import time
import os

class VLC_Audio_Player:
    def __init__(self):
        self.Player = vlc.Instance()
        
        self.listPlayer = self.Player.media_list_player_new()
        self.listPlayer.set_playback_mode(vlc.PlaybackMode.loop) #loop if playlist over

        self.mediaList = self.Player.media_list_new()

    def addPlaylist(self, paths):
        self.mediaList = self.Player.media_list_new()
        for path in paths:
            self.mediaList.add_media(self.Player.media_new(path))
        
        #add the current playlist to list
        self.listPlayer.set_media_list(self.mediaList)
    def play(self):
        self.listPlayer.play()
    def next(self):
        self.listPlayer.next()
    def pause(self):
        self.listPlayer.pause()
    def previous(self):
        self.listPlayer.previous()
    def stop(self):
        self.listPlayer.stop()