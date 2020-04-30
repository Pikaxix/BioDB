import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/basic/Home.vue'
import Broswer from '../components/basic/Broswer.vue'
import BroswerView from '../components/broswer/broswer_view.vue'
import Microbe from '../components/microbe/microbe.vue'
import Phage from '../components/phage/phage.vue'
import Help from '../components/basic/Help.vue'
import SystemView from '../components/microbe/system_view.vue'
import ItemPage from '../components/microbe/ItemPage.vue'

// 传入插件
Vue.use(VueRouter)

// 通过routes配置组件之间的映射关系
const routes = [
  { path: '', redirect: '/home' },
  { path: '/home', component: Home },
  {
    path: '/broswer',
    component: Broswer,
    children: [
      { path: '/', component: BroswerView },
      {
        path: '/broswer/:system',
        component: SystemView,
        children: [
          { path: 'itempage', component: ItemPage }
        ]
      }
    ]
  },
  {
    path: '/microbe',
    component: Microbe,
    children: [
      // { path: 'itempage/:nowTab', component: ItemPage },
      {
        path: '/microbe/:system',
        component: SystemView,
        children: [
          { path: 'itempage/:nowTab', component: ItemPage }
        ]
      }
    ]
  },
  { path: '/itempage/:genome_name', component: ItemPage },
  { path: '/help', component: Help },
  { path: '/phage', component: Phage }
]

const router = new VueRouter({
  routes
  // mode: 'history'
})

// 将router传入Vue实例中main.js中挂载
export default router
