import tkinter as tk
from tkinter import ttk 
import moviepy.editor as mp 


win = tk.Tk()
win.title('convert mp4 video to mp3 audio')



# label 
app_title = ttk.Label(win, text='convert your mp4 video to mp3 audio')
app_title.grid(row=0, columnspan=3, sticky=tk.W)

#video label and entry 

video_label = ttk.Label(win, text='Drop Your Video Location Here: ')
video_label.grid(row=1, column=0, sticky=tk.W)

# entry video location
video_file = tk.StringVar()
video_location = ttk.Entry(win, width=35, textvariable=video_file)
video_location.grid(row=1, column=1)
video_location.focus()


#audio file saving location
audio_label = ttk.Label(win, text='Save As: ')
audio_label.grid(row=2, column=0, sticky=tk.W)


# entry audio location
audio_file = tk.StringVar()
audio_location = ttk.Entry(win, width=35, textvariable=audio_file)
audio_location.grid(row=2, column=1)



# process Unit

def action():

	video = video_file.get()
	audio = audio_file.get()

	clip = mp.VideoFileClip(video)
	clip.audio.write_audiofile(audio)



#Process Button

process_btn = ttk.Button(win, text='''let's convert''', command=action)
process_btn.grid(row=3, column=1, sticky=tk.W)




win.mainloop()
