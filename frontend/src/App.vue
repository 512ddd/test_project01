<!-- src/App.vue -->
<template>
  <!-- 路由出口：所有页面组件的渲染容器 -->
  <router-view />
</template>

<script setup>
// 无需导入任何组件，路由会自动渲染
</script>

<style>
/* 这里可以写全局样式（如重置默认样式、全局字体/颜色） */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Microsoft YaHei", sans-serif;
}
a {
  text-decoration: none;
  color: #333;
}
ul, li {
  list-style: none;
}
/* 全局容器样式（之前写在Home.vue里的，移到这里更合理，所有页面共用） */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}
</style>