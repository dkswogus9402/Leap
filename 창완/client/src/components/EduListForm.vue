<template>
  <div>
    <h4>등록 가능한 교육</h4>
    <router-link :to="{ name:'eduDetail' }">
    <div class="edu_box">
      <h5>대한 중장비 운전학원</h5>
      <h5> 내용: 지게차운전기능사</h5>
      <h5>훈련기간 : 군대기간</h5>
    </div>
    </router-link>
    <router-link :to="{ name:'eduDetail' }">
    <div class="edu_box">
      <h5>대한 중장비 운전학원</h5>
      <h5> 내용: 지게차운전기능사</h5>
      <h5>훈련기간 : 군대기간</h5>
    </div>
    </router-link>
    <router-link :to="{ name:'eduDetail' }">
    <div class="edu_box">
      <h5>대한 중장비 운전학원</h5>
      <h5> 내용: 지게차운전기능사</h5>
      <h5>훈련기간 : 군대기간</h5>
    </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name:'EduListForm',

}
</script>

<style>
.edu_box{
  display: flex;
  border:1px solid black;
  justify-content:space-evenly
}
</style>