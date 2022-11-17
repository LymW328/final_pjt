<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <SignLogin />
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import SignLogin from '../components/SignLogin.vue'
export default {
  name: 'HomeView',
  components: {
    // HelloWorld,
    SignLogin,
  },
}
</script>
