<template>
  <div class="signup_container">
    <div class="signup">
      <h1>교육회원으로 가입하기</h1>
    <form @submit.prevent="signup(credentials)">
      <div>
        <label for="username"> </label>
        <input  
          v-model="credentials.username" 
          type="text" id="username" 
          placeholder="ID를 입력해주세요"
          required/>
      </div>
      <div>
        <label for="password1"></label>
        <input 
          v-model="credentials.password1" 
          type="password" id="password1" 
          placeholder="비밀번호를 입력해주세요"
          required />
      </div>
      <div>
        <label for="password2"></label>
        <input 
          v-model="credentials.password2" 
          type="password" id="password2" 
          placeholder="비밀번호를 재입력 해주세요"
          required 
          />
      </div>
      <div>
        <label for="tel"></label>
        <input 
          v-model="credentials.tel" 
          type="text" id="tel" 
          placeholder="전화번호 입력해주세요."
          required 
          />
      </div>
      <div>
        <label for="email"></label>
        <input 
          v-model="credentials.email" 
          type="text" id="email" 
          placeholder="E-mail을 입력해주세요"
          required 
          />
      </div>
      <div>
        <label for="CEO"></label>
        <input 
          v-model="credentials.CEO" 
          type="text" id="CEO" 
          placeholder="CEO을 입력해주세요"
          required 
          />
      </div>
      <div>
        <label for="location"></label>
        <input 
          v-model="credentials.location" 
          type="text" id="location" 
          placeholder="회사 주소을 입력해주세요"
          required 
          />
      </div>
      <div>
        <label for="site"></label>
        <input 
          v-model="credentials.site" 
          type="text" id="site" 
          placeholder="회사 홈페이지 주소를 입력해주세요"
          required 
          />
      </div>
      <div>
        <button>Signup</button>
      </div>
    </form>
    </div>
  </div>
</template>

<script>
  import { mapActions } from 'vuex'
  

  export default {
    name: 'AcademySignupView',

    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',
          tel: '',
          email: '',
          location: '',
          CEO: '',
          site: '',
          is_company: false,
          is_jobseeker: false,
          is_academy: true,
        }
      }
    },

    methods: {
      ...mapActions(['signup'])
    },
  }
</script>

<style>
.signup_container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 660px;
  background-color: #0009;
  border-radius: 5px;
  box-sizing: border-box;
  width: 100%;
  margin: auto;
  max-width: 450px;
  padding: 60px 68px 40px;
  margin-bottom: 100px;
}
.signup_container .signup{
  display: flex;
  flex-direction: column;
  max-width: 450px;
  width: 100%;
  align-items: center;
}




.signup_container .signup h1{

  color: white;
  font-size: 30px;
  margin-bottom: 28px;
}
.signup_container .signup input{
  background: #333;
border-radius: 4px;
border: 0;
color: white;  
width: 230px;
height: 30px;
line-height: 40px;
padding: 5px 20px;
margin-bottom: 20px;
}

.signup_container .signup button{
  background: lightskyblue;
  border-radius: 4px;
  font-size: 16px;
  font-weight: bold;
  margin: 24px 0 12px;
  padding: 16px;
  border: 0;
  color: white;
  cursor: pointer;
  width: 255px;   
}
</style>
