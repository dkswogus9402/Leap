<template>
  <div>
    <h1>Leap Main 페이지입니다</h1>
    <hr>
    <div class="main_container">
      <router-link class="router_box" :to="{name : 'jobList'}"> 구직 </router-link>
      <router-link class="router_box" :to="{name : 'jobSeekerList'}"> 구인 </router-link>
      <router-link class="router_box" :to="{name : 'academyCategory'}"> 교육 </router-link>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style>
.main_container{
  display: flex;
  justify-content: space-around;
}
.router_box {
  border: 1px solid black;
  width: 150px;
  height: 150px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 50px;
}
</style>