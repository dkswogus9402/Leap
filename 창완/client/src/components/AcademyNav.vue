<template>
  <div class="academy_nav">
    <router-link :to="{name:'academyProfile'}">학원 프로필</router-link>
    <router-link :to="{name: 'academyPosting'}">등록한 교육 공고</router-link>
    <router-link :to="{name: 'signout'}">회원 탈퇴하기</router-link>
  </div>
</template>

<script>
export default {
  name: 'AcademyNav',

}
</script>

<style>
.academy_nav{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border: 1px solid black;
}
</style>