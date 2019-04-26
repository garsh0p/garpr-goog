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
          <v-btn icon v-on="on" @click.stop="login">
            <v-icon>build</v-icon>
          </v-btn>
        </template>
        <span>Admin Login</span>
      </v-tooltip>
    </v-toolbar>
</template>

<script>
export default {
  data: () => ({
    pages: [
      {id: 1, name: 'Rankings', route: '/'},
      {id: 2, name: 'Tournaments', route: '/tournaments'},
      {id: 3, name: 'About', route: '/about'},
    ],
  }),
  methods: {
    login() {
      this.$emit('login');
    }
  }
}
</script>
