<template>
  <v-app>
    <Toolbar @login="showLogin=true" />
    <LoginDialog v-model="showLogin" />

    <v-content>
      <v-container>
        <router-view />
      </v-container>
    </v-content>

  </v-app>
</template>

<script>
import LoginDialog from './components/LoginDialog.vue';
import Toolbar from './components/Toolbar.vue';

export default {
  name: 'App',
  components: {
    LoginDialog,
    Toolbar,
  },
  data: () => ({
    showLogin: false,
  })
}
</script>
