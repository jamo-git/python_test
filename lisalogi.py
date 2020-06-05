import logging

def kirjoitaToiseen(viesti):
    logger = logging.getLogger("tokalogger")
    logger.info("Toisesta loggerista viesti")
    logger.warning(viesti)