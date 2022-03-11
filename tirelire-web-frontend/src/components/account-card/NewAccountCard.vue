<template>
  <div class="card">
    <img src="@/assets/bank.svg">
    <label>
      New Account
    </label>
  </div>
</template>

<script>
export default {
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
  border-style: dashed;
  background-color: rgb(0, 112, 0, .05);
  opacity: .5;
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
  box-shadow: 0px 1px 2px 0px rgba(42, 80, 64, .5), inset 0px 1px 2px 0px rgba(42, 80, 64, .5);
  transition: 0.15s ease;
  opacity: 1;
}
.card:hover *{
  opacity: 0.5;
  transition: 0.15s ease;
}
.img.add-element {
  transition: .5s ease;
  opacity: 0;
  position: inherit;
  top: 75%;
  left: 50%;
  transform: translate(-50%, -50%);
}

</style>