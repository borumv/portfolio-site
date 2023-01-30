from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/<string:name_page>")
def main_page_second(name_page):
    return render_template(name_page)


@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_data_to_csv(data)
            return redirect("/thankyou.html")
        except:
            return "Error connect ot DB"
    else:
        return "Something wrong"


def write_data_to_db(data):
    with open("db.txt", mode='a') as m:
        email = data["email"]
        message = data["message"]
        subject = data["subject"]
        m.write(f'\n{email}, {message}, {subject}')


def write_data_to_csv(data):
    with open("db.csv", mode='a') as db:
        email = data["email"]
        message = data["message"]
        subject = data["subject"]
        csv_writer = csv.writer(db, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, message, subject])
