<template>
  <div class="mini_detail_box">
    <h4>이동근 상세 프로필</h4>
    <div>사진</div>
    <h5>나이 : 57세</h5>
    <router-link :to="{name: 'jobOffer'}">제안하기</router-link>
  </div>
</template>

<script>
export default {

}
</script>

<style>
.mini_detail_box{
  border: 1px solid black;
}
</style>