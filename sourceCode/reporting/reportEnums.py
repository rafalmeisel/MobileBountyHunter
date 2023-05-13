from enum import Enum

class UrlResourceSecurityStatus(Enum):
    SECURED = 1
    VULNERABLE = 2
    TO_VERIFY = 3
    FOUND = 4
    NOT_FOUND = 5