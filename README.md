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
Once you are satisfied with the quanitity that has been scraped (or you may simply use the preprovided list of video IDs), running `main.py` will iterate through the scraped videos and download both the audio and captions from each video. It will then extract the videos subtitles and their corresponding audio clips, which are parsed from a `.srt` file, and organize a tree of subdirectories within each video's data folder. Each subdirectory contains both a text file containing the phrase uttered in the short audio clip (`subtitles.txt`), and the corresponding audio in waveform (`audio.wav`).

You can also try it out with the included file `LastWeekTonight.txt`, which contains the contatenated video IDs of every video posted on [John Oliver's Last Week Tonight's YouTube Channel](https://www.youtube.com/user/LastWeekTonight/videos) as of March 22, 2021.

## Some Demos via Google Drive
* [Statistical Abstract of the United](https://drive.google.com/file/d/14zZ5Fxx2IagCg-QruMH6nUIOg7bdWBgZ/view?usp=sharing)
* [this is not a good use of your time](https://drive.google.com/file/d/142TVXPnyMb6cjg45iNpPPZXXXe5Tk-5I/view?usp=sharing)
* [all the background knowledge we have](https://drive.google.com/file/d/1FyWTnJ4RCyJdNA_QsJ9k53UgOBirf5ey/view?usp=sharing)
* [to adjust your parameters so next time](https://drive.google.com/file/d/1Kghoz5NoSPvJcWlghnE4M7fHM7wx9GYQ/view?usp=sharing)
* [a lot of the baselines all right so if you](https://drive.google.com/file/d/1ii6XSfvHuW-_Td2po_osBwMHEtZF3iGI/view?usp=sharing)

## Uses
* Voice Cloning
* TTS Engines
* Speaker Embedding
* Speaker Recognition

## Download
* [Download Sample via Kaggle](https://www.kaggle.com/ryanrudes/yttts-speech/download)
* [John Oliver Voice Dataset](https://www.kaggle.com/ryanrudes/johnoliver)
