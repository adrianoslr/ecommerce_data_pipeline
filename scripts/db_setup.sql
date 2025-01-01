CREATE TABLE customers (
    customer_id UUID PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    city VARCHAR(100)
);

CREATE TABLE products (
    product_id UUID PRIMARY KEY,
    category VARCHAR(50),
    price DECIMAL(10, 2)
);

CREATE TABLE sales (
    sale_id UUID PRIMARY KEY,
    customer_id UUID REFERENCES customers(customer_id),
    product_id UUID REFERENCES products(product_id),
    date DATE,
    amount INT,
    sale_month INT,
    sale_year INT
);
