from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter as tk
import time 
from tkinter import messagebox
from pytube import *
from pytube import YouTube
from pytube.exceptions import RegexMatchError
from pytube.exceptions import VideoUnavailable
import os
import youtube_dl
from tqdm import *
import pytube.request
from VideoPlayer import *
from PyQt5.QtWidgets import QApplication
import sys


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("500x300")
        self.title('Download Media Manager')
        # self.iconbitmap('Icon/downloadicon.ico')



        # Variables
        self.link = tk.StringVar()
        self.placeholder = tk.StringVar()
        self.placeholder.set('Paste link here')
        self.progress = 0
        self.max_progress = 100

        # Widgets
        download_label = tk.Label(
            self, text="Copy your link for downloading", font=("Arial", 11))
        download_label.place(x=20, y=10)

        self.combobox_selector = ttk.Combobox(self, values=[
                                         "YouTube", "Facebook"], state="readonly", width=20, font=("Arial", 12))
        self.combobox_selector.place(x=20, y=90)
        self.combobox_selector.current(0)# set default value to "YouTube"

        self.edit_link = tk.Entry(
            self, width=40, fg='grey', textvariable=self.placeholder)
        self.edit_link.place(x=20, y=40)
        self.edit_link.bind('<FocusIn>', self.on_entry_click)
        self.edit_link.bind('<FocusOut>', self.on_focusout)

        download_btn = tk.Button(self, text="Download", width=10, font=(
            "Arial", 10), state="normal", command=self.download_chosen)
        download_btn.place(x=120, y=220)

        self.pb = ttk.Progressbar(self, orient='horizontal', mode='determinate',
                                  length=200, maximum=self.max_progress, value=self.progress)
        self.pb.place(x=20, y=160)

        self.progress_label = tk.Label(self, text="0%", font=("Arial", 12))
        self.progress_label.place(x=220, y=160)

        self.btnOpen = Button(self, text="Open file",
                              command=self.open_file_dialog, width=10)
        self.btnOpen.place(x=20, y=220)


        self.quality_selector = ttk.Combobox(self, values=[
                                     "Highest resolution", "1080p", "720p", "480p", "360p", "240p", "144p"], state="readonly", width=20, font=("Arial", 12))
        self.quality_selector.place(x=20, y=120)
        self.quality_selector.current(0)

       

    def open_file_dialog(self):
        app = QApplication(sys.argv)

    # Create the video player window
        player = VideoPlayer()
        filepath = filedialog.askopenfilename(filetypes=[("Media files", "*.mp3;*.mp4;*.avi;*.flv;*.mkv;*.wmv")])
        if filepath:
            player.abrir(filepath)
            player.show()

    # Run the PyQt5 event loop
        sys.exit(app.exec_())

    #for placeholders 
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

    #for facebook
    def get_selected_quality(self):
        """Returns the format code for the selected quality"""
        quality = self.quality_selector.get()
        if quality == "Highest resolution":
            return 'bestvideo[height<=?1080][fps<=?30][vcodec!=?av01][vcodec!=?vp9.2][vcodec!=?vp9.3][vcodec!=?vp9.4][vcodec!=?vp9.5][vcodec!=?vp9.6]+bestaudio/best'
        elif quality == "1080p":
            return 'bestvideo[height<=1080][fps<=30][vcodec!=av01][vcodec!=vp9.2][vcodec!=vp9.3][vcodec!=vp9.4][vcodec!=vp9.5][vcodec!=vp9.6]+bestaudio/best'
        elif quality == "720p":
            return 'bestvideo[height<=720][fps<=30][vcodec!=av01][vcodec!=vp9.2][vcodec!=vp9.3][vcodec!=vp9.4][vcodec!=vp9.5][vcodec!=vp9.6]+bestaudio/best'
        elif quality == "480p":
            return 'bestvideo[height<=480][fps<=30][vcodec!=av01][vcodec!=vp9.2][vcodec!=vp9.3][vcodec!=vp9.4][vcodec!=vp9.5][vcodec!=vp9.6]+bestaudio/best'
        elif quality == "360p":
            return 'bestvideo[height<=360][fps<=30][vcodec!=av01][vcodec!=vp9.2][vcodec!=vp9.3][vcodec!=vp9.4][vcodec!=vp9.5][vcodec!=vp9.6]+bestaudio/best'
        elif quality == "240p":
            return 'bestvideo[height<=240][fps<=30][vcodec!=av01][vcodec!=vp9.2][vcodec!=vp9.3][vcodec!=vp9.4][vcodec!=vp9.5][vcodec!=vp9.6]+bestaudio/best'
        elif quality == "144p":
            return 'bestvideo[height<=144][fps<=30][vcodec!=av01][vcodec!=vp9.2][vcodec!=vp9.3][vcodec!=vp9.4][vcodec!=vp9.5][vcodec!=vp9.6]+bestaudio/best'
        else:
            return 'best'    


    def download_from_youtube(self):
        """Downloads the video using the provided link"""
        link = self.edit_link.get()
        quality = self.quality_selector.get()
        print(f"Downloading video from {link}...")
        if link:
            try:
                yt = YouTube(link)
                if quality == "Highest resolution":
                    video = yt.streams.get_highest_resolution()
                else:
                    video = yt.streams.filter(res=quality).first()
                if video:
                    title = video.title
                    filename = title + '.mp4'
                    video.download(filename)
                    self.pb['value'] = self.max_progress
                    self.progress_label.configure(text="100%")
                    messagebox.showinfo("Download Complete",
                                        "Video downloaded successfully!")
                else:
                    messagebox.showerror("Download Error", "Failed to download video")
            except Exception as e:
                print(f"Error: {e}")
                messagebox.showerror("Invalid Link", f"Error: {e}")
        else:
            messagebox.showerror("Invalid Link", "Please enter a valid YouTube link")



    def download_from_facebook(self):
        """Downloads the video using the provided link"""
        link = self.edit_link.get()
        quality = self.quality_selector.get()
        print(f"Downloading video from {link}...")
        if link:
            try:
                ydl_opts = {
                    'outtmpl': '%(title)s.%(ext)s',
                    'format': self.get_selected_quality(),
                    'progress_hooks': [self.download_hook]
                }
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    info_dict = ydl.extract_info(link, download=True)
                    title = info_dict.get('title', None)
                    if title:
                        filename = title + '.mp4'
                        self.pb['value'] = self.max_progress
                        self.progress_label.configure(text="100%")
                        messagebox.showinfo("Download Complete",
                                                "Video downloaded successfully!")
            except Exception as e:
                print(f"Error: {e}")
                messagebox.showerror("Invalid Link", f"Error: {e}")
        else:
            messagebox.showerror(
                    "Invalid Link", "Please enter a valid Facebook link.")

        
    def download_hook(self, d):
        """Update the progress bar during the download."""
        if d['status'] == 'finished':
            self.pb['value'] = self.max_progress
            self.progress_label.configure(text="100%")
            messagebox.showinfo("Download Complete",
                            "Video downloaded successfully!")
        else:
            progress = d.get('downloaded_bytes', 0) / d.get('total_bytes', 1) * 100
            self.pb['value'] = progress
            self.progress_label.configure(text=f"{progress:.2f}%")


    def download_chosen(self):
        selected = self.combobox_selector.get()
        if selected == "YouTube":
            self.download_from_youtube()

        elif selected == "Facebook":
            self.download_from_facebook()


if __name__ == '__main__':
    app = App()
    app.mainloop()
