from termcolor import colored
from threading import Thread
from pytube import YouTube
from queue import Queue
from tqdm import tqdm
import soundfile
import librosa
import shutil
import pysrt
import os

def time2millis(time):
    return ((time.hour * 60 + time.minute) * 60 + time.second) * 1000 + time.microsecond / 1000

def process():
    while True:
        ID = queue.get()

        link = f"https://www.youtube.com/watch?v={ID}"
        path = f"data/data/{ID}"
        os.mkdir(path)

        youtube = YouTube(link)
        exists = False
        for captions in youtube.caption_tracks:
            if captions.name.startswith("English"):
                captions = captions.generate_srt_captions()
                srt_path = os.path.join(path, 'subtitles.srt')
                with open(srt_path, 'w') as f:
                    f.write(captions)
                exists = True
                break

        if not exists:
            print (colored(u"\U0001F534 " + ID, "red", attrs = ["bold"]))
            continue

        audio = youtube.streams.filter(only_audio = True, file_extension = 'mp4').first()
        audio.download(output_path = path, filename = 'audio')
        mp4_path = os.path.join(path, 'audio.mp4')

        y, sr = librosa.load(mp4_path, sr = 22000)
        subtitles = pysrt.open(srt_path)
        start = subtitles[0].start
        start_time = int(time2millis(start.to_time()) * sr / 1000)
        text = subtitles[0].text

        for line in tqdm(subtitles[1:], "Parsing"):
            end = line.start
            end_time = int(time2millis(end.to_time()) * sr / 1000)

            clip_path = os.path.join(path, str(start) + '-' + str(end))
            os.mkdir(clip_path)
            clip_text_path = os.path.join(clip_path, 'subtitles.txt')
            with open(clip_text_path, 'w') as f:
                f.write(text)
            clip = y[start_time:end_time + 1]
            start = end
            start_time = end_time
            text = line.text
            soundfile.write(os.path.join(clip_path, 'audio.wav'), clip, sr)

        os.remove(mp4_path)
        os.remove(srt_path)

        print (colored(u"\U0001F7E2 " + ID, "green", attrs = ["bold"]))
        queue.task_done()

workers = 8
queue = Queue(maxsize = workers)
for i in range(workers):
    Thread(target = process).start()

video_ids = open('/Volumes/Samsung T7 Touch/Ryan\'s iMac/New Drive/Users/markrudes/Downloads/youtube.txt', 'r')

while True:
    try:
        ID = video_ids.read(11)
        queue.put(ID)
    except Exception as e:
        print (str(e))

video_ids.close()
