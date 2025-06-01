import sqlite3
import os
from pathlib import Path


def initialize_database():
    # Database papkasini yaratish
    db_dir = Path("./Database")
    db_dir.mkdir(exist_ok=True)

    # Database bilan ulanish
    db_path = db_dir / "AutoShop.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 1. Parts_Category jadvali
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Parts_Category (
        parts_id TEXT PRIMARY KEY,
        parts_name TEXT NOT NULL,
        type TEXT NOT NULL,
        discount REAL,
        in_stock INTEGER NOT NULL,
        parts_price REAL NOT NULL
    )
    """)

    # 2. Admin_Account jadvali
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Admin_Account (
        admin_id TEXT PRIMARY KEY,
        admin_fullname TEXT NOT NULL,
        admin_username TEXT NOT NULL,
        admin_password TEXT NOT NULL
    )
    """)

    # 3. Employee_Account jadvali
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Employee_Account (
        employee_id TEXT PRIMARY KEY,
        employee_fullname TEXT NOT NULL,
        employee_username TEXT NOT NULL,
        employee_password TEXT NOT NULL
    )
    """)

    # 4. Guest_Account jadvali
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Guest_Account (
        guest_id TEXT PRIMARY KEY,
        guest_fullname TEXT NOT NULL,
        guest_username TEXT NOT NULL,
        guest_password TEXT NOT NULL
    )
    """)

    # 5. Inventory jadvali (cheklar uchun)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Inventory (
        bill_number TEXT PRIMARY KEY,
        date TEXT NOT NULL,
        cashier_name TEXT NOT NULL,
        contact TEXT NOT NULL,
        bill_details TEXT NOT NULL
    )
    """)

    # Dastur uchun boshlang'ich ma'lumotlar
    # Admin hisobi (agar mavjud bo'lmasa)
    cursor.execute("SELECT * FROM Admin_Account WHERE admin_username='admin'")
    if not cursor.fetchone():
        cursor.execute(
            "INSERT INTO Admin_Account VALUES (?, ?, ?, ?)",
            ('ADM001', 'System Administrator', 'admin', 'admin123')
        )

    # Misol uchun mahsulotlar
    cursor.execute("SELECT COUNT(*) FROM Parts_Category")
    if cursor.fetchone()[0] == 0:
        sample_products = [
            ('PRD001', 'Motor Moyi', 'Yog\'lar', 5.0, 50, 25.99),
            ('PRD002', 'Shina', 'Ehtiyot qismlar', 10.0, 30, 89.99),
            ('PRD003', 'Tormoz Diski', 'Ehtiyot qismlar', 7.5, 20, 45.50),
            ('PRD004', 'Akumulyator', 'Ehtiyot qismlar', 0.0, 15, 120.00),
            ('PRD005', 'Faralar', 'Optika', 15.0, 25, 35.75)
        ]
        cursor.executemany(
            "INSERT INTO Parts_Category VALUES (?, ?, ?, ?, ?, ?)",
            sample_products
        )

    conn.commit()
    conn.close()
    print(f"Database muvaffaqiyatli yaratildi: {db_path}")


if __name__ == '__main__':
    initialize_database()