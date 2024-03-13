from dataclasses import dataclass
from datetime import datetime


@dataclass
class MongoDbObject:
    object_id: str


def mongo_id_parse(mdb_obj: MongoDbObject) -> datetime:
    if not mdb_obj or not mdb_obj.object_id:
        raise ValueError("Invalid mongo id, empty")

    if len(mdb_obj.object_id) == 24:
        timestamp = int(mdb_obj.object_id[:8], 16)
        return datetime.fromtimestamp(timestamp)

    raise ValueError("Invalid mongo id, not 24 characters")
