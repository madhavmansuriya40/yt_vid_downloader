import tkinter as tk
import customtkinter as ctk
from pytubefix import YouTube


def start_download():
    try:
        yt_link = link.get()
        print(yt_link)
        yt_object = YouTube(yt_link)
        video = yt_object.streams.get_highest_resolution()
        video.download()
        print("Download complete")
    except Exception as e:
        print(f"There was some error downloading the video -> {e}")


# system settings
app = ctk.CTk()

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

# App Frame
app.geometry("720x480")
app.title("Youtube Downloader")


# adding UI elements
title = ctk.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)


url_var = tk.StringVar()
link = ctk.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

download = ctk.CTkButton(app, text="Download", command=start_download)
download.pack(padx=10, pady=10)


# run app
app.mainloop()
