import tkinter as tk
import pytube as pt
from moviepy.editor import *
from pathlib import Path
from tkinter import messagebox


root = tk.Tk('Youtube Converter', 'Youtube Converter')
# root.title = 'Youtube Converter'
root.geometry('700x500')
root.resizable(False, False)

downloadPath = str(os.path.join(Path.home(), 'Downloads'))


def complete():
    comlabel = tk.Label(root, text='COMPLETE').pack()


def convert():
    gotten = entry.get()
    if 'https://www.youtube.com/watch' in gotten or 'https://youtu.be' in gotten:
        con = pt.YouTube(gotten, use_oauth=True,
                         allow_oauth_cache=True)
        # con.streams.get_audio_only().download(downloadPath)
        result = con.streams.filter(
            progressive=True, file_extension='mp4').first().download(downloadPath)
        video = VideoFileClip(result)
        audio = video.audio
        fileName = str(con.title).split('.')[0]
        audio.write_audiofile(os.path.join(downloadPath, fileName + '.mp3'))
        os.remove(result)
        messagebox.showinfo(
            'succesful', 'Your File Has Been Converted Check Your Download Folder')
    else:
        messagebox.showerror(
            'failed', 'This URL Is Invalid')


def download():
    gotten = entry.get()
    con = pt.YouTube(gotten).streams.filter(progressive=True,
                                            file_extension='mp4').first().download(downloadPath)
    messagebox.showinfo(
        'succesful', 'Your File Has Been Downloaded Check Your Download Folder')


label = tk.Label(root, text='Youtube Converter',
                 font=('Arial', 24)).pack(pady=30)
label1 = tk.Label(root, text='---------------------------------------------',
                  font=('Arial', 24)).pack(pady=30)
entry = tk.Entry(root, font=('Arial', 18), width=40)
entry.pack()
ConBtn = tk.Button(root, text='Convert', font=(
    'Arial', 18), command=convert, height=2, width=10)
ConBtn.place(x=170, y=300)
DowBtn = tk.Button(root, text='Download', font=(
    'Arial', 18), command=download, height=2, width=10)
DowBtn.place(x=400, y=300)

root.mainloop()
