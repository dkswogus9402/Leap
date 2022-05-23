<template>
  <div>
    <h1>포스팅 완료 페이지</h1>
    <h5> ~~ 공고가 등록되었습니다~!</h5>
    <router-link :to="{name: 'main'}"> 메인으로 가기  |</router-link>
    <router-link :to="{name: 'jobPosting'}"> 계속해서 공고 등록하기</router-link>
  </div>
</template>

<script>
export default {
  name: 'PostingComplete',

}
</script>

<style>

</style>