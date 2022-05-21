<template>
  <div>
    <worker-nav></worker-nav>
    <h1>제안받은 회사</h1>
    <posting-box></posting-box>
  </div>
</template>

<script>
import WorkerNav from '@/components/WorkerNav.vue'
import PostingBox from '@/components/PostingBox.vue'
export default {
  name:'JobSeekerSuggest',
  components : { WorkerNav, PostingBox },
  
}
</script>

<style>

</style>