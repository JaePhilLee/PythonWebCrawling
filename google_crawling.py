from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

arguments = {"keywords":"flame scene on inside, flame scene", "limit":200,"print_urls":True, "format":"jpg", "chromedriver": "./chromedriver"}
paths = response.download(arguments)
print(paths)
