from enum import Enum

class UrlResourceSecurityStatus(Enum):
    IS_SECURE = 1
    IS_VULNERABLE = 2
    TO_VERIFY = 3
    NOT_FOUND = 4