from flask import Flask, render_template, request, flash, redirect, url_for
from calculations import calculate_bmi, calculate_bmr

app = Flask(__name__)
app.secret_key = "yoursecretkey"  # needed for flash messages

@app.route('/')
def main_page():
    return render_template("index.html")

@app.route("/Kalkulaator")
def kalkulaator():
    return render_template("kalkulaator.html")

@app.route("/Kalkulaator/bmi", methods=["POST"])
def bmi_calc():
    height = request.form.get("height", "")
    weight = request.form.get("weight", "")
    bmi, status = calculate_bmi(float(height), float(weight))
    return render_template(
        "kalkulaator.html",
        bmi=bmi,
        bmi_status=status,
        height_val=height,
        weight_val=weight
    )

@app.route("/Kalkulaator/bmr", methods=["POST"])
def bmr_calc():
    age = request.form.get("age", "")
    gender = request.form.get("gender", "")
    height = request.form.get("height", "")
    weight = request.form.get("weight", "")
    bmr = calculate_bmr(int(age), gender, float(height), float(weight))
    return render_template(
        "kalkulaator.html",
        bmr=bmr,
        age_val=age,
        gender_val=gender,
        height2_val=height,
        weight2_val=weight
    )

@app.route("/Kontakt", methods=["GET", "POST"])
def kontakt():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # For now, just print to console (later can save to DB or send email)
        print(f"Contact from {name} <{email}>: {message}")

        flash("Aitäh, sinu sõnum on saadetud!")
        return redirect(url_for("kontakt"))

    return render_template("contact.html")

@app.route('/Minust')
def Minust():
    return render_template("about.html")

if __name__ == "__main__":
    app.run()
