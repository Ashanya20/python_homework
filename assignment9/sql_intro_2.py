# Task 5
import sqlite3
import pandas as pd

db_path = "../db/lesson.db"

try:
    conn = sqlite3.connect(db_path)
    print("Connected to lesson.db")
    
    query = '''
        SELECT li.line_item_id, li.quantity, 
               p.product_id, p.product_name, p.price
        FROM line_items li
        JOIN products p ON li.product_id = p.product_id
    '''
    
    df = pd.read_sql_query(query, conn)
    print("\nFirst 5 rows of raw data:")
    print(df.head())
    
    df['total'] = df['quantity'] * df['price']
    print("\nAfter adding 'total' column (first 5 rows):")
    print(df.head())
    
    grouped = df.groupby('product_id').agg(
        count=('line_item_id', 'count'),
        total_sum=('total', 'sum'),
        product_name=('product_name', 'first')
    ).reset_index()
    
    print("\nGrouped data (first 5 rows):")
    print(grouped.head())
    
    grouped_sorted = grouped.sort_values('product_name')
    grouped_sorted.to_csv("order_summary.csv", index=False)
    print("\nSaved to order_summary.csv")
    
except Exception as e:
    print(f"Error: {e}")
finally:
    if conn:
        conn.close()