import random
from decimal import Decimal
from django.core.management.base import BaseCommand
from django.utils import timezone
from index.models import (
    Customer, Vendor, Store, Product, Order, OrderItem, 
    OrderStatus, CartItem, WishlistItem, Comment
)

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting old data...')
        # Clear existing data to avoid duplicates/conflicts
        OrderItem.objects.all().delete()
        Order.objects.all().delete()
        CartItem.objects.all().delete()
        WishlistItem.objects.all().delete()
        Product.objects.all().delete()
        Store.objects.all().delete()
        Vendor.objects.all().delete()
        Customer.objects.all().delete()
        
        self.stdout.write('Creating new data...')

        # 1. Create Vendors and Stores
        vendors = []
        stores = []
        vendor_names = ['TechGiant', 'FashionHub', 'HomeStyle', 'SportsPro']
        
        for name in vendor_names:
            vendor = Vendor.objects.create(
                vendorUsername=name.lower(),
                password='password123',  # In production use hashed passwords
                email=f'contact@{name.lower()}.com',
                phoneNo=f'1380013800{random.randint(0, 9)}'
            )
            vendors.append(vendor)
            
            store = Store.objects.create(
                vendor=vendor,
                storeName=f'{name} Official Store'
            )
            stores.append(store)
            self.stdout.write(f'Created store: {store.storeName}')

        # 2. Create Products
        products = []
        product_data = [
            ('Smartphone X', 999.00, 'Electronics', 'Latest model with AI features'),
            ('Laptop Pro', 1299.00, 'Electronics', 'High performance laptop for pros'),
            ('Summer Dress', 49.99, 'Clothing', 'Light and breezy for summer'),
            ('Running Shoes', 89.99, 'Footwear', 'Comfortable shoes for daily run'),
            ('Coffee Maker', 120.00, 'Home', 'Brew the perfect cup every morning'),
            ('Yoga Mat', 25.50, 'Sports', 'Non-slip mat for yoga practice'),
            ('Wireless Earbuds', 150.00, 'Electronics', 'Noise cancelling earbuds'),
            ('Denim Jacket', 75.00, 'Clothing', 'Classic style denim jacket'),
        ]

        for i, (name, price, category, desc) in enumerate(product_data):
            store = stores[i % len(stores)]
            product = Product.objects.create(
                store=store,
                productName=name,
                quantity=random.randint(10, 100),
                brand=store.storeName.split()[0],
                category=category,
                description=desc,
                price=Decimal(str(price)),
                availability=True
            )
            products.append(product)
            self.stdout.write(f'Created product: {product.productName}')

        # 3. Create Customers
        customers = []
        customer_names = [('John', 'Doe'), ('Jane', 'Smith'), ('Alice', 'Johnson')]
        
        for first, last in customer_names:
            customer = Customer.objects.create(
                firstName=first,
                lastName=last,
                password='password123',
                email=f'{first.lower()}.{last.lower()}@example.com',
                phoneNo=f'1390013900{random.randint(0, 9)}',
                shippingAddress=f'{random.randint(1, 999)} Main St, Cityville'
            )
            customers.append(customer)
            self.stdout.write(f'Created customer: {first} {last}')

        # 4. Create Orders
        for customer in customers:
            # Create 1-3 orders per customer
            for _ in range(random.randint(1, 3)):
                order = Order.objects.create(
                    customer=customer,
                    shippingAddress=customer.shippingAddress,
                    totalAmount=0  # Will update after adding items
                )
                
                total = 0
                # Add 1-4 items per order
                for _ in range(random.randint(1, 4)):
                    product = random.choice(products)
                    qty = random.randint(1, 3)
                    price = product.price
                    
                    order_item = OrderItem.objects.create(
                        order=order,
                        product=product,
                        productName=product.productName,
                        quantity=qty,
                        price=price
                    )
                    
                    OrderStatus.objects.create(
                        orderItem=order_item,
                        status=random.choice(['Pending', 'Shipped', 'Pending'])
                    )
                    
                    total += price * qty
                
                order.totalAmount = total
                order.save()
                self.stdout.write(f'Created order #{order.id} for {customer.firstName}')

        self.stdout.write(self.style.SUCCESS('Successfully populated database'))
