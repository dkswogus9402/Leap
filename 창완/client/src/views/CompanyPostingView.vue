<template>
  <div>
    <company-nav></company-nav>
    <router-link :to="{name:'jobPosting'}">공고 등록하기</router-link>
    <h1>등록한 공고</h1>
    <posting-box></posting-box>
  </div>
</template>

<script>
import CompanyNav from '@/components/CompanyNav.vue'
import PostingBox from '@/components/PostingBox.vue'
export default {
  name: 'CompanyPosting',
  components: { CompanyNav, PostingBox },

}
</script>

<style>

</style>