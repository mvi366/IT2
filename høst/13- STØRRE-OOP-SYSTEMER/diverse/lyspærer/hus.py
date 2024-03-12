#lag en husklasse som inneholder rom
#lag legg_til_rom
#lag skru_av_strøm som skrur av alle lys i hele huset
#

from rom import Rom
from lyspære import Lyspære

class Hus():
    def __init__(self) -> None:
        self._rom: list[Rom] = []
    
    def legg_tid_rom(self, rom):
        self._rom.append(rom)
    
    def skru_av_strøm(self):
        for rom in self._rom:
            rom.skru_av_lys()

        

