- en måte å beskrive en algoritme eller et program på ved hjelp av naturlig språk
- brukes ofte som et verktøy for å planlegge og designe algoritmer før de faktisk blir kodet i et bestemt programmeringsspråk
- gjør det lettere å kommunisere og samarbeide med andre programmerere, samt å teste og feilsøke algoritmer før de blir kodet.
- en god måte å lære grunnleggende programmeringskonsepter på, da det kan hjelpe deg med å forstå hvordan ulike instruksjoner og logiske 
  uttrykk fungerer sammen for å løse et bestemt problem.

  ##eksempel: penger inn på spotify

  - en algoritme som regner ut hvor mye penger vi tjener på spotify
```pseudo

hent inn antall streams
hvis antall streams er større enn 30 000 000:
    returner antall streams gange 70% (0.7)
ellers hvis antall streams er større enn 1 400 000:
    returner antall streams gange 40% (0.4)
ellers:
    returner 0
```
```pseudo
SET antall_streams TO READ "hvor mange streams"
IF antall streams GREATER THAN 30 000 000
    THEN DISPLAY antall_Streams * 0.7
ELSE IF antall_streams GREATER THAN 1 400 000:
    THEN DISPLAY antall_streams * 0.4


```
```python
antall_streams = int(input("antall streams?"))
if antall_streams > 30 000 000:
    print(antall_streams * 0.7)
elif antall_streams > 1 400 000:
    print(antall_Streams * 0.4)
else:
    print(0)