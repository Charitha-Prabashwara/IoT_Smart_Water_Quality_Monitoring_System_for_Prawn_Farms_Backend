from .Repository import Repository

class WaterTurbidityRepository(Repository):

    def __init__(self):
        super().__init__()
        self._TABLENAME = "water_turbidity"
        self._create_if_notExist()


   