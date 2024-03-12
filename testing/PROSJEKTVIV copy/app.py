from flask import Flask, render_template, request
import json

app = Flask(__name__)

fil_produkter = open("produkter.json")
produkter = json.load(fil_produkter)
fil_produkter.close()

fil_handlekurv = open("handlekurv.json")
handlekurv = json.load(fil_handlekurv)
fil_handlekurv.close()

fil_account = open("account.json")
account = json.load(fil_account)
fil_account.close()

def skriv_handlekurv():
    fil_handlekurv = open("handlekurv.json", "w")
    json.dump(handlekurv, fil_handlekurv)
    fil_handlekurv.close
    
def skriv_account():
    fil_account = open("account.json", "w")
    json.dump(account, fil_account)
    fil_account.close


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/shop")
def rute_shop():
    return render_template("shop.html", produkter=produkter)

@app.route("/produkt/<id>")
def rute_produkt(id):
    produkt = produkter[id]
    return render_template("produkt.html", id=id, produkt=produkt)

@app.route("/about")
def rute_about():
    return render_template("about.html")

@app.route("/shop/<type>")
def rute_sortering(type):
    sortert = {}
    for id, produkt in produkter.items():
        if type in produkt["type"]:
            sortert[id] = produkt
    return render_template("shop.html", produkter=sortert)

@app.route("/produkt/<id>/legg-til")
def rute_legg_til(id):
    handlekurv.append(id)
    skriv_handlekurv()
    return rute_produkt(id)

@app.route("/handlekurv")
def rute_handlekurv():
    return render_template("handlekurv.html", handlekurv=handlekurv, produkter=produkter)

@app.route("/handlekurv/slett/<id>")
def rute_slett(id):
    handlekurv.remove(id)
    skriv_handlekurv()
    return rute_handlekurv()

@app.route('/handlekurv-total')
def handlekurv_total():
    # Les handlekurv fra JSON-fil
    with open('handlekurv.json', 'r') as f:
        handlekurv = json.load(f)

    # Beregn totalpris for handlekurven
    total_price = 0
    for id, quantity in handlekurv.items():
        produkt = produkter[id]
        total_price += produkt["pris"] * quantity

    # Returner totalprisen som JSON-data
    return json.dumps({'total_price': total_price})


@app.route("/account", methods=["POST", "GET"])
def rute_account():
    if request.method == "POST":
        brukernavn = request.form["brukernavn"]
        passord = request.form["passord"]
        account.append({
            "brukernavn": brukernavn,
            "passord": passord
        })
        skriv_account()
    return render_template("account.html", account=account)

@app.route("/account/slett/<id>")
def rute_slettbruker(id):
    account.pop(int(id)+1)
    skriv_account()
    return rute_account()



app.run(debug=True)
