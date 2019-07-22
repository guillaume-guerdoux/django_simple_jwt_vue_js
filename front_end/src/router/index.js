import Vue from 'vue'
import Router from 'vue-router'
import Movies from '@/components/Movies'
import Login from '@/components/Login'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Movies',
      component: Movies
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    }
  ]
})
