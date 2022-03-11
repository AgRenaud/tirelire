<script setup>
import SideBarLink from './SideBarLink'
import LogOutButton from './LogOutButton'
import { collapsed, toggleSidebar, sidebarWidth } from './state'
</script>

<template>
  <div 
    class="sidebar" 
    :style="{ width: sidebarWidth }"
  >
    <div class="header">
      <h1>
        <span v-if="collapsed" />
        <span v-else>Tirelire</span>
      </h1>
    </div>

    <div class="links">
      <SideBarLink 
        to="/" 
        icon="fas fa-home"
      >
        Home
      </SideBarLink>
      <SideBarLink 
        to="/dashboard" 
        icon="fas fa-columns"
      >
        Dashboard
      </SideBarLink>
    </div>

    <div class="bottom-actions">
      <LogOutButton />
    </div>

    <span
      class="collapse-icon"
      :class="{ 'rotate-180': collapsed }"
      @click="toggleSidebar"
    >
      <i class="fas fa-angle-double-left" />
    </span>
  </div>
</template>

<style>
:root {
  --sidebar-bg-color: #2f855a;
  --sidebar-item-hover: #38a169;
  --sidebar-item-active: #276749;
}
</style>

<style scoped>
.sidebar {
  color: white;
  background-color: var(--sidebar-bg-color);
  float: left;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  bottom: 0;
  padding: 0.5em;
  transition: 0.3s ease;
  display: flex;
  flex-direction: column;
}
.sidebar h1 {
  height: 2.5em;
}
.collapse-icon {
  position: absolute;
  bottom: 0;
  padding: 0.75em;
  color: rgba(255, 255, 255, 0.7);
  transition: 0.2s linear;
}
.rotate-180 {
  transform: rotate(180deg);
  transition: 0.2s linear;
}
.bottom-actions {
  bottom: 0;
  padding-bottom: 2.5em;
}

</style>
