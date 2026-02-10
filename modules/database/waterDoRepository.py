from .Repository import Repository

class WaterDoRepository(Repository):

    def __init__(self):
        super().__init__()
        self._TABLENAME = "water_do"
        self._create_if_notExist()


   