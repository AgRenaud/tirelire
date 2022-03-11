<script setup>
  import { reactive } from 'vue'
  import { useRouter, useRoute } from 'vue-router'

  import auth from '@/auth'

  const router = useRouter()
  const route = useRoute()

  const formInput = reactive({
    username: "",
    password: ""
  })

  function login () {
    auth.login(formInput.username, formInput.password, loggedIn => {
      if (!loggedIn) {
        this.error = true
      } else {
        router.replace(route.query.redirect || '/')
        router.go()
      }
    })
  }
</script>

<template>
  <div class="container">
    <div class="container-row">
      <div class="container-cell" />
    </div>
    <div class="container-row">
      <div class="container-cell">
        <div class="form-container-row">
          <img 
            class="icon" 
            src="@/assets/person-outline.svg" 
          >
          <input 
            v-model="formInput.username"
            class="form-container-row-input" 
            placeholder="Username"
            autocomplete="on"
          >
        </div>
        <div class="form-container-row">
          <img 
            class="icon" 
            src="@/assets/lock-open-outline.svg"
          >
          <input 
            v-model="formInput.password"
            class="form-container-row-input" 
            type="password"
            placeholder="Password"
            autocomplete="on"
          >
        </div>
        <div class="form-container-row">
          <button class="form-container-row-button create-account">
            Créer un compte
          </button>
          <button
            class="form-container-row-button connect"
            type="button"
            @click="login()"
          >
            Connexion
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
  .container {
    display: table;
    width: 66%;
    max-width: 500px;
    height: auto;
    padding: 20px 30px;
    opacity: 100%;
  }
  .container-row {
    display: table-row;
    text-align: center;
  }
  .container-cell {
    display: table-cell;
    justify-content: center;
    text-align: center;
    vertical-align: middle;
  }
  .form-container-row {
    display: center;
    margin: 16px 0px;
    gap:16px;
    max-height: auto;
  }
  .form-container-row-input {
    width: 66%;
    padding: 5px;
    border-width:0px;
    color: rgb(0,0,0,1);
    background-color: rgb(0,0,0,0);
    border:transparent;
    outline: none;
    box-shadow: none;
  }
  .form-container-row-input::placeholder{
    color: rgb(0,0,0,.8);
  }
  .form-container-row-button {
    border-radius: 5px;
    margin: 4px;
    border:transparent;
    outline: none;
    box-shadow: none;
    background-color: rgba(224, 231, 255, 0.644)
  }
  .icon {
    height: 14px;
  }
  .logo {
    max-height: 100px;
    display: inline-block;
    vertical-align: middle;
    line-height: normal;
  }
  .connect:hover {
    background-color: rgb(4, 158, 17, .6); 
    transition: .4s;
  }
  .create-account:hover {
    background-color: rgba(255, 184, 52, 0.801); 
    transition: .4s;
  }
</style>
