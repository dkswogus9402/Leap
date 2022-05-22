<template>
  <div>
    <router-link :to="{name: 'main'}">Leap |</router-link>
    <router-link :to="{name: 'login'}"> Login | </router-link>
    <router-link :to="{name: 'singup'}"> SignUp | </router-link>
    <router-link :to="{name: 'logOut'}">LogOut | </router-link>
    <router-link :to="{name: 'jobSeekerProfile'}"> My Profile |</router-link>
    <router-link :to="{name: 'companyProfile'}"> Company Profile |</router-link>
    <router-link :to="{name: 'academyProfile'}"> Academy Profile</router-link>

  </div>
</template>

<script>
export default {
  name: 'NavBar',
}
</script>

<style>

</style>