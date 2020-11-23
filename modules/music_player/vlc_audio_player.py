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
        """
        Creates a playlist of files in the paths
        Plays the first instance of playlist
        """

        self.listPlayer.stop() #stop the player to refresh
        self.mediaList.release() #clear the old playlist

        self.mediaList = self.Player.media_list_new()
        for path in paths:
            self.mediaList.add_media(self.Player.media_new(path))
        
        #replace to current playlist
        self.listPlayer.set_media_list(self.mediaList)

        self.listPlayer.play()

    def play(self):
        self.listPlayer.play()
    def next(self):
        self.listPlayer.next()
    def pause(self):
        self.listPlayer.pause()
    def previous(self):
        self.listPlayer.previous()
    def stop(self):
        self.listPlayer.get_media_player().stop()

    def is_playing(self):
        """
        returns true if media is playing, false otherwise.
        """
        return bool(self.listPlayer.is_playing())

    def get_time(self):
        """
        returns time in ms in current media
        """
        return self.listPlayer.get_media_player().get_time()

    def set_time(self, ms):
        self.listPlayer.get_media_player().set_time(ms)

    def get_length(self):
        return self.listPlayer.get_media_player().get_length()
    
    def clear_playlist(self):
        """
        Empties vlc mediaList (object for playlist)
        Songs will still be played through playlist
        """
        self.mediaList.release()
        self.mediaList = self.Player.media_list_new()