def mongo_id_parse(_id: str):
    from datetime import datetime

    if not _id:
        raise Exception("Empty _id string")

    if len(_id) == 24:
        timestamp = int(_id[:8], 16)
        return datetime.fromtimestamp(timestamp)

    raise Exception("Invalid mongo id")
