import logging
import kiertotie as kt
import os.path
import multiprocessing
import time

'''
Python testi logitukselle sekä OOP
'''

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
    def __init__(self, Myyja, nimi, katalogi):
        self.Myyja = Myyja
        self.nimi = nimi
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
        print("Ohnose")
    logging.basicConfig(filename="application.log", filemode="w", 
    format="%(name)s - %(levelname)s - %(message)s", level=logging.DEBUG)

def toinenProsessi():
    logging.error("Kirjoitus toisesta prosessista")
    print("Toka prosari kirjoitti")

if __name__ == "__main__":
    alustaLogi()
    logging.info("Tästä se alkaa")

    miesAki = Myyja("mies", 24, 2500)
    naisAnna = Myyja("nainen", 32, 3200)
    verkkis = Kauppa(miesAki, "Verkkokauppa", ["Hiiri", "Naytto", "Tietokone"])
    siwa = Kauppa(naisAnna, "Siwa", ["Olut", "Leipa", "Maito"])

    logging.info("Myyjät ja kaupat luotu")

    prosessi = multiprocessing.Process(target=toinenProsessi)
    prosessi.start()

    luokka = kt.LuokkaProsessi(logging)
    luokkapros = multiprocessing.Process(target=luokka.kirjoitaLogiin)
    luokkapros.run()

    tie = kt.Kiertotie(logging)
    viesti = tie.palautaTie()
    logging.debug(viesti)
    kt.toinenTie(logging)

    print("Pääprosessi kirjoitti")

    logging.info(verkkis.listaaTuotteet())
    logging.debug(verkkis.kerroMyyjanPalkka())
    logging.info(verkkis.myyTuote("Hiiri"))
    logging.info(verkkis.listaaTuotteet())
    logging.debug(verkkis.kerroMyyjanPalkka())

    verkkis.taydennaTuotteet("Prossu")
    logging.debug(verkkis.listaaTuotteet())




