<template>
  <div>
    MoviedetailView
    <div>
      <!-- {{ (this.$route.params.check) }}
      {{ this.$route.params.movie_id }} -->
      <!-- {{ movie_id}} -->
          
      <img
      :src="imageURL" alt="사진">
      <!-- {{ imageURL }} -->
      <div>
      {{ thismovie.title }}
      </div>
      <hr>
      <div>
      {{ thismovie.poster_path }}
      </div>
      <hr>
      <div>
      {{ thismovie.genres }}
      </div>
      <hr>
      <div>
      {{ thismovie.released_date }}
      </div>
      <hr>
      <div>
      {{ thismovie.overview }}
      </div>
      <hr>
      <div>
        <button
        @click="getback">뒤로</button>
      </div>
      
      {{ check }}
    </div>
    <!-- {{ movie }} -->
  </div>
</template>

<script>
const API_URL = 'http://127.0.0.1:8000'
import axios from 'axios'
export default {
  name: 'MoviedetailView',
    computed: {
    movie() {
      console.log(this.$store.state.movie)
      return this.$store.state.movies
    },
      
    imageURL() {
      return `https://image.tmdb.org/t/p/w500${this.thismovie.poster_path}`

    },


    // onmovie() {
    //   return this.$store.state.movie
    // }
  },
  data() {

    return {
      movie_id : this.$route.params.movie_id,
      check : this.$route.params.check,

      // thismovie : null    ### null 로 기본 설정하면 오류가 나더라... 아고 너무 힘들다...ㅠㅠ
      thismovie : 0
    }
    
  },

  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.movie_id}/`
      })
      .then((res) => {
        console.log(res.data)
        this.thismovie = res.data
      })
      .catch(err => console.log(err))
    },
     getback() {
      this.$router.push({name : 'home'})

     }
  },

  // props: {
  //   movie_id: {
  //     type: Number,
      
  //   },
  //   check: {
  //     type: String,
  //     default: "",
  //   },

  // },
  created() {
    console.log(this.$route.params.check)
    console.log(this.$route.params.movie_id)
    console.log(this.$store.state.movie)
    this.getMovieDetail()
    
  },



}

</script>

<style>

</style>

