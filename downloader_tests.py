import os
import pytest
import downloader
from Exceptions import *


def test_download_picture_jpg():
    url = 'https://images.freeimages.com/images/large-previews/8b1/cat-1525070.jpg'
    result = downloader.download_picture(url)
    assert result == url.split('/')[-1]
    assert os.path.exists(f"{downloader.destination_folder}/{result}")
    os.remove(f"{downloader.destination_folder}/{result}")


def test_download_picture_with_not_accepted_extension():
    url = 'https://upload.wikimedia.org/wikipedia/commons/a/a1/Johnrogershousemay2020.webp'
    with pytest.raises(FileTypeError):
        result = downloader.download_picture(url)


def test_download_picture_with_bad_url():
    url = 'https://upload.wikimedia.org/wik WRONG STUFF a/commons/a/a1/Johnrogershousemay2020.jpg'
    with pytest.raises(FileRetrievalException):
        result = downloader.download_picture(url)


def test_download_picture_with_no_extension_checking():
    url = 'https://upload.wikimedia.org/wikipedia/commons/a/a1/Johnrogershousemay2020.webp'
    result = downloader.download_picture(url, check_for_file_extension=False)
    assert result == url.split('/')[-1]
    assert os.path.exists(f"{downloader.destination_folder}/{result}")
    os.remove(f"{downloader.destination_folder}/{result}")


def test_download_picture_with_added_extension():
    url = 'https://upload.wikimedia.org/wikipedia/commons/a/a1/Johnrogershousemay2020.webp'
    downloader.add_accepted_extension("webp")
    result = downloader.download_picture(url)
    assert result == url.split('/')[-1]
    assert os.path.exists(f"{downloader.destination_folder}/{result}")
    os.remove(f"{downloader.destination_folder}/{result}")


def test_download_picture_as_jpg():
    url = 'https://images.freeimages.com/images/large-previews/8b1/cat-1525070.jpg'
    result = downloader.download_picture_as(url, "catpic")
    assert result == "catpic.jpg"
    assert os.path.exists(f"{downloader.destination_folder}/{result}")
    os.remove(f"{downloader.destination_folder}/{result}")


def test_download_picture_as_webp_as_jpeg():
    url = 'https://upload.wikimedia.org/wikipedia/commons/a/a1/Johnrogershousemay2020.webp'
    result = downloader.download_picture_as(url, "house", False, "jpeg")
    assert result == "house.jpeg"
    assert os.path.exists(f"{downloader.destination_folder}/{result}")
    os.remove(f"{downloader.destination_folder}/{result}")