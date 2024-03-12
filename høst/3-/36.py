telefonbok = {
		"Navn": "Arne", "Telefonnummeret": 22334455, 
        "Navn": "Lisa", "Telefonnummeret": 95959595,
        "Navn": "Jonas", "Telefonnummeret": 1234567
}

navn = input("Skriv et navn ")
if navn in telefonbok:
    print(telefonbok["Navn"]["Telefonnummeret"])