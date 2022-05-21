<template>
  <div class>
    <h1>구직자 회원가입페이지</h1>
    <br>
    <br>
    <signup-form></signup-form>
  </div>
</template>

<script>
import SignupForm from '@/components/SignupForm.vue'

export default {
  name:'JobSeekerSignupView',
  components: { SignupForm },

}
</script>

<style>

</style>