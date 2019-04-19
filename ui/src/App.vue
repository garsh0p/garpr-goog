<template>
  <v-app>
    <v-toolbar app dark color="primary">
        <router-link to="/" tag="v-toolbar-title" class="headline text-uppercase">
                GAR PR
        </router-link>

        <v-toolbar-items class="ml-4">
          <v-btn flat v-for="page of pages"
                      :key="page.id"
                      :to="page.route">
            {{page.name}}
          </v-btn>
        </v-toolbar-items>
    </v-toolbar>

    <v-content>
      <v-container>
        <router-view />
      </v-container>
    </v-content>

  </v-app>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      pages: [
        {id: 1, name: 'Rankings', route: '/'},
        {id: 2, name: 'Tournaments', route: '/tournaments'},
        {id: 3, name: 'About', route: '/about'},
        {id: 4, name: 'Login', route: '/login'},
      ]
    }
  }
}
</script>
