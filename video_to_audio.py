from moviepy import VideoFileClip
from tkinter.filedialog import askopenfilename, asksaveasfilename

vid = askopenfilename(title="Select Video File")

save_path = asksaveasfilename(
    title="Save Audio As",
    defaultextension=".mp3",
    filetypes=[("MP3 Audio", "*.mp3")]
)

video = VideoFileClip(vid)
audio = video.audio

audio.write_audiofile(save_path)

video.close()
audio.close()

print("Done")