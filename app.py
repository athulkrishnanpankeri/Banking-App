from flask import Flask, render_template, request, redirect
from db import create_table, add_transaction, view_transactions

app = Flask(__name__)
create_table()  # Ensure DB is ready on launch

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

@app.route('/transactions')
def transactions():
    trans_type = request.args.get('type')
    category = request.args.get('category')
    rows = view_transactions(trans_type, category)
    return render_template('transactions.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
