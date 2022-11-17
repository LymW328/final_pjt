<template>
  <div>
    startview
    <div>
      <button @click="login">
        Login
      </button>
      <div>
        <button @click="sign">
          Signin
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'StartView',
  methods: {
    login() {
      this.$router.push('SignInView')
    },
  },
}
</script>

<style></style>
