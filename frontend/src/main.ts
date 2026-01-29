// src/main.ts
import { createApp } from 'vue'
import App from './App.vue'
import router from './router' // 导入路由配置

// 创建 Vue 应用实例
const app = createApp(App)

// 挂载路由
app.use(router)

// 将应用挂载到 index.html 中的 #app 元素上
app.mount('#app')