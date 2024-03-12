# serie.py
class Serie:
    def __init__(self, navn):
        self.navn = navn
        self.lag = []

    def hent_navn(self):
        return self.navn

    def hent_lagliste(self):
        return self.lag

    def legg_til_lag(self, lag):
        self.lag.append(lag)

    def spill_kamp(self, hjemmelag, bortelag, bortemål, hjemmemål):
        # Implementer logikken for å avgjøre vinneren av kampen her
        pass

    def finn_spiller(self, navn):
        for lag in self.lag:
            spiller = lag.finn_spiller(navn)
            if spiller:
                return spiller
        return None