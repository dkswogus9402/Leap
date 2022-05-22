<template>
  <div>
    <h1>구직 메인 페이지</h1>
    <!-- v-for 돌면서 공고 보여주기 -->
    <div class="post_box">
    <router-link :to="{name: 'jobDetail'}">
    <posting-box></posting-box>
    </router-link>

    <router-link :to="{name: 'jobDetail'}">
    <posting-box></posting-box>
    </router-link>

    <router-link :to="{name: 'jobDetail'}">
    <posting-box></posting-box>
    </router-link>  

    </div>
  </div>
</template>

<script>
import PostingBox from '@/components/PostingBox.vue'
export default {
  name: 'JobList',
  components: { PostingBox },

}
</script>

<style>
/* 임시 css입니다 */
.post_box{
  display: flex;
  justify-content: center;
  

}
.post_box div{
  margin: 15px;
  width: 150px;
  height: 150px;
}
</style>