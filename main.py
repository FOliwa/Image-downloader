from fetcher import ImageFetcherService
from pdf_creator import PDFCreatorService
from urls import URLS

if __name__ == "__main__":
    for url in URLS:
        service = ImageFetcherService(url)
        imgs_path, pdf_path = service.start()
        PDFCreatorService().create_pdf_from_png_images(pdf_path, imgs_path)
