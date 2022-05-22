<template>
  <div>
    <h1>교육 메인페이지(카테고리로 나뉜)</h1>
    <category-form></category-form>
    <category-form></category-form>
    
  </div>
</template>

<script>
import CategoryForm from '@/components/CategoryForm.vue'
export default {
  name: 'AcademyCategory',
  components: { CategoryForm },


}
</script>

<style>

</style>