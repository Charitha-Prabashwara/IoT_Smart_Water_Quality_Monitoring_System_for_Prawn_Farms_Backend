from .Repository import Repository

class PhRepository(Repository):

    def __init__(self):
        super().__init__()
        self._TABLENAME = "ph"
        self._create_if_notExist()


   