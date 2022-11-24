<template>
  <div>
    <h5>{{ article.id }} 번째 글</h5>
    <p>작성자 : {{ article.username }}</p>
    <p>제목 : {{ article.title }}</p>
    <router-link :to="{ name: 'DetailView', params: { id: article.id } }">
      [DETAIL]
    </router-link>
    <button @click="deletea">[DELETE]</button>

    <hr />
  </div>
</template>

<script>
import axios from 'axios'
// import router from '@/router'
const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'ArticleListItem',
  props: {
    article: Object,
  },
  data() {
    return {
      article_id: this.article.id,
    }
  },

  methods: {
    deletea() {
      axios({
        method: 'delete',
        url: `${API_URL}/articles/${this.article_id}/`,
      })
        .then((res) => {
          this.$store.dispatch('getArticles')
          console.log(res.data)
          console.log('ok')
        })
        .catch((err) => {
          console.log(err)
        })
      // router.push({ name: 'articles' })
    },
  },
}
</script>

<style></style>
