<template>
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

      <v-tooltip bottom>
        <template v-slot:activator="{on}">
          <v-btn icon v-on="on" @click.stop="toggleLogin">
            <v-icon>{{loginButton.icon}}</v-icon>
          </v-btn>
        </template>
        <span>{{loginButton.label}}</span>
      </v-tooltip>
    </v-toolbar>
</template>

<script>
export default {
  data: () => ({
    loggedIn: false,

    buttons: {
      login: {
        icon: "build",
        label: "Admin Login",
      },
      logout: {
        icon: "exit_to_app",
        label: "Logout",
      },
    },

    pages: [
      {id: 1, name: 'Rankings', route: '/'},
      {id: 2, name: 'Tournaments', route: '/tournaments'},
      {id: 3, name: 'About', route: '/about'},
    ],
  }),
  methods: {
    toggleLogin() {
      if (this.loggedIn) {
        // Logout
      } else {
        this.$emit('login');
      }
    }
  },
  computed: {
    loginButton: function() {
      if (this.loggedIn) {
        return this.buttons.logout;
      } else {
        return this.buttons.login;
      }
    }
  },
}
</script>
