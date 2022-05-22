<template>
  <div>
    <h1>원하시는 서비스를 클릭해주세요</h1>
    <hr>
    <br>
    <br>
    <div class="signup_containers">
      <router-link class="signup_box" :to="{name: 'jobseekerSignup'}"> 구직회원 </router-link>
      <router-link class="signup_box" :to="{name: 'companySignup'}"> 구인회원 </router-link>
      <router-link class="signup_box" :to="{name: 'academySignup'}"> 교육회원 </router-link>
    </div>
    <br>
    <router-link class="back_box" :to="{name: 'main'}">  Main </router-link>
  </div>
</template>

<script>
export default {
  name: 'SignupView',
}
</script>

<style>
.signup_containers{
  display: flex;
  justify-content: space-evenly;
}
.signup_box{
  border: 1px solid black;
  background-color: #0009;
  color: white;
  font-size: 40px;
  width: 300px;
  height: 300px;
  text-align: center;
  
}
.back_box{
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100px;
  height: 20px;
  background-color: #0009;
  padding: 10px;
  font-size: 20px;
  color: white;
  

}
</style>