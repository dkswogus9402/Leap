<template>
  <div>
    <academy-nav></academy-nav>
    <router-link :to="{name:'eduPosting'}">공고 등록하기</router-link>
    <h1>등록한 교육</h1>
    <edu-form></edu-form>
  </div>
</template>

<script>
import AcademyNav from '@/components/AcademyNav.vue'
import EduForm from '@/components/EduForm.vue'
export default {
  name: 'AcademyPosting',
  components: { AcademyNav, EduForm },

}
</script>

<style>

</style>