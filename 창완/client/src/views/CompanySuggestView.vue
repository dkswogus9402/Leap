<template>
  <div>
    <company-nav></company-nav>
    <router-link :to="{name:'jobPosting'}">공고 등록하기</router-link>
    <h1>Job Offer 현황</h1>
    <jobseeker-box></jobseeker-box>
  </div>
</template>

<script>
import CompanyNav from '@/components/CompanyNav.vue'
import JobseekerBox from '@/components/JobseekerBox.vue'
export default {
  name: 'CompanySuggest',
  components: { CompanyNav, JobseekerBox },

}
</script>

<style>

</style>