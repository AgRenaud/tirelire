<template>
  <div class="view-container">
    <div class="carousel-container">
      <img src="@/assets/img-main-features-presentation.svg">
      <h1>Suivez vos comptes avec Tirelire ! 🐽</h1>
    </div>
    <div class="form-container">
      <FormSignIn />
    </div>
  </div>
</template>

<script setup>
  import FormSignIn from '@/components/forms/FormSignIn'
</script>

<style scoped>
  .view-container {
    display: flex;
    flex-direction: row;
    height: 100%;
  }
  .carousel-container, .form-container{
    display: flex;
    justify-content: center;
    align-items: center;
    width: 50%;
    height: auto;
  }
  .carousel-container {
    flex-direction: column;
    color: white;
    background: linear-gradient(rgba(0,0,0,0), rgba(0,0,0,0.4));
    background-color: #42b983;
    border: 1px solid rgb(0, 134, 78);
    box-shadow: 6px 0 5px -2px rgb(136, 136, 136, .5);
  }
  /*
  .form-container {
    height: inherit;
    width: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
  } */
</style>
