<template>
  <div class="apply_box">
    <h3>이동근 님에게 제안하기</h3>
    <div>
      <input type="checkbox"> <p>등록된 공고 정보와 동일합니다</p>
      <div>사진칸</div>
      <p>회사 : (주)재현회사</p>
      <p>여러 정보~</p>
    </div>
    <router-link :to="{name:'jobOfferComplete'}">
    <button>제안하기</button>
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
