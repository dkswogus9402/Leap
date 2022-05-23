<template>
  <div>
    <academy-nav></academy-nav>
    <router-link :to="{name:'eduPosting'}">공고 등록하기</router-link>
    <h1>학원 프로필</h1>
    <h5>재현 아카데미</h5>
    <h5>정보~</h5>
    <button>수정하기</button>
  </div>
</template>

<script>
import AcademyNav from '@/components/AcademyNav.vue'
export default {
  name: 'AcademyProfile',
  components: { AcademyNav },

}
</script>

<style>

</style>