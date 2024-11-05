from flask import Flask, render_template, request, redirect, url_for, jsonify
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from io import BytesIO
import base64

app = Flask(__name__)

CSV_FILE = "finance_data.csv"

# Route to render home page
@app.route('/')
def index():
    df = pd.read_csv(CSV_FILE)
    income = df[df['category'] == 'Income']['amount'].sum()
    expense = df[df['category'] == 'Expense']['amount'].sum()
    net_worth = income - expense
    img = generate_graph(df)
    return render_template('index.html', income=income, expense=expense, net_worth=net_worth, graph=img)

# Route to add a new transaction
@app.route('/add', methods=['POST'])
def add_transaction():
    data = {
        "date": request.form['date'],
        "amount": float(request.form['amount']),
        "category": request.form['category'],
        "description": request.form['description']
    }
    add_entry(data)
    return redirect(url_for('index'))

# Function to add new entry to CSV
def add_entry(data):
    df = pd.read_csv(CSV_FILE)
    df = df._append(data, ignore_index=True)
    df.to_csv(CSV_FILE, index=False)

# Function to generate graph
def generate_graph(df):
    plt.figure(figsize=(10, 5))
    df['date'] = pd.to_datetime(df['date'], format="%d-%m-%Y")
    df = df.sort_values('date')
    
    income = df[df['category'] == 'Income']
    expenses = df[df['category'] == 'Expense']
    
    plt.plot(income['date'], income['amount'].cumsum(), label="Income")
    plt.plot(expenses['date'], expenses['amount'].cumsum(), label="Expenses", color="red")
    
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expenses Over Time")
    plt.legend()

    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    img_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    buf.close()
    return f"data:image/png;base64,{img_base64}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
