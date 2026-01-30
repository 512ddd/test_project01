<template>
  <div class="admin-layout">
    <!-- 侧边栏 -->
    <aside class="sidebar">
      <div class="logo">Shop Admin</div>
      <nav>
        <ul>
          <li :class="{ active: currentTab === 'dashboard' }" @click="currentTab = 'dashboard'">仪表盘</li>
          <li :class="{ active: currentTab === 'products' }" @click="currentTab = 'products'">商品管理</li>
          <li :class="{ active: currentTab === 'orders' }" @click="currentTab = 'orders'">订单管理</li>
          <li :class="{ active: currentTab === 'customers' }" @click="currentTab = 'customers'">客户列表</li>
        </ul>
      </nav>
    </aside>

    <!-- 主内容区 -->
    <main class="main-content">
      <!-- 顶部栏 -->
      <header class="top-bar">
        <h2>{{ pageTitle }}</h2>
        <div class="user-profile">Admin User</div>
      </header>

      <!-- 内容区域 -->
      <div class="content-area">
        <!-- 仪表盘 -->
        <div v-if="currentTab === 'dashboard'" class="dashboard-stats">
          <div class="stat-card">
            <h3>总销售额</h3>
            <p class="number">¥12,345</p>
          </div>
          <div class="stat-card">
            <h3>总订单</h3>
            <p class="number">150</p>
          </div>
          <div class="stat-card">
            <h3>总用户</h3>
            <p class="number">320</p>
          </div>
        </div>

        <!-- 商品管理 -->
        <div v-if="currentTab === 'products'">
          <div class="action-bar">
            <button class="btn-primary" @click="openProductModal()">添加商品</button>
          </div>
          <table class="data-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>图片</th>
                <th>商品名称</th>
                <th>价格</th>
                <th>库存</th>
                <th>操作</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="product in products" :key="product.id">
                <td>{{ product.id }}</td>
                <td>
                  <img v-if="product.image" :src="product.image" alt="Product Image" class="product-thumb">
                  <span v-else class="no-image">无图</span>
                </td>
                <td>{{ product.productName }}</td>
                <td>¥{{ product.price }}</td>
                <td>{{ product.quantity }}</td>
                <td>
                  <button class="btn-small" @click="openProductModal(product)">编辑</button>
                  <button class="btn-small btn-danger" @click="deleteProduct(product.id)">删除</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- 订单管理 -->
        <div v-if="currentTab === 'orders'">
            <table class="data-table">
            <thead>
              <tr>
                <th>订单号</th>
                <th>客户</th>
                <th>总金额</th>
                <th>状态</th>
                <th>日期</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="order in orders" :key="order.id">
                <td>#{{ order.id }}</td>
                <td>{{ order.customer_name }}</td>
                <td>¥{{ order.totalAmount }}</td>
                <td><span class="status-badge">{{ order.status }}</span></td>
                <td>{{ formatDate(order.date) }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </main>

    <!-- 商品编辑/添加弹窗 -->
    <div v-if="showProductModal" class="modal-overlay">
      <div class="modal">
        <div class="modal-header">
          <h3>{{ editingProduct ? '编辑商品' : '添加商品' }}</h3>
          <button class="close-btn" @click="closeProductModal">×</button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="saveProduct">
            <div class="form-group">
              <label>商品名称</label>
              <input v-model="productForm.productName" type="text" required>
            </div>
            <div class="form-group">
              <label>价格</label>
              <input v-model="productForm.price" type="number" step="0.01" required>
            </div>
            <div class="form-group">
              <label>库存</label>
              <input v-model="productForm.quantity" type="number" required>
            </div>
             <div class="form-group">
              <label>店铺ID</label>
              <input v-model="productForm.store" type="number" required placeholder="输入店铺ID (例如: 1)">
            </div>
            <div class="form-group">
              <label>描述</label>
              <textarea v-model="productForm.description"></textarea>
            </div>
            <div class="form-group">
              <label>图片</label>
              <input type="file" @change="handleImageUpload" accept="image/*">
              <div v-if="previewImage" class="image-preview">
                <img :src="previewImage" alt="Preview">
              </div>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn-secondary" @click="closeProductModal">取消</button>
              <button type="submit" class="btn-primary">保存</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, reactive } from 'vue'
import axios from 'axios'

const currentTab = ref('dashboard')
const products = ref([])
const orders = ref([])

// 商品弹窗状态
const showProductModal = ref(false)
const editingProduct = ref(null)
const productForm = reactive({
  productName: '',
  price: 0,
  quantity: 0,
  store: 1, // 默认店铺ID，实际应从下拉框选择
  description: '',
  image: null
})
const previewImage = ref(null)

const pageTitle = computed(() => {
  const titles = {
    dashboard: '仪表盘',
    products: '商品管理',
    orders: '订单管理',
    customers: '客户列表'
  }
  return titles[currentTab.value]
})

// 获取数据
const fetchData = async () => {
  try {
    // 获取商品
    const prodRes = await axios.get('/products/')
    products.value = prodRes.data.results || prodRes.data

    // 获取订单 (这里假设有订单接口，且后端做了适当的序列化优化)
    const orderRes = await axios.get('/orders/')
    orders.value = (orderRes.data.results || orderRes.data).map(order => ({
        ...order,
        // 简单处理，实际可能需要根据customer id再去查，或者后端直接返回name
        customer_name: `Customer ${order.customer}`,
        status: 'Pending' // 示例状态
    }))
  } catch (error) {
    console.error('获取数据失败', error)
  }
}

// 打开商品弹窗
const openProductModal = (product = null) => {
  editingProduct.value = product
  showProductModal.value = true
  
  if (product) {
    // 编辑模式：填充表单
    productForm.productName = product.productName
    productForm.price = product.price
    productForm.quantity = product.quantity
    productForm.store = product.store
    productForm.description = product.description
    previewImage.value = product.image
    productForm.image = null // 重置文件上传，除非用户重新选择
  } else {
    // 添加模式：重置表单
    productForm.productName = ''
    productForm.price = 0
    productForm.quantity = 0
    productForm.store = 1
    productForm.description = ''
    productForm.image = null
    previewImage.value = null
  }
}

// 关闭商品弹窗
const closeProductModal = () => {
  showProductModal.value = false
  editingProduct.value = null
}

// 处理图片选择
const handleImageUpload = (event) => {
  const file = event.target.files[0]
  if (file) {
    productForm.image = file
    // 创建预览 URL
    previewImage.value = URL.createObjectURL(file)
  }
}

// 保存商品 (新增/更新)
const saveProduct = async () => {
  try {
    const formData = new FormData()
    formData.append('productName', productForm.productName)
    formData.append('price', productForm.price)
    formData.append('quantity', productForm.quantity)
    formData.append('store', productForm.store)
    formData.append('description', productForm.description)
    
    if (productForm.image) {
      formData.append('image', productForm.image)
    }

    if (editingProduct.value) {
      // 更新
      await axios.patch(`/products/${editingProduct.value.id}/`, formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      })
    } else {
      // 新增
      await axios.post('/products/', formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      })
    }
    
    // 刷新列表并关闭弹窗
    await fetchData()
    closeProductModal()
  } catch (error) {
    console.error('保存失败', error)
    alert('保存失败: ' + (error.response?.data?.detail || error.message))
  }
}

// 删除商品
const deleteProduct = async (id) => {
  if (!confirm('确定要删除这个商品吗？')) return
  
  try {
    await axios.delete(`/products/${id}/`)
    await fetchData()
  } catch (error) {
    console.error('删除失败', error)
    alert('删除失败')
  }
}

const formatDate = (dateStr) => {
  return new Date(dateStr).toLocaleDateString()
}

onMounted(() => {
  fetchData()
})
</script>

<style scoped>
/* ...原有样式... */
.admin-layout {
  display: flex;
  min-height: 100vh;
  background-color: #f5f7fa;
}

/* 侧边栏 */
.sidebar {
  width: 240px;
  background-color: #2c3e50;
  color: white;
  flex-shrink: 0;
}

.logo {
  height: 60px;
  line-height: 60px;
  text-align: center;
  font-size: 20px;
  font-weight: bold;
  border-bottom: 1px solid #34495e;
}

.sidebar nav ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.sidebar nav li {
  padding: 15px 20px;
  cursor: pointer;
  transition: background 0.3s;
}

.sidebar nav li:hover, .sidebar nav li.active {
  background-color: #34495e;
  border-left: 4px solid #42b983;
}

/* 主内容区 */
.main-content {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}

.top-bar {
  height: 60px;
  background: white;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
  box-shadow: 0 1px 4px rgba(0,0,0,0.1);
}

.content-area {
  padding: 20px;
  overflow-y: auto;
}

/* 统计卡片 */
.dashboard-stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin-bottom: 20px;
}

.stat-card {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.stat-card h3 {
  color: #7f8c8d;
  font-size: 14px;
  margin-bottom: 10px;
}

.stat-card .number {
  font-size: 24px;
  font-weight: bold;
  color: #2c3e50;
}

/* 表格样式 */
.data-table {
  width: 100%;
  background: white;
  border-radius: 8px;
  border-collapse: collapse;
  overflow: hidden;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.data-table th, .data-table td {
  padding: 12px 15px;
  text-align: left;
  border-bottom: 1px solid #ecf0f1;
}

.data-table th {
  background-color: #f8f9fa;
  font-weight: 600;
  color: #2c3e50;
}

.action-bar {
  margin-bottom: 20px;
}

.btn-primary {
  background: #42b983;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
}

.btn-secondary {
  background: #95a5a6;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
  margin-right: 10px;
}

.btn-small {
  padding: 4px 8px;
  margin-right: 5px;
  border: 1px solid #ddd;
  background: white;
  border-radius: 4px;
  cursor: pointer;
}

.btn-danger {
  color: #e74c3c;
  border-color: #e74c3c;
}

.product-thumb {
  width: 50px;
  height: 50px;
  object-fit: cover;
  border-radius: 4px;
}

.no-image {
  color: #ccc;
  font-size: 12px;
}

/* 弹窗样式 */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0,0,0,0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal {
  background: white;
  border-radius: 8px;
  width: 500px;
  max-width: 90%;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.modal-header {
  padding: 15px 20px;
  border-bottom: 1px solid #eee;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.close-btn {
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
}

.modal-body {
  padding: 20px;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: 500;
}

.form-group input[type="text"],
.form-group input[type="number"],
.form-group textarea {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.image-preview img {
  max-width: 100px;
  margin-top: 10px;
  border-radius: 4px;
}

.modal-footer {
  padding: 15px 20px;
  border-top: 1px solid #eee;
  text-align: right;
}
</style>
