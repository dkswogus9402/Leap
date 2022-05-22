<template>
  <div>
    <h1>교육페이지(학원, 직장으로 나뉜)</h1>
    <h3>파워포인트에 대한 교육 정보</h3>
    <edu-list-form></edu-list-form>
    <certificate-form></certificate-form>


  </div>
</template>

<script>
import EduListForm from '@/components/EduListForm.vue'
import CertificateForm from '@/components/CertificateForm.vue'
export default {
  name: 'AcademyList',
  components: { EduListForm, CertificateForm },

}
</script>

<style>

</style>