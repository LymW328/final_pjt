<template>
  <div class="container">
    <b-carousel
      id="carousel-1"
      v-model="slide"
      :interval="4000"
      controls
      indicators
      background="#ababab"
      img-width="500"
      img-height="300"
      style="text-shadow: 1px 1px 2px #333; width:100px  vertical-align: middle"
      @sliding-start="onSlideStart"
      @sliding-end="onSlideEnd"
    >
      <TrendMovieItem
        v-for="(movie, index, movie_id) in trendmovies"
        :key="movie.id"
        :movie="movie"
        :movie_id="movie_id"
      />
    </b-carousel>

    <hr />
    <div></div>
  </div>
</template>

<script>
import TrendMovieItem from './TrendMovieItem.vue'
export default {
  name: 'TrendMovie',
  components: {
    TrendMovieItem,
  },
  computed: {
    trendmovies() {
      // console.log(this.$store.state.movies)
      return this.$store.state.trends
    },
  },
}
</script>

<style></style>
