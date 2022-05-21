<template>
<div>
  <router-link :to="{name: 'jobDetail'}">
  <div class="posting_box">
    <h4>공고 제목</h4>
    <h5>채용 유형</h5>
  </div>
  </router-link>
  </div>
</template>

<script>
export default {
  name: 'postingBox',
}
</script>

<style>
.posting_box{
  border: 1px solid black;
  display: flex;
  flex-direction: column;
}
</style>