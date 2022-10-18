from flask import Flask, render_template, redirect, request
from helper import update_csv, get_csv, remove_stock, change_time


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        symbol = request.form.get("symbol")
        update_csv(symbol)

        dates, namePrice = get_csv()
        names = [i for i in namePrice]
        time_period = map(str.title, ["5d", "1m", "6m", "1y", "10y"])

        return render_template(
            "index.html", dates=dates, namePrice=namePrice, names=names, time_period=time_period,
            )
    else:
        dates, namePrice = get_csv()
        names = [i for i in namePrice]
        time_period = map(str.title, ["5d", "1m", "6m", "1y", "10y"])

        return render_template(
            "index.html", dates=dates, namePrice=namePrice, names=names, time_period=time_period,
            )


@app.route("/remove", methods=["POST"])
def remove():
    symbol = request.form.get("symbol")
    remove_stock(symbol)
    return redirect('/')


@app.route("/time", methods=["POST"])
def time():
    time = request.form.get("time")
    change_time(time)
    return redirect('/')

