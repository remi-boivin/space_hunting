from enum import Enum

class Color(str, Enum):
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    INFO = '\033[92m'