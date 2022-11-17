<template>
  <div>
    startview
    <div>
      <button @click="login">
        Login
      </button>
      <div>
        <button @click="sign">
          Signup
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
      this.$router.push('/login')
    },
    sign() {
      this.$router.push('/signup')
    },
  },
}
</script>

<style></style>
