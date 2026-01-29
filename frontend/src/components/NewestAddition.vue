<template>
  <section class="newest">
    <div class="container">
      <div class="newest__header">
        <div>
          <h3>Newest Addition</h3>
          <p class="count">16</p>
          <p>Items Waiting To Be Discovered</p>
          <button class="btn btn-outline">SHOP NOW</button>
        </div>
      </div>
      <div class="newest__items">
        <div class="item-card" v-for="item in 4" :key="item">
          <div class="item-card__image"></div>
          <p>Lorem Ipsum Dolor<br>Sit Amet</p>
        </div>
        <button class="scroll-btn">→</button>
      </div>
    </div>
  </section>
</template>

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
}
.newest__items {
  display: flex;
  gap: 2rem;
  align-items: center;
  overflow-x: auto;
  padding-bottom: 1rem;
}
.item-card {
  flex: 0 0 auto;
  text-align: center;
}
.item-card__image {
  width: 200px;
  height: 300px;
  background: #999;
  border-radius: 8px;
  margin-bottom: 1rem;
}
.scroll-btn {
  background: transparent;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
}
</style>