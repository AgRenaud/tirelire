import { defineStore } from 'pinia';

export const useUserStore = defineStore(
    "user",
    {
        state: () => {
            return {
                isAuthenticated: false,
            }
        },
        actions: {
            logIn(mail, password) {
                this.isAuthenticated = True
            },
            logOut() {
                this.isAuthenticated = False
            },
            register(mail, password) {
                this.isAuthenticated = True
            }
        }
    }
)