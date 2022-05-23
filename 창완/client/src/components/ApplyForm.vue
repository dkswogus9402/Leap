<template>
  <div class="apply_box">
    <h3>(주) 재현회사에 지원하기</h3>
    <p>응답까지 평균 ~일 소요됩니다</p>
    <div>
      <input type="checkbox"> <p>프로필의 정보와 동일합니다</p>
      <div>사진칸</div>
      <p>이름 : 이동근</p>
      <p>여러 정보~</p>
    </div>
    <router-link :to="{name:'jobApplyComplete'}">
    <button>지원하기</button>
    </router-link>
  </div>
</template>

<script>
export default {
  name:'ApplyForm',

}
</script>

<style>
.apply_box{
  border:1px solid black
}
</style>
