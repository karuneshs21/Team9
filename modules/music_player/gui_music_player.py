from vlc_audio_player import VLC_Audio_Player
from music_dataframe import Music_Dataframe

from tkinter.filedialog import *
from tkinter import *

class FrameApp(Frame):
    def __init__(self,master):
        super(FrameApp, self).__init__(master)

        self.grid()
        self.paused = False
        self.player = VLC_Audio_Player()

        self.b1 = Button(self, text="play", command=self.play_music, width=20)
        self.b1.grid(row=1, column=0)

        self.b2 = Button(self, text="previous", command=self.previous_song,
                         width=20)
        self.b2.grid(row=2, column=0)

        self.b3 = Button(self, text="toggle", command=self.toggle, width=20)
        self.b3.grid(row=3, column=0)

        self.b4 = Button(self, text="next", command=self.next_song, width=20)
        self.b4.grid(row=4, column=0)

        self.b5 = Button(self, text="add to list", command=self.add_to_list,
                         width=20)
        self.b5.grid(row=5, column=0)

        self.label1 = Label(self)
        self.label1.grid(row=6, column=0)

        self.output = Text(self, wrap=WORD, width=50)
        self.output.grid(row=8, column=0)

        # TODO: Make progressbar, delete songs from playlist, amplify volume

    def add_to_list(self):
        """
        Opens window to browse data on disk and adds selected songs to play list
        :return: None
        """
        directory = askopenfilenames()
        # appends song directory on disk to playlist in memory
        self.player.addPlaylist(paths=directory)



    def play_music(self):
        """
        Plays Current Song
        :return: None
        """
        self.player.play()



    def toggle(self):
        """
        Toggles current song
        :return: None
        """
        pass


    def next_song(self):
        """
        Plays next song
        :return: None
        """
        self.player.next()


    def previous_song(self):
        """
        Plays prevoius song
        :return: 
        """
        self.player.previous()

    def check_music(self):
        pass


root = Tk()
root.geometry("350x500")
app = FrameApp(root)

while True:
    # runs mainloop of program
    app.check_music()
    app.update()