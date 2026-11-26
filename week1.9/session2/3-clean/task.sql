.headers on
.mode column

-- add tasks below
-- sqlite3 database_file.db to open the database
-- .read sql_file.sql to run the queries

-- YOU SHOULD RUN ANY 'UPDATES' AS SELECTS FIRST - it's very easy to accidentally update more than you intended..
'''Enter ".help" for usage hints.
sqlite> .tables
customers     drivers     menu_items     order_items     orders     restaurants     reviews'''


'''sqlite> PRAGMA foreign_keys = ON;
sqlite> .schema customers
sqlite> 
sqlite> .read schema.sql
sqlite> .tables
customers     drivers     menu_items     order_items     orders     restaurants     reviews
sqlite> .schema customers
CREATE TABLE customers (
    customer_id  INTEGER PRIMARY KEY,
    name         TEXT NOT NULL,
    email        TEXT NOT NULL UNIQUE,
    postcode     TEXT,
    phone        TEXT,                -- optional, may be NULL
    joined_date  TEXT,                -- 'YYYY-MM-DD'
    referred_by  INTEGER,             -- who referred this customer (NULL if nobody)
    FOREIGN KEY (referred_by) REFERENCES customers(customer_id)
);
sqlite> .schema reviews
CREATE TABLE reviews (
    review_id  INTEGER PRIMARY KEY,
    order_id   INTEGER NOT NULL UNIQUE,   -- at most one review per order
    rating     INTEGER CHECK (rating BETWEEN 1 AND 5),
    comment    TEXT,                      -- optional, may be NULL
    FOREIGN KEY (order_id) REFERENCES orders(order_id)'''

    INSERT INTO customers(customer_id ,name , email) VALUES(1 , 'Alice' ,'alice@gmail.com' );
    INSERT INTO customers(customer_id ,name , email) VALUES(2 , 'Bob' ,'bob@gmail.com' ,NULL );
