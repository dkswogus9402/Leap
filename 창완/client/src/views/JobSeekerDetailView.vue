<template>
  <div>
    <h1> 회사가 보는 구직자 디테일페이지</h1>
    <h3>이동근 님의 경력사항</h3>
    <h4> 업무분야 : 냉동공조</h4>
    <h5> 경력 : 12년 </h5>
    <h5>무슨 자격증 가짐</h5>
    <jobseeker-mini-detail></jobseeker-mini-detail>
  </div>
</template>

<script>
import JobseekerMiniDetail from '@/components/JobseekerMiniDetail.vue'
export default {
  name:'JobseekerDetail',
  components : { JobseekerMiniDetail },

}
</script>

<style>

</style>