class Setting():
    loaded = False

    def __init__(self):
        self.path = None
        self.debug = None

    def init(self):
        if Setting.loaded:
            return

        self.path = "./agent.log"
        self.debug = True
