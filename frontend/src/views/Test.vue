<template>
  <div class="user-info">
    <h2>我的个人信息</h2>
    <!-- 加载中提示 -->
    <div v-if="loading">加载中...</div>
    <!-- 错误提示 -->
    <div v-if="error" class="error">{{ error }}</div>
    <!-- 用户信息卡片 -->
    <div v-if="userInfo" class="info-card">
      <p><span>姓名：</span>{{ userInfo.firstName }} {{ userInfo.lastName }}</p>
      <p><span>邮箱：</span>{{ userInfo.email }}</p>
      <p><span>手机号：</span>{{ userInfo.phoneNo }}</p>
      <p><span>收货地址：</span>{{ userInfo.shippingAddress }}</p>
      <p><span>注册时间：</span>{{ formatDate(userInfo.createdDate) }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getCustomerInfo } from '@/api/api'

// 状态管理
const loading = ref(true)
const error = ref('')
const userInfo = ref(null)

// 实际项目中，customer_id从“登录状态”获取（比如存在Vuex/Pinia中）
const customer_id = 1  // 这里先写死测试，后续替换为动态值

// 页面加载时请求用户信息
onMounted(async () => {
  try {
    const res = await getCustomerInfo(customer_id)
    userInfo.value = res.data  // 接口返回的用户数据
  } catch (err) {
    error.value = err.response?.data?.error || "获取用户信息失败"
  } finally {
    loading.value = false
  }
})

// 格式化时间（可选）
const formatDate = (dateStr) => {
  return new Date(dateStr).toLocaleString()
}
</script>

<style scoped>
.user-info {
  padding: 20px;
}
.info-card {
  border: 1px solid #eee;
  padding: 20px;
  margin-top: 10px;
}
.info-card p {
  line-height: 2;
}
.info-card span {
  font-weight: bold;
  margin-right: 10px;
}
.error {
  color: red;
  margin-top: 10px;
}
</style>