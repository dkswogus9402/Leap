<template>
  <div>
    <h1>구직자 리스트 메인 페이지(회사가 보는 페이지)</h1>
    <jobseeker-box></jobseeker-box>
    <jobseeker-box></jobseeker-box>
    <jobseeker-box></jobseeker-box>
    <jobseeker-box></jobseeker-box>
  </div>
</template>

<script>
import jobseekerBox from '@/components/JobseekerBox.vue'
export default {
  name: 'JobSeekerList',
  components: { jobseekerBox },

}
</script>

<style>

</style>