import concurrent.futures
import time
import platform
import requests

def teeajoa(odotus):
    print(f"Lähdin tekemään ajoa, odottaen {odotus} sekuntia")
    time.sleep(odotus)
    print(f"{platform.processor()} : {platform.architecture()}")
    return "Suoritettu arkkitehtuuri selvitys"

def ajatoista(osoite):
    print(f"Haetaan osoitetta {osoite}")
    res = requests.get(osoite)
    if res.status_code == 200:
        return(f"{osoite} haku kesti {res.elapsed.total_seconds()}")
    elif res.status_code == 404:
        return(f"{osoite} ei löydy")
    else:
        return(f"{osoite} haku ei onnistunut")

with concurrent.futures.ThreadPoolExecutor() as exec:
    fut = exec.submit(teeajoa, 1)
    print(fut.result())

    sivut = ["http://www.heroku.com", "http://www.google.fi", "http://www.iltalehti.fi",
        "http://www.microsoft.com", "http://www.apple.com", "http://www.funet.fi"]

    # results = [exec.submit(ajatoista, sivu) for sivu in sivut]
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

    results = exec.map(ajatoista, sivut)
    for result in results:
        print(result)