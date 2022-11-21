<template>
  <span class="col d-flex justify-content-center margin mb-3 mt-3">
    <div class="card" style="width: 18rem;">
      <img @click="getdetail" :src="imageURL" class="card-img-top" alt="사진" />
      <hr />
      <div class="card-body">
        <p class="card-title">{{ movie.title }}</p>
      </div>
    </div>
  </span>
</template>

<script>
export default {
  name: 'MovieAllItem',
  props: {
    movie: Object,
    movie_id: Number,
  },

  computed: {
    imageURL() {
      return `https://image.tmdb.org/t/p/w500${this.movie.poster_path}`
    },
  },

  methods: {
    getdetail() {
      // this.$router.push({name : 'detail'})
      this.$router.push({
        name: 'MovieDetail',
        params: { movie_id: this.movie.movie_id, check: '재대로왓나..' },
      })
    },
  },
}
</script>

<style></style>
