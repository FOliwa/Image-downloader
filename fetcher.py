import os
import re
import requests


class ImageFetcherService():

    def __init__(self, url) -> None:
        self.url = url
        self.image_path = None
        self.current_image = None
        self.pdf_dir_path = None
        self.pdf_file_name = None


    def get_data_from_link(self):
        img_num_pattern = r"\b\d{6}\b"
        document_name_pattern = r"\w+-\w{2}-\w+"

        document_name = re.findall(document_name_pattern, self.url).pop()
        module_name, chapter_idx, chapter_name  = document_name.split("-")
        chapter_name = re.sub("_pdf", "", chapter_name)
        
        self.current_image = re.findall(img_num_pattern, self.url).pop()
        self.image_path = f"./assets/images/{module_name}/{chapter_idx}/{chapter_name}"
        self.pdf_dir_path = f"./assets/pdfs/{module_name}/{chapter_idx}"
        self.pdf_file_path = self.pdf_dir_path + "/" + chapter_name + ".pdf"

    def start(self):
        print("[LOG] Start Fetching")
        self.get_data_from_link()
        self.create_directory_structure()
        for i in range(0, 500):
            if self.img_already_saved():
                print(f"[LOG] Image already saved! {self.image_path}/{self.current_image}.png")
            else:
                print(f"[LOG] Request the image! Index: {self.current_image}")
                response = requests.get(self.url)
                if response.status_code == 200:
                    self.save_image(response.content)
                elif response.status_code == 404:
                    print(f"[LOG] There is no image {self.current_image}! Status code 404.")
                    print(f"[LOG] End Fetching. Downloaded images: {i}")
                    return self.image_path, self.pdf_file_path
            self.update_url()

    def img_already_saved(self):
        return self.current_image+".png" in os.listdir(self.image_path) 

    def update_url(self):
        val = int(self.current_image) + 1
        old_number = self.current_image
        self.current_image = str(val).zfill(len(self.current_image))
        self.url = re.sub(old_number, self.current_image, self.url)

    def save_image(self, image_data):
        path = self.image_path + "/" + self.current_image + ".png"
        if self._you_are_in_good_dir():
            with open(path, "wb") as image_file:
                image_file.write(image_data)
        else:
            # TODO: ADD decorator wrapper for it - as you will use it few times
            raise Exception("[LOG] Wrong path! Run the program in main project directory!")

    def create_directory_structure(self):
        if self._you_are_in_good_dir():
            os.makedirs(self.image_path, exist_ok=True)
            os.makedirs(self.pdf_dir_path, exist_ok=True)
        else:
            # TODO: ADD decorator wrapper for it - as you will use it few times
            raise Exception("Wrong path! Run the program in main project directory!")

    def _you_are_in_good_dir(self):
        current_path = os.getcwd()
        return os.path.basename(current_path) == "hu-pdf-generator"
