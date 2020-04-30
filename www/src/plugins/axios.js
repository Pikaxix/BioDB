import Vue from 'vue'
import axios from 'axios'

axios.defaults.baseURL = 'http://api.dacapo.top/api/'
Vue.prototype.axios = axios
