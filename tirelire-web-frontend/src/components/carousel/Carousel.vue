<template>
  <div class="carousel">
    <slot />
    <button
      class="carousel__nav carousel__next" 
      @click.prevent="next"
    >
      Next
    </button>
    <button
      class="carousel__nav carousel__prev" 
      @click.prevent="prev"
    >
      Previous
    </button>
  </div>
</template>

<script>

export default {
    data () {
        return {
            index: 0,
            slides: []
        }
    },
    computed: {
      slidesCount () { return this.slides.length}
    },
    mounted () {
        this.slides = this.$children
        this.slides.forEach((slide, i) => {
            slide.index = i
        })
    },
    methods: {
      next () {
        this.index++
        if (this.index >= this.slidesCount) {
          this.index = this.slidesCount - 1 
        }
      },
      prev () {
        this.index-- 
        if (this.index < this.slidesCount) {
          this.index = 0
        }
      }
    }
}

</script>

<style>

</style>