import logging

def kirjoitaToiseen(viesti):
    logger = logging.getLogger("tokalogger")

    formatter = logging.Formatter("%(asctime)s  %(name)s  %(levelname)s: %(message)s")
    handler = logging.StreamHandler()
    logger.addHandler(handler)
    handler.setFormatter(formatter)
    logger.info("Toisesta loggerista viesti")
    logger.warning(viesti)
    logger.removeHandler(handler)