

from flask import Flask, render_template, request, redirect
from db import create_table, add_transaction, view_transactions

app = Flask(__name__)
create_table()  # Ensure DB is ready on launch
app.secret_key = "supersecretkey"  # Needed for flashing messages

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        date = request.form['date']
        desc = request.form['description']
        amount = float(request.form['amount'])
        trans_type = request.form['transaction_type']
        category = request.form['category']
        add_transaction(date, desc, amount, trans_type, category)
        return redirect('/transactions')
    return render_template('add.html')

from flask import Flask, render_template, request, redirect, flash
from datetime import datetime

@app.route("/add", methods=["GET", "POST"])
def add_transaction_route():
    if request.method == "POST":
        date = request.form.get("date")
        desc = request.form.get("description")
        amount = request.form.get("amount")
        ttype = request.form.get("type")
        category = request.form.get("category")

        # --- Backend Validation ---
        try:
            # Validate date
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            flash("Invalid date format. Use YYYY-MM-DD.")
            return redirect("/add")

        if not desc or not category:
            flash("Description and category cannot be empty.")
            return redirect("/add")

        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError
        except ValueError:
            flash("Amount must be a number greater than zero.")
            return redirect("/add")

        if ttype not in ["Income", "Expense"]:
            flash("Transaction type must be Income or Expense.")
            return redirect("/add")

        # Save to DB if valid
        add_transaction(date, desc, amount, ttype, category)
        flash("Transaction added successfully.")
        return redirect("/transactions")

    return render_template("add.html")

