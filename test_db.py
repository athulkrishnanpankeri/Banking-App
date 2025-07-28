from db import create_table, add_transaction, view_transactions

if __name__ == "__main__":
    create_table()

    # Add some test data
    add_transaction('2025-07-25', 'Salary', 2500.00, 'Income', 'Work')
    add_transaction('2025-07-26', 'Groceries', 55.50, 'Expense', 'Food')
    add_transaction('2025-07-27', 'Internet Bill', 40.00, 'Expense', 'Utilities')

    # View all transactions
    view_transactions()
