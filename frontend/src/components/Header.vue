<template>
  <header class="header">
    <div class="container">
      <div class="header__inner">
        <div class="logo">
          <h1>SenseLondon</h1>
        </div>
        <nav class="nav">
          <ul>
            <li><a href="#categories">Categories</a></li>
            <li><a href="#brands">Brands</a></li>
            <li><a href="#sale">Sale</a></li>
            <li><a href="#in-stock">In Stock</a></li>
            <li><a href="#contact">Contact Us</a></li>
          </ul>
        </nav>
        <div class="header__actions">
          <button class="icon-btn">🛒</button>
          <button class="icon-btn">🔍</button>
          <button class="icon-btn">🤍</button>
          <button class="icon-btn">👤</button>
        </div>
      </div>
    </div>
  </header>
</template>

<style scoped>
.header {
  border-bottom: 1px solid #e5e5e5;
  padding: 1rem 0;
}
.header__inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.nav ul {
  display: flex;
  gap: 2rem;
  list-style: none;
  padding: 0;
  margin: 0;
}
.nav a {
  text-decoration: none;
  color: #333;
  font-weight: 500;
}
.header__actions {
  display: flex;
  gap: 1rem;
}
.icon-btn {
  background: none;
  border: none;
  font-size: 1.2rem;
  cursor: pointer;
}
</style>