class EchoBase:
    def __init__(self, name: str, set : str, cost: int, main_stat : str, main_stat_value : int, substats : list):
        self.name = name
        self.set = set
        self.cost = cost
        self.main_stat = main_stat
        self.main_stat_value = main_stat_value
        self.substats = substats