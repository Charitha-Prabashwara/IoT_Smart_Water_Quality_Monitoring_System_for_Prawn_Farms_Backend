from .Repository import Repository

class WaterTempRepository(Repository):

    def __init__(self):
        super().__init__()
        self._TABLENAME = "water_temp"
        self._create_if_notExist()


   