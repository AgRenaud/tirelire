import { defineStore } from "pinia";
import axios from "axios";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    user: null,
    loggedIn: false
  }),

  getters: {},

  actions: {
    async register(credentials) {
      const response = await axios.post(
        "/api/v1/user/register", 
        credentials,
        {
          headers: {
            'Content-Type': 'application/json'
          }
        })
        .then((response) => { 
          
        })
        .catch((error) => {
          if( error.response ){
            console.log(error.response.data);
          }
          console.log(error)
        }
      );
    },

    async login(credentials) {
      const response = await axios.post(
        "/api/v1/user/login", 
        credentials,
        {
          headers: {
            'Content-Type': 'application/json'
          }
        }
      ).then(async function(res){
        if (res.status == 200){
          console.log('Fetch User')
          await this.fetchUser(); 
        }
      }
      ).catch((error) => {
        if( error.response ){
          console.log(error.response.data);
          }
        console.log(error)
        }
      );
    },

    async logout() {
      const response = (await axios.post(
        "/api/v1/user/logout"
      )).data;

      if (response) {
        this.$reset();
      }
    },

    async fetchUser() {
      this.user = (await axios.get("/api/v1/user/me")).data;
      this.loggedIn = true;
    },
  },
});