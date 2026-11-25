from faker import Faker
import pandas as pd
import numpy as np
import random

fake = Faker()

#customer table
customer = [[fake.user_name(), fake.address(), fake.email()] for x in range(10)]

df_customer = pd.DataFrame(customer, columns = ["customer_name", "customer_address", "email"])
df_customer["customer_phone_number"] = ["+91" + str(np.random.randint(6000000000, 9999999999, dtype = np.int64)) for _ in range(len(df_customer))]
df_customer["customer_id"] = np.random.randint(low = 1000, high = 10000, size = len(df_customer))
print(df_customer.head())

#order table
order_type = ["online order", "offline order"]
order_status = ["pending", "shipped", "delivered", "cancelled"]

Order = [[fake.date(), random.choice(order_type), random.choice(order_status)] for x in range(10)]

df_order = pd.DataFrame(Order, columns = ["order_date", "order_type", "order_status"])
df_order["Order_id"] = np.random.randint(low = 10000, high = 100000, size = len(df_order))
print(df_order.head())

#product table
products_category = ["Electronics", "Clothing", "Home & kitchen", "Books"]
product_name = ["smartphone", "laptop", "t-shirt", "jeans", "mixer", "plates", "novel", "textbook"]

product = [[random.choice(product_name), random.choice(products_category)] for x in range(10)]

df_product = pd.DataFrame(product, columns = ["product_name", "product_category"])
df_product["product_quantity"] = np.random.randint(low = 1, high = 100, size = len(df_product))
df_product["product_discount"] = np.random.randint(low = 0, high = 90, size = len(df_product))
df_product["product_price"] = np.random.randint(low = 10.5, high = 1000.5, size = len(df_product)).astype(float)
df_product["Total Amount"] = df_product["product_quantity"] * df_product["product_price"]
df_product["Discounted_product_price"] = df_product["Total Amount"] - (df_product["Total Amount"] * df_product["product_discount"] / 100)
df_product["product_id"] = np.random.randint(low = 1000, high = 10000, size = len(df_product))
print(df_product.head())

#employee table
employee_name = ["Arjun", "Jaya", "Maha", "Raja", "Vishal", "Sara"]

employee = [[fake.address(), fake.email(), random.choice(employee_name)]]

df_employee = pd.DataFrame(employee, columns = ["employee_address", "employee_email", "employee_name"])
df_employee["employee_phone_number"] = ["+91" + str(np.random.randint(6000000000, 9999999999, dtype = np.int64)) for _ in range(len(df_employee))]
df_employee["employee_id"] = np.random.randint(low = 10000, high = 100000, size = len(df_employee))
print(df_employee.head())

#payment table
payment_status = ["payment_processing", "payment_received", "payment_received_confirm"]
payment_type = ["cash_on_hand", "online_payment"]

payment = [[random.choice(payment_status), random.choice(payment_type), fake.date()]]

df_payment = pd.DataFrame(payment, columns = ["payment_status", "payment_type", "payment_date"])
df_payment["payment_id"] = np.random.randint(low = 100000, high = 1000000, size = len(df_payment))
print(df_payment.head())

#cleaning - to drop duplicates
df_customer = df_customer.drop_duplicates()
df_order = df_order.drop_duplicates()
df_product = df_product.drop_duplicates()

#cleaning - to drop null values
df_customer = df_customer.dropna()
df_order = df_order.dropna()
df_product = df_product.dropna()

df_customer = df_customer.to_csv("customer.csv", index = False)
df_order = df_order.to_csv("order.csv", index = False)
df_product = df_product.to_csv("product.csv", index = False)
df_employee = df_employee.to_csv("employee.csv", index = False)
df_payment = df_payment.to_csv("payment.csv", index = False)