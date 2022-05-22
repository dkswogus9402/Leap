<template>
  <div>
    <worker-nav></worker-nav>
    <h1>구직자 프로필</h1>
    <h5>이름 : 아 귀찮아</h5>
    <h5>나이 : 57세</h5>
    <h5> 정보 블라블라 </h5>
    <button> 수정하기 </button>
  </div>
</template>

<script>
import WorkerNav from '@/components/WorkerNav.vue'
export default {
  name: 'JobSeekerProfile',
  components: { WorkerNav },
}
</script>

<style>

</style>