<template>
  <div>
    <div class="title">
      <div>(주) 재현회사의 채용정보 |</div>
      <router-link :to="{name:'academyCategory'}"><div> 이수 교육 정보 보러가기 |</div></router-link>
      <router-link :to="{name: 'jobApply'}"><div> 지원하러가기</div></router-link>
    </div>
    <hr>
    <div>
      <h5>사무원 채용</h5>
      <p>담당업무 : 물퍼기</p>
      <h4>교육 이수 및 자격증 우대 목록</h4>
      <router-link :to="{name:'academyCategory'}"><div>링크로 들어가는</div></router-link>
      <router-link :to="{name:'academyCategory'}"><div>자격증</div></router-link>
    </div>
    <div>
      <h5>근무조건</h5>
      <h6>설명~~</h6>
    </div>
  </div>
</template>

<script>
export default {
  name: 'JobDetailForm',

}
</script>

<style>
.title{
  display: flex;
  justify-content: center;
  
}
</style>