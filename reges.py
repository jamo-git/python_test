# coding: utf-8

import re

mailit = """
joku.tyyppi@kutumail.next
toka-ukko12@niksula.net
vika_akka@tokosla.cu
"""

ehto = re.compile(r"([a-zA-Z0-9._-]+)@([a-zA-Z-]+\.\w+)")

tulokset = ehto.finditer(mailit)

for tulos in tulokset:
    print(tulos.span(), tulos.group())

kayttajat = ehto.sub(r"\1", mailit)
domainit = ehto.sub(r"\2", mailit)

print(kayttajat)
print(domainit)
