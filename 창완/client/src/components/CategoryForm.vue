<template>
  <div>
    <h3>사무 IT 강의</h3>
    <div class="eduform_box">
    <edu-form></edu-form>
    <edu-form></edu-form>
    <edu-form></edu-form>
    </div>
  </div>
</template>

<script>
import EduForm from '@/components/EduForm.vue'
export default {
  name:'CategoryForm',
  components: { EduForm },

}
</script>

<style>
.eduform_box{
  display: flex;
  justify-content: space-evenly;
}
</style>