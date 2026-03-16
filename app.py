from flask import Flask, render_template, request, redirect, flash
from db import cursor, db

app = Flask(__name__)
app.secret_key = "expense_tracker_secret"

@app.route("/")
@app.route("/expenses")
def view_expenses():

    cursor.execute("""
        SELECT expenses.id, categories.name, amount, description, expense_date
        FROM expenses
        JOIN categories
        ON expenses.category_id = categories.id
        """)

    expenses = cursor.fetchall()

    cursor.execute("SELECT SUM(amount) AS total FROM expenses")

    total_expense = cursor.fetchone()["total"]

    return render_template(
        "expenses.html",
        expenses=expenses,
        total_expense=total_expense
    )

@app.route("/add", methods=["GET","POST"])
def add_expense():

    if request.method == "POST":

        category_id = request.form["category_id"]
        amount = request.form["amount"]
        description = request.form["description"]
        expense_date = request.form["expense_date"]

        cursor.execute("""
        INSERT INTO expenses (category_id, amount, description, expense_date)
        VALUES (%s,%s,%s,%s)
        """, (category_id, amount, description, expense_date))

        db.commit()

        flash("Expense added successfully!", "success")

        return redirect("/add")

    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()

    return render_template("add_expense.html", categories=categories)


@app.route("/summary")
def summary():

    # Category summary
    cursor.execute("""
        SELECT categories.name, SUM(amount) as total
        FROM expenses
        JOIN categories
        ON expenses.category_id = categories.id
        GROUP BY categories.name
    """)
    summary = cursor.fetchall()


    # Today
    cursor.execute("""
        SELECT SUM(amount) as total_today
        FROM expenses
        WHERE expense_date = CURDATE()
    """)
    today_total = cursor.fetchone()["total_today"] or 0


    # This month
    cursor.execute("""
        SELECT SUM(amount) as total_month
        FROM expenses
        WHERE MONTH(expense_date) = MONTH(CURDATE())
        AND YEAR(expense_date) = YEAR(CURDATE())
    """)
    month_total = cursor.fetchone()["total_month"] or 0


    # This year
    cursor.execute("""
        SELECT SUM(amount) as total_year
        FROM expenses
        WHERE YEAR(expense_date) = YEAR(CURDATE())
    """)
    year_total = cursor.fetchone()["total_year"] or 0


    overall_total = sum(row["total"] for row in summary)


    return render_template(
        "summary.html",
        summary=summary,
        overall_total=overall_total,
        today_total=today_total,
        month_total=month_total,
        year_total=year_total
    )

@app.route("/delete/<int:id>")
def delete_expense(id):

    cursor.execute("DELETE FROM expenses WHERE id=%s", (id,))
    db.commit()

    return redirect("/")

@app.route("/edit/<int:id>", methods=["GET","POST"])
def edit_expense(id):

    if request.method == "POST":

        category_id = request.form["category_id"]
        amount = request.form["amount"]
        description = request.form["description"]
        expense_date = request.form["expense_date"]

        cursor.execute("""
        UPDATE expenses
        SET category_id=%s, amount=%s, description=%s, expense_date=%s
        WHERE id=%s
        """, (category_id, amount, description, expense_date, id))

        db.commit()

        return redirect("/")

    cursor.execute("SELECT * FROM expenses WHERE id=%s", (id,))
    expense = cursor.fetchone()

    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()

    return render_template(
        "edit_expense.html",
        expense=expense,
        categories=categories
    )

if __name__ == "__main__":
    app.run(debug=True)