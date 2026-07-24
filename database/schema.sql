PRAGMA foreign_keys = ON;

----------------------------------------------------
-- ACCOUNTS
----------------------------------------------------

CREATE TABLE IF NOT EXISTS accounts (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL UNIQUE,

    description TEXT DEFAULT '',

    active INTEGER DEFAULT 1,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

----------------------------------------------------
-- CURRENCIES
----------------------------------------------------

CREATE TABLE IF NOT EXISTS currencies (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,

    code TEXT NOT NULL UNIQUE,

    symbol TEXT DEFAULT '',

    active INTEGER DEFAULT 1,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

----------------------------------------------------
-- PERSONS
----------------------------------------------------

CREATE TABLE IF NOT EXISTS persons (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,

    phone TEXT DEFAULT '',

    note TEXT DEFAULT '',

    active INTEGER DEFAULT 1,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

----------------------------------------------------
-- CATEGORIES
----------------------------------------------------

CREATE TABLE IF NOT EXISTS categories (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL UNIQUE,

    icon TEXT DEFAULT '',

    active INTEGER DEFAULT 1

);

----------------------------------------------------
-- TRANSACTION TYPES
----------------------------------------------------

CREATE TABLE IF NOT EXISTS transaction_types (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL UNIQUE,

    active INTEGER DEFAULT 1

);

----------------------------------------------------
-- TRANSACTIONS
----------------------------------------------------

CREATE TABLE IF NOT EXISTS transactions (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    transaction_type_id INTEGER,

    category_id INTEGER,

    account_id INTEGER,

    currency_id INTEGER,

    person_id INTEGER,

    amount REAL NOT NULL,

    note TEXT DEFAULT '',

    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(transaction_type_id)
        REFERENCES transaction_types(id),

    FOREIGN KEY(category_id)
        REFERENCES categories(id),

    FOREIGN KEY(account_id)
        REFERENCES accounts(id),

    FOREIGN KEY(currency_id)
        REFERENCES currencies(id),

    FOREIGN KEY(person_id)
        REFERENCES persons(id)

);

----------------------------------------------------
-- SETTINGS
----------------------------------------------------

CREATE TABLE IF NOT EXISTS settings (

    key TEXT PRIMARY KEY,

    value TEXT

);
