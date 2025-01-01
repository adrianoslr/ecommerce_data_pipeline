import random
import pandas as pd
from faker import Faker

fake = Faker()

def generate_customers(num_customers=1000):
    data = []
    for _ in range(num_customers):
        data.append({
            'customer_id': fake.uuid4(),
            'name': fake.name(),
            'age': random.randint(18, 70),
            'city': fake.city()
        })
    return pd.DataFrame(data)

def generate_products(num_products=100):
    data = []
    for _ in range(num_products):
        data.append({
            'product_id': fake.uuid4(),
            'category': random.choice(['Electronics', 'Books', 'Clothing', 'Food']),
            'price': round(random.uniform(5, 500), 2)
        })
    return pd.DataFrame(data)

def generate_sales(customers, products, num_sales=5000):
    data = []
    for _ in range(num_sales):
        data.append({
            'sale_id': fake.uuid4(),
            'customer_id': random.choice(customers['customer_id']),
            'product_id': random.choice(products['product_id']),
            'date': fake.date_this_year(),
            'amount': random.randint(1, 5)
        })
    return pd.DataFrame(data)

if __name__ == "__main__":
    customers = generate_customers()
    products = generate_products()
    sales = generate_sales(customers, products)

    customers.to_csv('../data/customers.csv', index=False)
    products.to_csv('../data/products.csv', index=False)
    sales.to_csv('../data/sales.csv', index=False)
