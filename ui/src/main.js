import Vue from 'vue'
import App from './App.vue'
import router from './router'
import Vuetify from 'vuetify/lib'
import 'vuetify/src/stylus/app.styl'

Vue.config.productionTip = false
Vue.use(Vuetify)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
