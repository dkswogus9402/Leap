<template>
  <div>
    <h1>교육 등록 완료 페이지</h1>
    <h4>무슨무슨 교육 등록이 완료되었습니다!</h4>
    <router-link :to="{name:'main'}">메인으로 돌아가기</router-link>
    <br>
    <router-link :to="{name:'jobSeekerProfile'}">내 프로필 보기</router-link>
  </div>
</template>

<script>
export default {
  name: 'EduApplyComplete',

}
</script>

<style>

</style>