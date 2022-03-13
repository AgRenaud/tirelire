<template>
  <div class="view-container">
    <div class="carousel-container">
      <!-- <img src="@/assets/img-main-features-presentation.svg">
      <h1>Suivez vos comptes avec Tirelire ! 🐽</h1> -->
      <Carousel
      :navigation="true"
      :pagination="true"
      :startAutoPlay="false"
      :timeout="5000"
      class="carousel"
      v-slot="{ currentSlide }"
    >
      <Slide v-for="(slide, index) in carouselSlides" :key="index">
        <div v-show="currentSlide === index + 1" class="slide-info">
          <img :src="`${slide.img}`" />
          <p> {{ slide.msg }} </p>
        </div>
      </Slide>
      </Carousel>
    </div>
    <div class="form-container">
      <FormSignIn />
    </div>
  </div>
</template>

<script setup>
  import FormSignIn from '@/components/forms/FormSignIn'
  import Carousel from '@/components/carousel/Carousel'
  import Slide from '@/components/carousel/Slide'

  import carouselImage1 from '@/assets/carousel/carousel-1.svg'
  import carouselImage2 from '@/assets/carousel/carousel-2.svg'
  import carouselImage3 from '@/assets/carousel/carousel-3.svg'

  const carouselSlides = [
    { "img": carouselImage1, "msg": "Rejoignez Tirelire pour suivre vos comptes !" },
    { "img": carouselImage2, "msg": "Ajoutez vos relevé de compte à tirelire à l'aide de notre interface ..." },
    { "img": carouselImage3, "msg": "... et analyser vos dépenses en détails !" } 
  ]
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
