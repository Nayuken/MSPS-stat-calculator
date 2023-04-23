import json

from flask import Flask, render_template, request,session
import weaponformulas

app= Flask(__name__)

"""index page"""
@app.route("/", methods = ["GET", "POST"])
def index():
    range = {}
    if request.method == "POST":
        web_str = int(request.form.get("str"))
        web_dex = int(request.form.get("dex"))
        web_int = int(request.form.get("int"))
        web_luk = int(request.form.get("luk"))
        web_wpattk = int(request.form.get("wp_attk"))
        web_wptype = str(request.form.get("weapon_type"))
        web_throwable = str(request.form.get("throwable"))

        castella = weaponformulas.Weaponformula(web_str, web_dex, web_int,
                                                web_luk, web_wpattk,
                                                web_wptype,web_throwable)
        range = {"Range": castella.weapon_calc()}
    calculation = json.dumps(range)
    return render_template('index.html', calculation=calculation)


@app.route("/spells", methods = ["GET", "POST"])
def spells():
    return render_template('spells.html')