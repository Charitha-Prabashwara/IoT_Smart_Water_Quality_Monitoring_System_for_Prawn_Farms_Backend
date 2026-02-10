from .Repository import Repository

class BottomPressureRepository(Repository):

    def __init__(self):
        super().__init__()
        self._TABLENAME = "bottom_pressure"
        self._create_if_notExist()


   