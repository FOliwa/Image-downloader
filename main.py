from fetcher import ImageFetcherService
from pdf_creator import PDFCreatorService

# You have to define configs on your own
from configs import URL


if __name__ == "__main__":
    service = ImageFetcherService(URL, is_textbook=False)
    imgs_path, pdf_path = service.start()
    PDFCreatorService().create_pdf_from_png_images(pdf_path, imgs_path)
