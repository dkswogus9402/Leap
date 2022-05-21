<template>
  <div >
    <router-link class="jobseeker_box" :to="{name:'jobSeekerDetail'}">
    <p>냉동 공조</p>
    <p>경력 : 12년</p>
    <p>무슨무슨 자격증</p>
    <router-link :to="{name: 'jobSeekerDetail' }">상세보기</router-link>
    <router-link :to="{name: 'jobOffer' }">제안하기</router-link>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'jobseekerBox',
}
</script>

<style>
.jobseeker_box{
  border: 1px solid black;
  display: flex;
  justify-content:space-evenly;
  align-items: center;
}
</style>