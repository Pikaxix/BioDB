import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import App from './App.vue'
import router from './router/'
import './plugins/element.js'
import './plugins/axios.js'
import './plugins/chart.js'
import './assets/css/global.css'
import Router from 'vue-router'

import VCharts from 'v-charts'
Vue.use(VCharts)

Vue.use(Router)

const originalPush = Router.prototype.push
Router.prototype.push = function push (location) {
  return originalPush.call(this, location).catch(err => err)
}

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
