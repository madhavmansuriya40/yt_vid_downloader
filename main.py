import tkinter as tk
import customtkinter as ctk
from pytubefix import YouTube


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent_of_completion = (bytes_downloaded/total_size)*100
    progress_bar.set(percent_of_completion/100)
    
    per = str(int(percent_of_completion))
    p_percent.configure(text=per + '%')
    p_percent.update()



def start_download():
    try:
        finish_label.configure(text="Downloading ...", text_color='white')
        finish_label.update()

        yt_link = link.get()
        yt_object = YouTube(yt_link, on_progress_callback=on_progress)
        if check_var.get() == 'on':
            print("downloading audio")
            video = yt_object.streams.get_audio_only()
        else:
            video = yt_object.streams.get_highest_resolution()

        title.configure(text=yt_object.title, text_color='white')
        title.update()
        
        video.download()
        finish_label.configure(text="Downloaded!", text_color='green')
        finish_label.update()
    except Exception as e:
        print(f"There was some error downloading the video -> {e}")
        finish_label.configure(text="Somwthing went wrong!", text_color='red')


def checkbox_event():
    print("checkbox toggled, current value:", check_var.get())

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


frame = ctk.CTkFrame(master=app, width=200, height=200)
frame.pack(padx=10, pady=10)


url_var = tk.StringVar()
link = ctk.CTkEntry(frame, width=350, height=40, textvariable=url_var)
link.pack(side='left')

check_var = ctk.StringVar(value="off")
checkbox = ctk.CTkCheckBox(frame, text="Audio Only", command=checkbox_event,
                                     variable=check_var, onvalue="on", offvalue="off")
checkbox.pack(padx=10, pady=10,side='left')

download = ctk.CTkButton(app, text="Download", command=start_download)
download.pack(padx=10, pady=10)

p_percent = ctk.CTkLabel(app, text='0%')
p_percent.pack()

progress_bar = ctk.CTkProgressBar(app, width=400)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)

# finish downloading update
finish_label = ctk.CTkLabel(app, text="")
finish_label.pack()


# run app
app.mainloop()
