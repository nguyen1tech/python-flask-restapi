import enum


class Op(enum.Enum):
    NO_OP = 1
    INSERT = 2
    UPDATE = 3
    DELETE = 4


class InsertResult:
    def __init__(self, inserted: int = 0, exists: bool = True):
        self.op = Op.INSERT
        self.inserted = inserted
        self.exists = exists


class DeleteResult:

    def __init__(self, deleted: int = 0, exists=True):
        self.op = Op.DELETE
        self.deleted = deleted
        self.exists = exists
