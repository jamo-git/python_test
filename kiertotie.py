

class Kiertotie():
    def __init__(self, logger):
        self.logger = logger

    def palautaTie(self):
        self.logger.error("En katastrof")
        return "Och människör"

def toinenTie(logger):
    logger.debug("Inte alls")
    return "Va fan"