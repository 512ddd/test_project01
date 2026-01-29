<template>
  <div>
    <Header />
    <HeroSection />
    <div class="divider"></div>
    <NewestAddition />
    <Footer />
  </div>
</template>

<script setup>
import Header from '../components/Header.vue'
import HeroSection from '../components/HeroSection.vue'
import NewestAddition from '../components/NewestAddition.vue'
import Footer from '../components/Footer.vue'
</script>

<style scoped>
.divider {
  height: 150px;
  background: #999;
  margin: 2rem 0;
}
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}
</style>