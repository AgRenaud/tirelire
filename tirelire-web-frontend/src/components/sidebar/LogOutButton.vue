<script>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { collapsed } from './state'
import auth from '@/auth'

export default {
  props: {
    to: { type: String, required: true },
    icon: { type: String, required: true }
  },
  setup (props) {
    const route = useRoute()
    const isActive = computed(() => route.path === props.to)
    return { isActive, collapsed }
  },
  methods: {
    // Log out with Userfront.logout()
    handleLogout() {
      auth.logout()
      this.$router.go()
    },
  },
}
</script>

<template>
  <transition name="fade">
    <v-button 
      class="logout-button"
      :disabled="isLoggedOut"
      @click="logout"
      @click.prevent="handleLogout"
    >
      <div class="info">
        <i class="fas fa-power-off" />
        <span v-if="!collapsed">
          Log out
        </span>
      </div>
    </v-button>
  </transition>
</template>

<style scoped>
.logout-button {
  display: block;
  margin: 2px;
  padding: 2px;
  background-color: #31614d;
  border-radius: 0.5em;
}
.logout-button:hover {
  transition: 0.15s ease;
  background-color: rgb(42, 80, 64);
  box-shadow: rgba(42, 80, 64, 0.253) 0px 2px 8px 0px;
  cursor: pointer;
}
.info:hover {
  color: rgb(255, 86, 86);
}
</style>
