<template>
  <div>
    <h4>해당 자격증 채용 정보</h4>
    <router-link :to="{ name:'jobDetail' }">
    <div class="certi_box">
      <h5>(주) 창완회사</h5>
      <h5> 내용: 노예구함</h5>
      <h5>훈련기간 : 군대기간</h5>
    </div>
    </router-link>
    <router-link :to="{ name:'jobDetail' }">
    <div class="certi_box">
      <h5>(주) 창완회사</h5>
      <h5> 내용: 노예구함</h5>
      <h5>훈련기간 : 군대기간</h5>
    </div>
    </router-link>
    <router-link :to="{ name:'jobDetail' }">
    <div class="certi_box">
      <h5>(주) 창완회사</h5>
      <h5> 내용: 노예구함</h5>
      <h5>훈련기간 : 군대기간</h5>
    </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name:'CertificateForm',

}
</script>

<style>
.certi_box{
  display: flex;
  border:1px solid black;
  justify-content:space-evenly
}
</style>