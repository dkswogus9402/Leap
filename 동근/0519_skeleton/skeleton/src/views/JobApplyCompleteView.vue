<template>
  <div class="container">
    <h1>회사 지원 완료 페이지</h1>
    <h2>이동근 님의 지원이 완료되었습니다</h2>
    <p>~~~</p>
    <div class="post_box">
    <posting-box></posting-box>
    <posting-box></posting-box>
    </div>
    <router-link :to="{name : 'jobList'}"><p>공고 더 보러 가기</p></router-link>
  </div>
</template>

<script>
import PostingBox from '@/components/PostingBox.vue'
export default {
  name: 'JobApplyComplete',
  components: { PostingBox },

}
</script>

<style>
.container {
  border: 1px solid black;
}
.post_box {
  display: flex;
  justify-content: center;
}
</style>