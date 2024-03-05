# Modul reclamacions en Odoo
## Grup2 Eric Ortega Joan Chortó



### Atributs del modul
* Un títol
###
* Una descripció de la resolució final de la reclamació

###
* Client que fa la reclamació
###

* Usuari que crea la reclamació
###

*  Data de creació, data de modificació i data de tancament.
###

* La comanda de vendes associada a la reclamació

###

* Una descripció inicial de la reclamació.
###

*  Una llista de missatges, on a més del text del missatge, per a cadascun s’ha
d’indicar quin és l’autor (pot ser un usuari d’Odoo o el client) i la data del missatge.
Una vegada el missatge s’ha creat, no es pot modificar ni esborrar.
###

* El nombre de factures i enviaments associats a la comanda
###

* Un estat que pot ser: nova (en el moment de creació), en tractament (quan hi ha
almenys un missatge), tancada (quan està resolta) i cancel·lada (quan no s’ha de
continuar amb la resolució)

###
* Una descripció de la resolució final de la reclamació

###
*  Un motiu de tancament o cancel·lació a seleccionar d’una llista de valors. Els valors
hauran de poder-se gestionar des d’un menú específic, no es poden crear valors des
del mateix llistat.


### Acions a realitzar

* Tancar tiquet
###
* Cancel·lar tiquet
###
* Reobrir tiquet
###
* Cancel·lar la comanda de venda associada.

### En cas de cancelacio de la comanda
* Alertar l’usuari si existeixen factures publicades associades a la comanda abans de
procedir a cancel·lar
###
* Enviar un correu al client informant de la cancel·lació de la comanda. Aquest correu
ha de quedar registrat a l’historial de la comanda.
###
* Cancel·lar la comanda, les factures associades no publicades i els enviaments no
fets.


