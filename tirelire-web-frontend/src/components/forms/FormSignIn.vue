<script setup>
  import { reactive } from 'vue'
  import axios from 'axios';

  const formInput = reactive({
    email: "",
    password: ""
  })

  function signIn () {
      const backend_url = import.meta.env.VITE_BACKEND_URL
      const response = axios.post(
          backend_url + '/api/v1/login',
          JSON.stringify(formInput),
          {
            headers: {
              'Content-Type': 'application/json'
            }
          }
        ).then((response) => { console.log(response); }
        ).catch((error) => {
          if( error.response ){
            console.log(error.response.data);
            }
          console.log(error)
          }
        );
      
      console.log(response)

    }

</script>

<template>
  <div class="sign-form">
      <h2>Sign In</h2>
      <form>
        <div class="input email">
          <label for='email'>Email</label>
          <input v-model="formInput.email" type='email'>
        </div>
        <div class="input password">
          <label for='password'>Password</label>
          <input v-model="formInput.password" type='password'>
        </div>
        <button type="button" class='signin' @click="signIn()">Sign In</button>
      </form>
    </div>
</template>

<style scoped>
  .sign-form {
      font-weight: 500;
      color: black;
      text-align: center;
  }
  .sign-form form {
      width: 328px;
  }
  form input[type='text'],
  form input[type='email'],
  form input[type='password'] {
      display: block;
      width: 100%;
      box-sizing: border-box;
      border-radius: 8px;
      border: 1px solid #c4c4c4;
      padding: 0.75em;
      margin-bottom: 1rem;
      font-size: 0.875rem;
  }
  label {
      display: block;
      text-align: left;
      margin-bottom: 0.5rem;
      font-size: 0.75rem;
      font-weight: 500;
  }
  .signin {
      display: block;
      width: 100%;
      background-color: #42b983;
      color: white;
      font-weight: 700;
      border: none;
      padding: 1rem;
      border-radius: 8px;
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.5px;
  }
  .signin:hover {
      background: #14985d;
      cursor: pointer;
      transition: 0.15s ease;
  }
</style>
