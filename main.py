from flask import Flask, render_template

import random


app = Flask(__name__)


max_score = 100

@app.get("/")
def index():
    return render_template("index.html")


@app.get("/menu/")
def menu():
    context = {
        "price": random.randint(15, 50),
        "discount": random.randint(0, 100)
    }
    return render_template("menu.html", **context)


@app.get("/contacts/")
def contacts():
    context = {
        "first_number": random.randint(101, 999),
        "second_number": random.randint(1001, 9999)
    }
    return render_template("contacts.html", **context)




if __name__ == "__main__":
    app.run()