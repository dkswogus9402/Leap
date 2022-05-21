<template>
  <div>
    <h1>회원가입 페이지</h1>
    <div class="signup_container">
    <router-link class="signup_box" :to="{name: 'jobseekerSignup'}"> 일반회원으로 가입하기 </router-link>
    <router-link class="signup_box" :to="{name: 'companySignup'}"> 회사회원으로 가입하기 </router-link>
    <router-link class="signup_box" :to="{name: 'academySignup'}"> 학원으로 가입하기 </router-link>
    </div>
    <br>
    <router-link :to="{name: 'main'}"> 메인으로 돌아가기 </router-link>
  </div>
</template>

<script>
export default {
  name: 'SignupView',
}
</script>

<style>
.signup_container{
  display: flex;
  justify-content: space-evenly;
}
.signup_box{
  border: 1px solid black;
  width: 150px;
  height: 150px;
}
</style>