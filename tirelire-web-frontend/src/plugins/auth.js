import { useAuthStore } from "@/stores/useAuth";

export default {
  install: ({ config }) => {
    config.globalProperties.$auth = useAuthStore();

    if (useAuthStore().loggedIn) {
      useAuthStore().fetchUser();
    }
  },
};