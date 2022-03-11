<template>
  <div class="login-container">
    <div class="carousel-container">
      Hello world
    </div>
    <div class="form-container">
      <FormAuth />
    </div>
  </div>
</template>

<script setup>
  import FormAuth from '@/components/forms/FormAuth'
</script>

<style scoped>
  .login-container {
    display: flex;
    height: 100vh;
    text-align: center;
  }
  .carousel-container {
    height: inherit;
    width: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #42b983;
    border: 1px solid rgb(0, 134, 78);
    box-shadow: 6px 0 5px -2px #888;
  }
  .form-container {
    height: inherit;
    width: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
  }
</style>
