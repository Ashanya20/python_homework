# advanced_sql.py – Tasks 1 and 2
import sqlite3

db_path = "../db/lesson.db"

def task1():
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        query = """
            SELECT o.order_id, SUM(li.quantity * p.price) AS total_price
            FROM orders o
            JOIN line_items li ON o.order_id = li.order_id
            JOIN products p ON li.product_id = p.product_id
            GROUP BY o.order_id
            ORDER BY o.order_id
            LIMIT 5
        """
        cursor.execute(query)
        results = cursor.fetchall()
        print("\n--- Task 1: First 5 orders total price ---")
        print("Order ID | Total Price")
        for row in results:
            print(f"{row[0]}        | ${row[1]:.2f}")
    except sqlite3.Error as e:
        print(f"Task 1 error: {e}")
    finally:
        if conn:
            conn.close()

def task2():
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        query = """
            SELECT c.customer_name, AVG(sub.total_price) AS average_total_price
            FROM customers c
            LEFT JOIN (
                SELECT o.customer_id AS customer_id_b, SUM(li.quantity * p.price) AS total_price
                FROM orders o
                JOIN line_items li ON o.order_id = li.order_id
                JOIN products p ON li.product_id = p.product_id
                GROUP BY o.order_id
            ) sub ON c.customer_id = sub.customer_id_b
            GROUP BY c.customer_id
            ORDER BY c.customer_name
        """
        cursor.execute(query)
        results = cursor.fetchall()
        print("\n--- Task 2: Average order price per customer ---")
        print("Customer Name               | Average Total Price")
        for row in results:
            name = row[0]
            avg_price = row[1] if row[1] is not None else 0.0
            print(f"{name:<25} | ${avg_price:.2f}")
    except sqlite3.Error as e:
        print(f"Task 2 error: {e}")
    finally:
        if conn:
            conn.close()

def task3():
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()
        
        # Get customer_id for "Perez and Sons"
        cursor.execute("SELECT customer_id FROM customers WHERE customer_name = ?", ("Perez and Sons",))
        customer_row = cursor.fetchone()
        if not customer_row:
            print("Customer 'Perez and Sons' not found.")
            return
        customer_id = customer_row[0]
        
        # Get employee_id for "Miranda Harris"
        cursor.execute("SELECT employee_id FROM employees WHERE first_name = ? AND last_name = ?", ("Miranda", "Harris"))
        emp_row = cursor.fetchone()
        if not emp_row:
            print("Employee Miranda Harris not found.")
            return
        employee_id = emp_row[0]
        
        # Get the 5 least expensive products
        cursor.execute("SELECT product_id FROM products ORDER BY price LIMIT 5")
        product_rows = cursor.fetchall()
        if len(product_rows) != 5:
            print("Could not fetch 5 products.")
            return
        product_ids = [row[0] for row in product_rows]
        
        # Begin transaction
        conn.execute("BEGIN")
        
        # Insert new order
        cursor.execute("""
            INSERT INTO orders (customer_id, employee_id)
            VALUES (?, ?)
            RETURNING order_id
        """, (customer_id, employee_id))
        order_id = cursor.fetchone()[0]
        
        # Insert 5 line items (quantity 10)
        for pid in product_ids:
            cursor.execute("""
                INSERT INTO line_items (order_id, product_id, quantity)
                VALUES (?, ?, ?)
            """, (order_id, pid, 10))
        
        # Commit transaction
        conn.commit()
        
        # Now retrieve and print the line items for this order
        query = """
            SELECT li.line_item_id, li.quantity, p.product_name
            FROM line_items li
            JOIN products p ON li.product_id = p.product_id
            WHERE li.order_id = ?
            ORDER BY li.line_item_id
        """
        cursor.execute(query, (order_id,))
        items = cursor.fetchall()
        
        print("\n--- Task 3: New order for Perez and Sons ---")
        print(f"Order ID: {order_id}")
        print("Line Item ID | Quantity | Product Name")
        for row in items:
            print(f"{row[0]}            | {row[1]}        | {row[2]}")
            
    except sqlite3.Error as e:
        print(f"Task 3 error: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

def task4():
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        query = """
            SELECT e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) AS order_count
            FROM employees e
            JOIN orders o ON e.employee_id = o.employee_id
            GROUP BY e.employee_id
            HAVING COUNT(o.order_id) > 5
            ORDER BY order_count DESC
        """
        cursor.execute(query)
        results = cursor.fetchall()
        print("\n--- Task 4: Employees with more than 5 orders ---")
        print("Employee ID | First Name | Last Name | Order Count")
        for row in results:
            print(f"{row[0]}           | {row[1]}      | {row[2]}       | {row[3]}")
    except sqlite3.Error as e:
        print(f"Task 4 error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    task1()
    task2()
    task3()
    task4()