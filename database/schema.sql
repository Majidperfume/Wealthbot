-- WealthBot Database Schema
-- Version 1.0


PRAGMA foreign_keys = ON;


-- کاربران
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER UNIQUE NOT NULL,
    name TEXT,
    username TEXT,
    is_admin INTEGER DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);


-- حساب ها
CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT DEFAULT 'bank',
    active INTEGER DEFAULT 1,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);


-- ارزها
CREATE TABLE IF NOT EXISTS currencies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    code TEXT UNIQUE NOT NULL,
    symbol TEXT,
    active INTEGER DEFAULT 1,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);


-- اشخاص
CREATE TABLE IF NOT EXISTS persons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT,
    note TEXT,
    active INTEGER DEFAULT 1,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);


-- انواع تراکنش
CREATE TABLE IF NOT EXISTS transaction_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    icon TEXT,
    active INTEGER DEFAULT 1,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);


-- دسته بندی ها
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    icon TEXT,
    active INTEGER DEFAULT 1,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);


-- تراکنش اصلی
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    transaction_type_id INTEGER NOT NULL,
    category_id INTEGER,
    person_id INTEGER,
    description TEXT,
    transaction_date TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(transaction_type_id)
        REFERENCES transaction_types(id),

    FOREIGN KEY(category_id)
        REFERENCES categories(id),

    FOREIGN KEY(person_id)
        REFERENCES persons(id)
);


-- اثرهای مالی هر تراکنش
-- هر تراکنش می‌تواند چند اثر داشته باشد
CREATE TABLE IF NOT EXISTS transaction_entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    transaction_id INTEGER NOT NULL,

    account_id INTEGER,
    currency_id INTEGER,
    person_id INTEGER,

    amount REAL NOT NULL,

    entry_type TEXT NOT NULL,

    note TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,


    FOREIGN KEY(transaction_id)
        REFERENCES transactions(id),

    FOREIGN KEY(account_id)
        REFERENCES accounts(id),

    FOREIGN KEY(currency_id)
        REFERENCES currencies(id),

    FOREIGN KEY(person_id)
        REFERENCES persons(id)
);


-- تنظیمات سیستم
CREATE TABLE IF NOT EXISTS settings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    key TEXT UNIQUE NOT NULL,
    value TEXT
);
