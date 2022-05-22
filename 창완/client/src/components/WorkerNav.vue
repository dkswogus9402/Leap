<template>
  <div class="worker_nav">
    <router-link :to="{name: 'jobSeekerProfile'}"> 개인 프로필</router-link>
    <router-link :to="{name: 'jobSeekerProcess'}">수강중인 교육</router-link>
    <router-link :to="{name: 'jobSeekerApply'}">지원중인 회사</router-link>
    <router-link :to="{name: 'jobSeekerSuggest'}">제안받은 회사</router-link>
    <router-link :to="{name: 'signout'}">회원 탈퇴하기</router-link>
  </div>
</template>

<script>
export default {
  name: 'WorkerNav'

}
</script>

<style>
.worker_nav{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border: 1px solid black;
}
</style>