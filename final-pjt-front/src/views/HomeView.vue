<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />

  
    <div>
      
      <!-- <MovieAll /> -->
      <h1>한 주의 PICK</h1>
      <TrendMovie />
    </div>

    <div>

      <h1>스테디</h1>
      <TopMovie />
    </div>
    

    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <!-- <SignLogin /> -->
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
// import SignLogin from '../components/SignLogin.vue'

// import NavBar from '@/components/NavBar.vue'
// import MovieAll from '@/components/MovieAll.vue'
import TrendMovie from '@/components/TrendMovie.vue'
import TopMovie from '@/components/TopMovie.vue'

export default {
  name: 'HomeView',
  components: {
    // NavBar,
    // MovieAll,
    TrendMovie,
    TopMovie
    

    // HelloWorld,
  },

  created() {
    this.getMovies()
    this.getTrendMovies()
    this.getTopMovies()
  },
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    },
    getTrendMovies() {
      this.$store.dispatch('getTrendMovies')
    },
    getTopMovies() {
    this.$store.dispatch('getTopMovies')
    },
  },
}
</script>
