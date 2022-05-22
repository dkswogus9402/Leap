<template>
  <div class="edu_box">
    <router-link :to="{name:'academyList'}">
      <div>
        <h4> 파워포인트</h4>
        <h5> 학습 기간 : 2주</h5>
        <h5> 온라인 학습 </h5>
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name:'EduForm'

}
</script>

<style>
.edu_box{
  border: 1px solid black;
}
</style>