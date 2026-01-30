// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
// 导入首页组件（之前写的Home.vue）
import Home from '../views/Home.vue'


// 路由规则数组：path是访问路径，component是对应组件
const routes = [
  {
    path: '/', // 根路径（网站首页）
    name: 'Home', // 路由名称（可选，方便跳转）
    component: Home // 对应首页组件
  },
  {
    path: '/test', 
    name: 'Test', 
    component: () => import('../views/Test.vue') 
  },
  {
    path: '/admin',
    name: 'Admin',
    component: () => import('../views/Admin.vue')
  },
 
]

// 创建路由实例
const router = createRouter({
  history: createWebHistory(), // 采用HTML5历史模式（无#的路径，推荐）
  routes // 注入路由规则
})

// 导出路由，供main.js使用
export default router