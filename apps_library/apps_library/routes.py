from enum import Enum


class Route(Enum):
    INDEX = "/"
    TUTORIALS = "/tutoriales"

    PDF_UTILS = "/pdf_utils"
    IMAGE_UTILS = "/image_utils"
    TEXT_UTILS = "/text_utils"
    YT_DOWNLOADER = "/yt_downloader"
    GLOBAL_TIME = "/global_time"