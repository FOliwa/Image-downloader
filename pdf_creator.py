import os
import re
import img2pdf


class PDFCreatorService():
        
    def create_pdf_from_png_images(self, pdf_file_path: str, imgs_dir_path: str):
        png_files = self.get_images(imgs_dir_path)

        with open(pdf_file_path, "wb") as f:
            pdf_bytes = img2pdf.convert(png_files)
            f.write(pdf_bytes)

    def get_images(self, imgs_dir_path: str) -> list[str]:
        img_files = os.listdir(imgs_dir_path)
        check_func = lambda x: re.match(r"\d{6}.png", x)
        return sorted([os.path.join(imgs_dir_path, f) for f in filter(check_func, img_files)])
