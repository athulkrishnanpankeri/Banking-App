from flask import Flask, render_template, request, redirect
from db import create_table, add_transaction, view_transactions

app = Flask(__name__)

@app.before_first_request
def init():
    create_table()

@app.route('/')
def home():
    return redirect('/view')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = request.form
        add_transaction(
            data['date'],
            data['description'],
            float(data['amount']),
            data['type'],
            data['category']
        )
        return redirect('/view')
    return render_template('add_transaction.html')

@app.route('/view')
def view():
    trans_type = request.args.get('type')
    category = request.args.get('category')
    transactions = view_transactions(trans_type, category)
    return render_template('view_transactions.html', transactions=transactions)

if __name__ == '__main__':
    app.run(debug=True)
