<template>
  <div class="card">
    <img src="@/assets/bank.svg">
    <label>
      {{ name }}
    </label>
  </div>
</template>

<script>
export default {
  props: {
    name: String
  }
}
</script>


<style scoped>
.card {
  position: relative;
  min-width: 80px;
  max-width: 100px;
  height: 120px;
  border-radius: 15px;
  margin: 4px;
  border: 2px solid rgba(0, 112, 0);
  background-color: rgb(0, 112, 0, .3);
}
.card label{
  position: absolute;
  top: 65%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: auto;
  color: black;
  opacity: .5;
}
.card img{
  width: 30px;
  position: absolute;
  top: 25%;
  left: 50%;
  transform: translate(-50%, -50%);
  opacity: .5;
}
.card:hover {
  box-shadow: rgba(42, 80, 64) 0px 2px 8px 0px;
}
.card:hover *{
  opacity: .7;
  transition: 0.15s ease;
}
</style>