<template>
  <div class="signup_container">
    <div class="signup">
      <h2>구인회원으로 가입하기</h2>
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
        <label for="tell"></label>
        <input 
          v-model="credentials.tell" 
          type="text" id="tell" 
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
        <label for="numberOfWorkers"></label>
        <input 
          v-model="credentials.numberOfWorkers" 
          type="text" id="numberOfWorkers" 
          placeholder="근무자수을 입력해주세요"
          required 
          />
      </div>
      <div>
        <label for="yearOfEstablishment"></label>
        <input 
          v-model="credentials.yearOfEstablishment" 
          type="text" id="yearOfEstablishment" 
          placeholder="설립년도을 입력해주세요"
          required 
          />
      </div>
      <div>
        <label for="industry"></label>
        <input 
          v-model="credentials.industry" 
          type="text" id="industry" 
          placeholder="산업군를 입력해주세요"
          required 
          />
      </div>
      <div>
        <label for="companySize"></label>
        <input 
          v-model="credentials.companySize" 
          type="text" id="companySize" 
          placeholder="회사규모를 입력해주세요"
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
    name: 'CompanySignupView',

    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',
          tell: '',
          email: '',
          location: '',
          numberOfWorkers: '',
          yearOfEstablishment: '',
          industry: '',
          companySize: '',
          is_company: true,
          is_jobseeker: false,
          is_academy: false,
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




.signup_container .signup h2{
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
