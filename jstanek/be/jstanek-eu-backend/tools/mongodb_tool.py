from datetime import datetime


def mongo_id_parse(_id: str):

    if not _id:
        raise ValueError("Invalid mongo id, empty")

    if len(_id) == 24:
        timestamp = int(_id[:8], 16)
        return datetime.fromtimestamp(timestamp)

    raise ValueError("Invalid mongo id, not 24 characters")
