from .Repository import Repository

class WaterTDSRepository(Repository):

    def __init__(self):
        super().__init__()
        self._TABLENAME = "water_tds"
        self._create_if_notExist()


   