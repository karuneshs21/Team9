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

        self.list_songpaths = []

        self.mediaList = self.Player.media_list_new()

    def addPlaylist(self, paths):
        """
        Creates a playlist of files in the paths
        Plays the first instance of playlist
        """

        self.listPlayer.stop() #stop the player to refresh
        self.clear_playlist() #clear playlist

        self.mediaList = self.Player.media_list_new()
        for path in paths:
            self.mediaList.add_media(self.Player.media_new(path))
            self.list_songpaths.append(path)
        
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
        """
        self.mediaList.release()
        self.mediaList = self.Player.media_list_new()
        self.list_songpaths.clear()

    def play_song_from_current_playlist(self, song_path):
        """
        Takes in path to song, plays the song if it is the current playlist.
        Returns True if song is being played
        Returns False if song is not in the playlist
        """
        try:
            index = self.list_songpaths.index(song_path)
        except ValueError:
            return False
        played = self.listPlayer.play_item_at_index(index)
        
        return (played == 0) #exit code 0 if played no error