from django.db import models

# 1. 客户模型
class Customer(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    phoneNo = models.CharField(max_length=20)
    shippingAddress = models.TextField()
    createdDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

# 2. 商家模型
class Vendor(models.Model):
    vendorUsername = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField()
    phoneNo = models.CharField(max_length=20)
    profileImage = models.ImageField(upload_to='vendor_profiles/', null=True, blank=True)
    createdDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vendorUsername

# 3. 店铺模型
class Store(models.Model):
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE)
    storeName = models.CharField(max_length=100)

    def __str__(self):
        return self.storeName

# 4. 店铺图片模型
class StorePhoto(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    photoURL = models.URLField()
    sortedOrder = models.IntegerField()
    isPrimary = models.BooleanField(default=False)
    uploadedDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['sortedOrder']

# 5. 商品模型
class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    productName = models.CharField(max_length=200)
    quantity = models.IntegerField()
    brand = models.CharField(max_length=50, null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    availability = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.productName

# 6. 商品媒体模型
class ProductMedia(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    mediaURL = models.URLField()
    mediaType = models.CharField(max_length=50)
    mediaContent = models.TextField(null=True, blank=True)
    sortedOrder = models.IntegerField()
    isPrimary = models.BooleanField(default=False)

    class Meta:
        ordering = ['sortedOrder']

# 7. 订单模型
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    shippingAddress = models.TextField()
    totalAmount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} - {self.customer}"

# 8. 订单项模型
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    productName = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.productName} - {self.quantity}"

# 9. 订单状态模型
class OrderStatus(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Holding', 'Holding'),
        ('Shipped', 'Shipped'),
        ('Cancelled', 'Cancelled'),
    ]
    orderItem = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    updatedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.orderItem} - {self.status}"

# 10. 取消项模型
class CancelledItem(models.Model):
    orderStatus = models.OneToOneField(OrderStatus, on_delete=models.CASCADE, primary_key=True)
    reason = models.TextField()

    def __str__(self):
        return f"Cancelled: {self.orderStatus.orderItem}"

# 11. 购物车项模型（复合主键）
class CartItem(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        unique_together = ['customer', 'product']  # 复合主键替代

    def __str__(self):
        return f"{self.customer} - {self.product}"

# 12. 收藏项模型
class WishlistItem(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    addedDate = models.DateTimeField(auto_now_add=True)
    isNotified = models.BooleanField(default=False)
    original_price_at_added = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount_rate_at_added = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    price_at_added = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        unique_together = ['customer', 'product']

    def __str__(self):
        return f"{self.customer} - {self.product}"

# 13. 评论模型
class Comment(models.Model):
    orderItem = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Comment on {self.orderItem} - {self.rating}/5"

# 14. 收藏节省模型
class WishlistSavings(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    totalSavings = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    lastUpdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Savings for {self.customer}: {self.totalSavings}"

# 15. 搜索历史模型
class SearchHistory(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    query = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now=True)
    expirationDate = models.DateTimeField()

    def __str__(self):
        return f"{self.query} - {self.store}"

# 16. 促销模型
class Promotion(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('activated', 'Activated'),
        ('expired', 'Expired'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    discountRate = models.DecimalField(max_digits=5, decimal_places=2)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    createdTime = models.DateTimeField(auto_now_add=True)
    updatedTime = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.product} - {self.discountRate}% off"