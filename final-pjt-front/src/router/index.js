import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'

import LoginView from '../views/LoginView.vue'
import SignupView from '../views/SignupView.vue'
import MoviedetailView from '../views/MoviedetailView.vue'
import ArticleView from '@/views/ArticleView'
import CreateView from '@/views/CreateView'
import DetailView from '@/views/DetailView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ '../views/AboutView.vue'),
  },
  {
    path: '/login',
    name: 'LoginView',
    component: LoginView,
  },
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/signup',
    name: 'SignupView',
    component: SignupView,
  },
  {
    // path: 'movies/detail',
    path: '/movies/:movie_id',
    name: 'MovieDetail',
    component: MoviedetailView,
  },
  {
    path: '/articles',
    name: 'articles',
    component: ArticleView,
  },

  {
    path: '/create',
    name: 'CreateView',
    component: CreateView,
  },

  {
    path: '/articles/:article_id',
    name: 'DetailView',
    component: DetailView,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
})

export default router
