<template>
  <v-app>
    <v-toolbar app tabs dark color="primary">
        <router-link to="/" tag="v-toolbar-title" class="headline text-uppercase">
                GAR PR
        </router-link>

      <template v-slot:extension>
        <v-tabs centered grow color="transparent" v-model="activeTab">
          <v-tab v-for="tab in tabs"
                 :key="tab.id"
                 :to="tab.route">
            {{tab.name}}
          </v-tab>
        </v-tabs>
      </template>
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
      activeTab: '/rankings',
      tabs: [
        {id: 1, name: 'Rankings', route: '/rankings'},
        {id: 2, name: 'Tournaments', route: '/tournaments'},
        {id: 3, name: 'About', route: '/about'},
        {id: 4, name: 'Login', route: '/login'},
      ]
    }
  },
  watch: {
    // Update the tabs correctly when navigating to the home page.
    $route(to, from) {
      if (to.path === '/') {
        this.activeTab = this.tabs[0].route;
      }
    }
  },
}
</script>
