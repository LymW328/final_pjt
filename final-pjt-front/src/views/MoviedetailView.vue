<template>
  <div>
    <div class="d-flex justify-content-center mb-3 mt-3">
      <b-card no-body class="overflow-hidden" style="max-width: 540px;">
        <b-row no-gutters>
          <b-col md="6">
            <b-card-img
              :src="imageURL"
              alt="Image"
              class="rounded-0"
            ></b-card-img>
          </b-col>

          <b-col md="6">
            <b-card-body :title="thismovie.title">
              <b-card-text>
                <div>
                  {{ thismovie.genres[1].name }}
                </div>

                <div>
                  {{ thismovie.released_date }}
                </div>

                <div>
                  {{ thismovie.overview }}
                </div>
              </b-card-text>
            </b-card-body>
          </b-col>
        </b-row>
      </b-card>
    </div>
    <div>
      <button @click="getback">뒤로</button>
    </div>
    <!-- {{ check }} -->
    <div></div>
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
      console.log(this.thismovie)
      return `https://image.tmdb.org/t/p/w500${this.thismovie.poster_path}`
    },

    // onmovie() {
    //   return this.$store.state.movie
    // }
  },
  data() {
    return {
      movie_id: this.$route.params.movie_id,
      check: this.$route.params.check,

      // thismovie : null    ### null 로 기본 설정하면 오류가 나더라... 아고 너무 힘들다...ㅠㅠ
      thismovie: 0,
    }
  },

  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.movie_id}/`,
      })
        .then((res) => {
          console.log('디테일')
          console.log(res.data)
          this.thismovie = res.data
        })
        .catch((err) => console.log(err))
    },
    getback() {
      this.$router.push({ name: 'home' })
    },
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

<style></style>
