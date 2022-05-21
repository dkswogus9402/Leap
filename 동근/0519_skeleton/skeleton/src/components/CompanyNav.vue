<template>
  <div class="company_nav">
    <router-link :to="{name: 'companyProfile'}">회사 프로필</router-link>
    <router-link :to="{name: 'companyPosting'}">등록한 공고</router-link>
    <router-link :to="{name: 'companySuggest'}">Job Offer 현황</router-link>
    <router-link :to="{name: 'signout'}">회원 탈퇴하기</router-link>
  </div>
</template>

<script>
export default {
  name: 'CompanyNav',

}
</script>

<style>
.company_nav{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border: 1px solid black;
}
</style>