from flask import Flask, request, jsonify
import sqlite3
import json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import unittest


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite3:///users-vouchers.db'
DATABASE = 'users-vouchers.db'


conn = sqlite3.connect('users-vouchers.db')
cursor = conn.cursor()
users = cursor.execute("select * from user_info")
users_data = users.fetchall()


@app.route('/api/total_spent/<int:user_id>', methods=["GET"])
def money_spent(user_id):
    conn = sqlite3.connect('users-vouchers.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(money_spent) as total_spent FROM user_spending WHERE user_id = ?", [user_id])
    result = cursor.fetchone()
    print(result)
    if result is None:
        return jsonify({"message":"user not found"}),404
    return jsonify({"user_id": user_id, "total_spent": result["total_spent"]})


@app.route('/api/average_spending_by_age', methods=["GET"])
def get_average_spending_by_age():
    conn = sqlite3.connect('users-vouchers.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    age_ranges = [(18, 24), (25, 30), (31, 36), (37, 47), (48, None)]
    spending_data = []

    for start, end in age_ranges:
        if end:
            cursor.execute("""
                SELECT AVG(money_spent) AS avg_spending
                FROM user_spending
                JOIN user_info ON user_spending.user_id = user_info.user_id
                WHERE user_info.age BETWEEN ? AND ?
            """, (start, end))
        else:
            cursor.execute("""
                SELECT AVG(money_spent) AS avg_spending
                FROM user_spending
                JOIN user_info ON user_spending.user_id = user_info.user_id
                WHERE user_info.age >= ?
            """, (start,))

        result = cursor.fetchone()  # Use fetchone() as you are expecting a single result
        avg_spending = result['avg_spending'] if result['avg_spending'] is not None else 0  # Avoid None value

        spending_data.append({
            "age_range": f"{start}-{end}" if end else f"{start} and above",
            "avg_spending": avg_spending
        })

    if spending_data:
        return jsonify(spending_data), 200
    else:
        return jsonify({"message": "No data found"}), 404

@app.route('/write_high_spending_user', methods=['POST'])
def write_high_spending_user():
    data = request.get_json()
    user_id = data.get('user_id')
    total_spending = data.get('total_spending')

    if not user_id or not total_spending:
        return jsonify({"error": "Missing user_id or total_spending"}), 400

    conn = sqlite3.connect("users-vouchers.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO high_spenders (user_id, total_spending) VALUES (?, ?)""",
                       (user_id, total_spending))
    conn.commit()
    conn.close()

    return jsonify({"message": "User recorded successfully"}), 201


if __name__ == "__main__":
    app.run(debug=True)
