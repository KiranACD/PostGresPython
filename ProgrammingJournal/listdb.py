class ListDb:
    # __instance = None
    # @staticmethod
    # def get_instance():
    #     if ListDb.__instance is None:
    #         return ListDb()
    #     return ListDb.__instance
    def __init__(self):
        pass
    def connect(self):
        self.dblist = []
    def insert(self, entry):
        self.dblist.append(entry.__dict__)
    def fetch(self):
        return self.dblist
