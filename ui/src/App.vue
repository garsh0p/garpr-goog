<template>
  <v-app>
    <!-- TODO: Move toolbar to seperate component. -->
    <v-toolbar app dark color="primary">
      <router-link to="/" tag="div" class="headline">
        GAR PR
      </router-link>

      <v-toolbar-items class="ml-4">
        <v-btn flat v-for="page of pages"
                    :key="page.id"
                    :to="page.route">
          {{page.name}}
        </v-btn>
      </v-toolbar-items>

      <v-spacer></v-spacer>

      <v-menu bottom left offset-y>
        <template v-slot:activator="{on}">
          <v-btn icon v-on="on">
            <v-icon>more_vert</v-icon>
          </v-btn>
        </template>

        <v-list dense>
          <v-list-tile @click.stop="showLogin=true" >
            <v-list-tile-title>Login</v-list-tile-title>
          </v-list-tile>
        </v-list>
      </v-menu>
    </v-toolbar>

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

export default {
  name: 'App',
  components: {
    LoginDialog,
  },
  data: () => ({
    pages: [
      {id: 1, name: 'Rankings', route: '/'},
      {id: 2, name: 'Tournaments', route: '/tournaments'},
      {id: 3, name: 'About', route: '/about'},
    ],
    showLogin: false,
  })
}
</script>
