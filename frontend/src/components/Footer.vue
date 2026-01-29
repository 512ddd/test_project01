<template>
  <footer class="footer">
    <div class="container">
      <div class="footer__grid">
        <div class="footer__column" v-for="col in 4" :key="col">
          <p>About Us</p>
          <p>About Us</p>
          <p>About Us</p>
          <p>About Us</p>
        </div>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  background: #f5f5f5;
  padding: 3rem 0;
  margin-top: 3rem;
}
.footer__grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2rem;
}
.footer__column p {
  margin: 0.5rem 0;
  color: #666;
}
</style>