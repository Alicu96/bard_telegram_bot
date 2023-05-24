from icrawler.builtin import GoogleImageCrawler
import os

save_dir = '/opt/temp/'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
google_crawler = GoogleImageCrawler(storage={'root_dir': save_dir})

def get_image(keyword):
    google_crawler.crawl(keyword=keyword, max_num=1)

