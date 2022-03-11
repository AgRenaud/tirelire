<script setup>
  import { ref } from 'vue'

  import SideBar from '@/components/sidebar/SideBar'
  import Login from '@/views/Login'
  import { sidebarWidth } from '@/components/sidebar/state.js'

  import auth from './auth'

  const loggedIn = ref(auth.loggedIn())
</script>

<template>
  <div>
    <div v-if="loggedIn === true">
      <SideBar />
      <div :style="{ 'margin-left': sidebarWidth, 'padding-left': '10px' }">
        <router-view />
      </div>
    </div>
    <div v-else>
      <Login />
    </div>
  </div>
</template>



<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background-color: white;
  text-align: center;
  color: #2c3e50;
  height: 100vh;
}
#nav {
  padding: 30px;
}
#nav a {
  font-weight: bold;
  color: #2c3e50;
}
#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
