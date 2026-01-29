<template>
  <section class="hero">
    <div class="container">
      <div class="hero__inner">
        <div class="hero__banner">
          <h2>DISCOVER YOUR NEXT FASHION ITEM</h2>
          <button class="btn">Shop Now</button>
        </div>
        <div class="hero__grid">
          <div class="hero__grid-item" v-for="i in 4" :key="i"></div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.hero {
  padding: 2rem 0;
}
.hero__inner {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}
.hero__banner {
  background: #999;
  border-radius: 8px;
  padding: 3rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  color: white;    
}
.hero__banner h2 {
  font-size: 2rem;
  margin-bottom: 1.5rem;
  line-height: 1.2;
}
.btn {
  align-self: flex-start;
  background: white;
  color: #333;
  border: none;
  padding: 0.8rem 1.5rem;
  border-radius: 20px;
  cursor: pointer;
  font-weight: 600;
}
.hero__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr 1fr;
  gap: 1rem;
}
.hero__grid-item {
  background: #999;
  border-radius: 8px;
}
</style>