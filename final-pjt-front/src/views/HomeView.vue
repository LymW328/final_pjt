<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <NavBar />
    <div>homeview입니다.</div>
    <div>
      {{ movies }}
    </div>

    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <!-- <SignLogin /> -->
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
// import SignLogin from '../components/SignLogin.vue'

import NavBar from '@/components/NavBar.vue'

export default {
  name: 'HomeView',
  components: {
    NavBar,

    // HelloWorld,
  },
  computed: {
    movies() {
      // console.log(this.$store.state.movies)
      return this.$store.state.movies
    },
  },
  created() {
    this.getMovies()
  },
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    },
  },
}
</script>
