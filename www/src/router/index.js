import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/Home.vue'
import Broswer from '../components/Broswer.vue'
import BroswerView from '../components/systems/broswer_view.vue'
import Contact from '../components/Contact.vue'
import MotherBoard from '../components/MotherBoard.vue'
import SystemView from '../components/systems/system_view.vue'
import ItemPage from '../components/systems/ItemPage.vue'
import Research from '../components/Research.vue'
Vue.use(VueRouter)
// 传入插件

// 通过routes配置组件之间的映射关系
const routes = [
  { path: '', redirect: '/home' },
  { path: '/home', component: Home },
  { path: '/about', component: Contact },
  { path: '/research', component: Research },
  {
    path: '/broswer',
    component: Broswer,
    redirect: '/broswer_view',
    children: [
      { path: '/broswer_view', component: BroswerView },
      { path: '/CRISPR', component: SystemView },
      { path: '/CRISPR/itempage', component: ItemPage },
      { path: '/RM', component: SystemView },
      { path: '/RM/itempage', component: ItemPage },
      { path: '/TA', component: SystemView },
      { path: '/TA/itempage', component: ItemPage },
      { path: '/Abi', component: SystemView },
      { path: '/Abi/itempage', component: ItemPage },
      { path: '/BREX', component: SystemView },
      { path: '/BREX/itempage', component: ItemPage },
      { path: '/pAgos', component: SystemView },
      { path: '/pAgos/itempage', component: ItemPage }
    ]
  },
  { path: '/motherboard', component: MotherBoard }
]

const router = new VueRouter({
  routes
  // mode: 'history'
})

// 将router传入Vue实例中main.js中挂载
export default router
