<template>
  <div>
    <worker-nav></worker-nav>
    <h1>수강중인 교육</h1>
    <edu-form></edu-form>
  </div>
</template>

<script>
import WorkerNav from '@/components/WorkerNav.vue'
import EduForm from '@/components/EduForm.vue'
export default {
  name:'JobSeekerProcess',
  components : { WorkerNav, EduForm },
}
</script>

<style>

</style>