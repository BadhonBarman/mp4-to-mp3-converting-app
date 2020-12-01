# Python code to convert video to audio 



# import moviepy.editor as mp 

# clip = mp.VideoFileClip(r'Enter Your File Location (video)')
# clip.audio.write_audiofile(r'Enter Your File Location (audio)')





import moviepy.editor as mp 


video_location = 'C:/Users/sbc/Desktop/apy/v.mp4'
audio_location = 'C:/Users/sbc/Desktop/apy/a.mp3'

clip = mp.VideoFileClip(video_location)
clip.audio.write_audiofile(audio_location)













