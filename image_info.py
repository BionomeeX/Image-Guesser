from typing import List
from dataclasses import dataclass

@dataclass
class ImageInfo(object):
    image_url: str
    answers: List[str]
