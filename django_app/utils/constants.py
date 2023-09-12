from enum import Enum


class Status(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


API_URL='api/'