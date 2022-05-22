<template>
  <div>
    <company-nav></company-nav>
    <router-link :to="{name:'jobPosting'}">공고 등록하기</router-link>
    <h1>회사 프로필</h1>
    <h5>(주) 창완회사</h5>
    <h5>정보~</h5>
    <button>수정하기</button>
  </div>
</template>

<script>
import CompanyNav from '@/components/CompanyNav.vue'
export default {
  name: 'CompanyProfile',
  components: { CompanyNav },

}
</script>

<style>

</style>