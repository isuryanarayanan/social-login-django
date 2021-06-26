import { createApp } from "vue";
import App from "./App.vue";
import gAuthPlugin from "vue3-google-oauth2";
const app = createApp(App);
const gAuthOptions = {
  clientId:
    "237734924210-9g6r23vnmpmv1l6jtmfrn8f1tb6ing6o.apps.googleusercontent.com",
  scope: "profile email openid",
  prompt: "consent",
  fetch_basic_profile: false,
};
app.use(gAuthPlugin, gAuthOptions);
app.mount("#app");
