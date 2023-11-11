import zipfile

def extractor(file_path, destination="extracted"):
    with zipfile.ZipFile(file_path, 'r') as archive:
        archive.extractall(destination)

if __name__ == "__main__":
    extractor("Compress.zip")
