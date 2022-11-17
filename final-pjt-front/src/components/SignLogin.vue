<template>
  <div>
    <div>
      <div>
        <button @click="signIn">
          <!-- <router-link to="/signin">signin</router-link> -->

          SIGN IN
        </button>
      </div>
      <div>
        <button @click="logIn">
          LOG IN
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SignLogin',
  methods: {
    logIn() {
      this.$router.push({ name: 'LogInView' })
    },
    signIn() {
      this.$router.push({ name: 'signin' })
    },
  },
}
</script>

<style></style>
