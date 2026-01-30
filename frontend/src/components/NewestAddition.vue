<template>
  <section class="newest">
    <div class="container">
      <div class="newest__header">
        <div>
          <h3>Newest Addition</h3>
          <p class="count">{{ totalCount }}</p>
          <p>Items Waiting To Be Discovered</p>
          <button class="btn btn-outline">SHOP NOW</button>
        </div>
      </div>
      <div class="newest__items">
        <div class="item-card" v-for="product in products" :key="product.id">
          <div class="item-card__image">
            <img v-if="product.image" :src="product.image" :alt="product.productName" />
            <div v-else class="no-image">No Image</div>
          </div>
          <p class="product-name">{{ product.productName }}</p>
          <p class="product-price">¥{{ product.price }}</p>
        </div>
        <button class="scroll-btn" v-if="products.length > 4">→</button>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const products = ref([])
const totalCount = ref(0)

const fetchNewestProducts = async () => {
  try {
    // 获取最新商品，按 ID 升序
    // 限制只获取 4 个
    const response = await axios.get('/products/?ordering=id&page_size=4')
    
    // 兼容分页和不分页的返回结构
    if (response.data.results) {
      // 确保只取前4个，虽然 page_size=4 应该已经限制了
      products.value = response.data.results.slice(0, 4)
      totalCount.value = response.data.count
    } else {
      products.value = response.data.slice(0, 4)
      totalCount.value = response.data.length
    }
  } catch (error) {
    console.error('获取最新商品失败:', error)
  }
}

onMounted(() => {
  fetchNewestProducts()
})
</script>

<style scoped>
.newest {
  padding: 3rem 0;
}
.newest__header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}
.count {
  font-size: 3rem;
  font-weight: 700;
  margin: 0.5rem 0;
}
.btn-outline {
  background: transparent;
  border: 2px solid #333;
  color: #333;
  margin-top: 1rem;
  padding: 0.8rem 2rem;
  cursor: pointer;
  transition: all 0.3s;
}
.btn-outline:hover {
  background: #333;
  color: white;
}
.newest__items {
  display: flex;
  gap: 2rem;
  align-items: flex-start; /* 改为顶部对齐，防止高度不一致 */
  overflow-x: auto;
  padding-bottom: 1rem;
  scroll-behavior: smooth;
}
.newest__items::-webkit-scrollbar {
  height: 6px;
}
.newest__items::-webkit-scrollbar-thumb {
  background: #ccc;
  border-radius: 3px;
}
.item-card {
  flex: 0 0 auto;
  text-align: center;
  width: 200px; /* 固定宽度 */
}
.item-card__image {
  width: 200px;
  height: 300px;
  background: #f5f5f5;
  border-radius: 8px;
  margin-bottom: 1rem;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}
.item-card__image img {
  width: 100%;
  height: 100%;
  object-fit: cover; /* 保持比例填充 */
  transition: transform 0.3s;
}
.item-card:hover .item-card__image img {
  transform: scale(1.05);
}
.no-image {
  color: #999;
  font-size: 0.9rem;
}
.product-name {
  font-weight: 600;
  margin-bottom: 0.5rem;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.product-price {
  color: #666;
}
.scroll-btn {
  background: transparent;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  align-self: center;
}
</style>