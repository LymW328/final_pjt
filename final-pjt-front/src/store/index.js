import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    token: [],
  },
  getters: {},
  mutations: {},
  actions: {
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies`,
      })
        .then((res) => console.log(res, context))
        .catch((err) => console.log(err))
    },
  },
  modules: {},
})
