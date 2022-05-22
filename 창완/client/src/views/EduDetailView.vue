<template>
  <div>
    <h1>교육 디테일 페이지</h1>
    <div class="edu_header">
      <h5>대형 중장비 운전학원</h5>
      <router-link :to="{name: 'academyList'}">다른 교육장 알아보기</router-link>
      <router-link :to="{name: 'eduApply'}">교육 신청하기</router-link>
    </div>
    <hr>
    <edu-detail-form></edu-detail-form>


  </div>
</template>

<script>
import EduDetailForm from '@/components/EduDetailForm.vue'
export default {
  name: 'EduDetail',
  components: { EduDetailForm },

}
</script>

<style>
.edu_header{
  display: flex;
  justify-content: space-evenly;
  align-items: center;
}
</style>