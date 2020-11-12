import pandas as pd
import os

class Music_Dataframe:
    def __init__(self, path = None):
        """Creates a dataframe. If path is specified, it loads songs from path into dataframe."""

        self.Music = pd.DataFrame(columns=['path'])
        if path is not None:
            self.load(path)
          
    #stores all music info from path
    def load(self, path):
        """Takes in directory, updates DataFrame with all songs in directory (recursive)."""

        all_music_data = []

        for root, dirs, files in os.walk(path):
            for filename in files:
                if os.path.splitext(filename)[1] == ".mp3" or os.path.splitext(filename)[1] == ".wav":
                    music_path = os.path.join(root, filename)

                    current_music_data = {}
                    current_music_data['path'] = music_path

                    all_music_data.append(current_music_data)

        #pd.append must be stored into a new place, otherwise nothing happens
        self.Music = self.Music.append(all_music_data, ignore_index = True)

    def print(self):
        print(self.Music)

    def size(self):
        return self.Music.shape[0]

