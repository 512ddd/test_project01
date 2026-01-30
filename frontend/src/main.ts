// src/main.ts
import { createApp } from 'vue'
import App from './App.vue'
import router from './router' // 导入路由配置
import axios from 'axios'

// 创建 Vue 应用实例
const app = createApp(App)

// 配置 axios 全局默认值
axios.defaults.baseURL = 'http://127.0.0.1:8000/index/api' // 后端 API 基础路径

// 将 axios 挂载到全局属性（可选，Vue 3 推荐按需导入，但这样配置方便老习惯）
app.config.globalProperties.$axios = axios

// 挂载路由
app.use(router)

// 将应用挂载到 index.html 中的 #app 元素上
app.mount('#app')