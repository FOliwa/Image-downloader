from fetcher import ImageFetcherService
from pdf_creator import PDFCreatorService
from time import sleep
from datetime import datetime

# You have to define configs on your own
from configs.cit_conf import LABS, PRESENTATIONS
from configs.textbooks import BOOKS


def get_you_pdf(url, is_textbook=False):
    print(f'[LOG] {datetime.now().strftime("%Y-%m-%d %H:%M")} - Strat for {url}')

    service = ImageFetcherService(url, is_textbook)
    imgs_path, pdf_path = service.start()
    PDFCreatorService().create_pdf_from_png_images(pdf_path, imgs_path)

    print(f'[LOG] {datetime.now().strftime("%Y-%m-%d %H:%M")} END for {url}\n')
    sleep(4)


if __name__ == "__main__":
    for url in BOOKS:
        get_you_pdf(url, is_textbook=True)
