import logging
import time
from start_program import ajoituslaskenta


def kirjoitaToiseen(viesti):
    aloitus = time.perf_counter()
    logger = logging.getLogger("tokalogger")

    formatter = logging.Formatter("%(asctime)s  %(name)s  %(levelname)s: %(message)s")
    handler = logging.StreamHandler()
    logger.addHandler(handler)
    handler.setFormatter(formatter)
    logger.info("Toisesta loggerista viesti")
    logger.warning(viesti)
    logger.removeHandler(handler)
    lopetus = time.perf_counter()

    print("kirjoitaToiseen kesti: " + ajoituslaskenta(aloitus, lopetus))
