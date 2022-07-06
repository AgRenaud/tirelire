import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

var path = require('path');

export default defineConfig({
  plugins: [vue()],
  resolve: {
    extensions: ['.mjs', '.js', '.ts', '.jsx', '.tsx', '.json', '.vue'],
    alias: {
      "@": path.resolve(__dirname, "./src")
    },
  },
  server: {
    cors: {
      credentials: true
    }
  }
});