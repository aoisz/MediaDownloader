from tkinter import *
from tkinter import ttk
import tkinter as tk
import time
from pytube import *
from pytube.exceptions import RegexMatchError
import os
import youtube_dl
from tqdm import *
import pytube.request

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("792x450")
        self.title('Download Media Manager')
        self.iconbitmap('Icon/downloadicon.ico')

        # Variables
        self.link = tk.StringVar()
        self.placeholder = tk.StringVar()
        self.placeholder.set('Paste link here')
        self.progress = 0
        self.max_progress = 100

        # Widgets
        download_label = tk.Label(self, text="Paste your link to download here:", font=("Arial", 11))
        download_label.place(x=10, y=10)

        combobox_selector = ttk.Combobox(self, values=["YouTube", "Facebook"], state="readonly", width=20, font=("Arial", 12))
        combobox_selector.place(x=300, y=10)
        combobox_selector.current(0)  # set default value to "YouTube"

        self.edit_link = tk.Entry(self, width=40, fg='grey', textvariable=self.placeholder)
        self.edit_link.place(x=20, y=40)
        self.edit_link.bind('<FocusIn>', self.on_entry_click)
        self.edit_link.bind('<FocusOut>', self.on_focusout)

        #download_btn = tk.Button(self, text="Download", width=10, height=1, font=("Arial", 10), state="normal", command=self.download)
        #download_btn.place(x=540, y=10)

        self.pb = ttk.Progressbar(self, orient='horizontal', mode='determinate', length=500, maximum=self.max_progress, value=self.progress)
        self.pb.place(x=20, y=80)

    def on_entry_click(self, event):
        """Clears the placeholder text when user clicks on Entry"""
        if self.edit_link.get() == self.placeholder.get():
            self.edit_link.delete(0, "end")
            self.edit_link.config(fg='black')

    def on_focusout(self, event):
        """Displays the placeholder text if Entry is empty"""
        if self.edit_link.get() == '':
            self.edit_link.insert(0, self.placeholder.get())
            self.edit_link.config(fg='grey')

    # def download(self):
    #     """Downloads the video using the provided link"""
    #     link = self.edit_link.get()
    #     if link:
    #         try:
    #             yt = YouTube(link)
    #             video = yt.streams.first()
    #             title = video.title
    #             filename = title + '.mp4'
    #             video.download(filename)

    #             self.pb['value'] = self.max_progress
    #             messagebox.showinfo("Download Complete", "Video downloaded successfully!")

    #         except (RegexMatchError, VideoUnavailable, KeyError):
    #             messagebox.showerror("Invalid Link", "Please enter a valid YouTube link.")

    #     else:
    #         messagebox.showerror("Invalid Link", "Please enter a valid YouTube link.")


if __name__ == '__main__':
    app = App()
    app.mainloop()
