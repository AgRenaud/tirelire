<script setup>
  import { ref, reactive } from 'vue'

  import { useRouter } from "vue-router";
  import { useAuthStore } from "@/stores/useAuth.js";


  const loading = ref(false);
  const router = useRouter();


  const formInput = reactive({
    first_name: "",
    last_name: "",
    email: "",
    password: ""
  })

  function signUp () {
        useAuthStore()
          .register(
            JSON.stringify(formInput)
          )
          .then(() => router.push({ name: "index" }))
          .catch(() => (loading.value = !loading.value));
    }
</script>

<template>
  <div class="sign-form">
      <h2>Sign Up</h2>
      <form>
        <div class="input name">
          <label for='fname'>First Name</label>
          <input v-model="formInput.first_name" type='text'>
        </div>
        <div class="input name">
          <label for='lname'>Last Name</label>
          <input v-model="formInput.last_name" type='text'>
        </div>
        <div class="input email">
          <label for='email'>Email</label>
          <input v-model="formInput.email" type='email'>
        </div>
        <div class="input password">
          <label for='password'>Password</label>
          <input v-model="formInput.password" type='password'>
        </div>
        <button type="button" class='signup' @click="signUp()">Sign Up</button>
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
    .signup {
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
    .signup:hover {
        background: #14985d;
        cursor: pointer;
        transition: 0.15s ease;
    }
</style>
