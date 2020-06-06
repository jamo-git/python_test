import logging
import kiertotie as kt
import os.path
import multiprocessing
import time
import lisalogi
import time

'''
Python testi logitukselle sekä OOP
'''

logging.basicConfig(filename="application.log", filemode="w", 
    format="%(asctime)s  %(name)s  %(levelname)s: %(message)s", level=logging.DEBUG)

class Myyja():
    def __init__(self, sukupuoli, ika, palkka):
        self.sukupuoli = sukupuoli
        self.ika = ika
        self.palkka = palkka
    
    def korotaPalkka(self):
        if self.sukupuoli == "mies":
            self.palkka *= 1.05
        else:
            self.palkka *= 1.02
    
    def vanheta(self):
        self.ika += 1

class Kauppa():
    def __init__(self, Myyja, nimi, katalogi=None):
        self.Myyja = Myyja
        self.nimi = nimi
        if katalogi is None:
            self.katalogi = []
        else:
            self.katalogi = katalogi
    
    def listaaTuotteet(self):
        return self.katalogi
    
    def kerroMyyjanPalkka(self):
        return self.Myyja.palkka

    def myyTuote(self, tuote):
        if tuote in self.katalogi:
            self.katalogi.remove(tuote)
            self.Myyja.korotaPalkka()
            return "Tuote myyty ja palkka korotettu"
        else:
            logging.warning("Ei löydy")
            return "Pieleen meni"

    def taydennaTuotteet(self, tuote):
        self.katalogi.append(tuote)

def alustaLogi():
    if os.path.exists("./application.log"):
        print("Logi application.log löytyy")
    
    return logging.getLogger("jehu")

def toinenProsessi():
    logging.error("Kirjoitus toisesta prosessista")

def ajoituslaskenta(aloitus, lopetus):
    kesti = lopetus - aloitus
    return str(round(kesti,3))

if __name__ == "__main__":

    mainlog = alustaLogi()
    moniajolog = logging.getLogger("moniajo")

    logging.info("Tästä se alkaa")

    aloitus_aika = time.perf_counter()
    
    miesAki = Myyja("mies", 24, 2500)
    naisAnna = Myyja("nainen", 32, 3200)

    verkkis = Kauppa(miesAki, "Verkkokauppa", ["Hiiri", "Naytto", "Tietokone"])
    siwa = Kauppa(naisAnna, "Siwa", ["Olut", "Leipa", "Maito"])

    lopetus_aika = time.perf_counter()
    print("Myyjän ja kaupan luonti kesti: " + ajoituslaskenta(aloitus_aika, lopetus_aika))

    mainlog.info("Myyjät ja kaupat luotu")

    prosessi = multiprocessing.Process(target=toinenProsessi)
    prosessi.start()

    luokka = kt.LuokkaProsessi(moniajolog)
    luokkapros = multiprocessing.Process(target=luokka.kirjoitaLogiin)
    luokkapros.run()

    tie = kt.Kiertotie(moniajolog)
    viesti = tie.palautaTie()
    logging.critical(viesti)
    kt.toinenTie(moniajolog)

    lisalogi.kirjoitaToiseen("Pääjehu kutsuu toista loggeria")

    proslisalog = multiprocessing.Process(target=lisalogi.kirjoitaToiseen, args=("Tokalogi toinen pros",))
    proslisalog.start()

    logging.info(verkkis.listaaTuotteet())
    logging.debug(verkkis.kerroMyyjanPalkka())
    logging.info(verkkis.myyTuote("Hiiri"))
    logging.info(verkkis.listaaTuotteet())
    logging.debug(verkkis.kerroMyyjanPalkka())

    verkkis.taydennaTuotteet("Prossu")
    logging.debug(verkkis.listaaTuotteet())




