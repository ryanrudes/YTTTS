# YTTTS

The YouTube Text-To-Speech dataset is comprised of waveform audio extracted from YouTube videos alongside their English transcriptions

`videos.txt` is a text file that consists of concatenated YouTube video IDs. YouTube video URLs are in the format `https://www.youtube.com/watch?v=<video-id>`, for example:

> [https://www.youtube.com/watch?v=`BRRolKTlF6Q`](https://www.youtube.com/watch?v=BRRolKTlF6Q)

A YouTube video ID is always 11 characters in length, so to read in video IDs from the example file provided, you simply have to read the contents in 11 byte chunks:

```python
with open('videos.txt', 'r') as f:
  while True:
    ID = f.read(11)
    print (ID)
```

`scrape.py` scrapes YouTube video IDs and continuously appends them to the file `videos.txt`. \
Once you are satisfied with the quanitity that has been scraped (or you may simply use the preprovided list of video IDs), running `main.py` will iterate through the scraped videos and download both the audio and captions from each video. It will then parse the videos subtitles, which are stored in the `.srt` file format, and organize a tree of subdirectories within each video's data folder. Each subdirectory contains both a text file containing the phrase uttered in the short audio clip (`subtitles.txt`), and the corresponding audio in waveform (`audio.wav`).


## Uses
* Voice Cloning
* TTS Engines
* Speaker Embedding
* Speaker Recognition

## Download
* [Download Sample via Kaggle](https://www.kaggle.com/ryanrudes/yttts-speech/download)
