from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
from threading import Thread
from queue import Queue
from time import sleep
from tqdm import tqdm

BUFFER = 64

writer_queue = Queue()
scrape_queue = Queue()

def writer():
    videos = set()
    writes = 0

    pbar = tqdm(total = BUFFER)
    while True:
        pbar.n = 0
        pbar.refresh()
        with open('videos.txt', 'a') as f:
            while pbar.n < BUFFER:
                video = writer_queue.get()
                if not video in videos:
                    scrape_queue.put(video)
                    videos.add(video)
                    f.write(video)
                    writes += 1

                    pbar.set_description('Latest: %s, Total: %d' % (video, writes))
                    pbar.update()
                    pbar.refresh()
                    sleep(1 / 30)

def scrape():
    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Chrome(options = options)
    while True:
        video = scrape_queue.get()
        url = 'https://www.youtube.com/watch?v=' + video
        browser.get(url)
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'thumbnail')))
        WebDriverWait(browser, 2)
        html = browser.page_source
        soup = BeautifulSoup(html, 'lxml')
        thumbnails = soup.find_all('a', id = 'thumbnail')
        for thumbnail in thumbnails:
            if thumbnail.has_attr('href'):
                href = thumbnail['href']
                if len(href) == 20:
                    video = href[-11:]
                    writer_queue.put(video)

Thread(target = writer).start()
for i in range(4):
    Thread(target = scrape).start()
scrape_queue.put('')
