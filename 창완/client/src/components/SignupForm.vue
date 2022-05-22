<template>
  <div class="form_box">
    <h1>회원가입 폼입니다</h1>
    <h3>가입경로마다 다르겠죠?</h3>
    <br><br><br>
    <router-link :to="{name : 'main'}">회원가입하기</router-link>
   
  </div>
</template>

<script>
export default {
  name: 'SignupForm',

}
</script>

<style>
.form_box{
  border: 1px solid black;
}
</style>