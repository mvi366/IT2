# Program for reisekaranatene
 
land = "grønn"
vaksinert = True

# Dersom personen er vaksinert -> 0 dager
if vaksinert:
    print("0 dager")
# Dersom uvasinert og rød/oransj -> 10 dager
elif vaksinert == False and (land == "rød" or land == "oransje"):
    print("10 dager")

# Dersom uvaksinert og grønn -> 3 dager
elif vaksinert == False and land == "grønn":
    print("3 dager") 


def karantene(vaksinert, farge):
    if vaksinert:
        return 0 
    elif farge == "rød" or farge == "oransje":
        return 10
    elif farge == "grønn":
        return 3 


print(karantene(True, "rød"))
print(karantene(False, "rød"))


#if vaksinert == True:
 #   print("0 dager")
#else:
#    if land == "grønn":
#        print("3 dager")
#    elif land == "rød" or land == "oransje":
#        print("10 dager")
        
# a)  test programmer med de forskjell