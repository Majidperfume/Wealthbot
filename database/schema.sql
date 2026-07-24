PRAGMA foreign_keys = ON;


----------------------------------------------------
-- ASSET TYPES
----------------------------------------------------

CREATE TABLE IF NOT EXISTS asset_types (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL UNIQUE,

    description TEXT DEFAULT '',

    active INTEGER DEFAULT 1

);


----------------------------------------------------
-- CURRENCIES
----------------------------------------------------

CREATE TABLE IF NOT EXISTS currencies (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    code TEXT NOT NULL UNIQUE,

    name TEXT NOT NULL,

    symbol TEXT DEFAULT '',

    active INTEGER DEFAULT 1

);


----------------------------------------------------
-- ASSETS
----------------------------------------------------

CREATE TABLE IF NOT EXISTS assets (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,

    asset_type_id INTEGER NOT NULL,

    currency_id INTEGER NOT NULL,

    note TEXT DEFAULT '',

    active INTEGER DEFAULT 1,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,


    FOREIGN KEY(asset_type_id)
        REFERENCES asset_types(id),


    FOREIGN KEY(currency_id)
        REFERENCES currencies(id)

);


----------------------------------------------------
-- PERSONS
----------------------------------------------------

CREATE TABLE IF NOT EXISTS persons (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,

    relation TEXT DEFAULT '',

    note TEXT DEFAULT '',

    active INTEGER DEFAULT 1,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);


----------------------------------------------------
-- PROJECTS
----------------------------------------------------

CREATE TABLE IF NOT EXISTS projects (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,

    description TEXT DEFAULT '',

    active INTEGER DEFAULT 1,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);


----------------------------------------------------
-- TRANSACTION TEMPLATES
----------------------------------------------------

CREATE TABLE IF NOT EXISTS transaction_templates (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL UNIQUE,

    requires_source INTEGER DEFAULT 1,

    requires_destination INTEGER DEFAULT 1,

    active INTEGER DEFAULT 1

);


----------------------------------------------------
-- TRANSACTIONS
----------------------------------------------------

CREATE TABLE IF NOT EXISTS transactions (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    template_id INTEGER,

    project_id INTEGER,

    person_id INTEGER,

    note TEXT DEFAULT '',

    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    active INTEGER DEFAULT 1,


    FOREIGN KEY(template_id)
        REFERENCES transaction_templates(id),


    FOREIGN KEY(project_id)
        REFERENCES projects(id),


    FOREIGN KEY(person_id)
        REFERENCES persons(id)

);


----------------------------------------------------
-- TRANSACTION ENTRIES
----------------------------------------------------

CREATE TABLE IF NOT EXISTS transaction_entries (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    transaction_id INTEGER NOT NULL,

    asset_id INTEGER NOT NULL,

    amount REAL NOT NULL,


    FOREIGN KEY(transaction_id)
        REFERENCES transactions(id),


    FOREIGN KEY(asset_id)
        REFERENCES assets(id)

);


----------------------------------------------------
-- SETTINGS
----------------------------------------------------

CREATE TABLE IF NOT EXISTS settings (

    key TEXT PRIMARY KEY,

    value TEXT

);
