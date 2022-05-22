<template>
  <div class="login_container">
    <div class="login">
      <h1>Login</h1>
      <div>
        <label for="username"></label>
        <input type="text"
        id="username"
        v-model="credentials.username"
        placeholder="아이디를 입력해주세요">
      </div>
      <div>
        <label for="password"></label>
        <input type="password" 
        id="password"
        v-model="credentials.password"
        placeholder="비밀번호를 입력해주세요.">
      </div>       
      <button @click="login">LOGIN</button>

      <router-link :to="{ name: 'signup' }"
      class="gosignup">Signup</router-link>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'


export default {
  name: 'LoginView',

  data: function (){
    return {
      credentials: {
        username: null,
        password: null,
      }
    }
  },

    methods: {
      ...mapActions(['login'])
  },

}
</script>

<style>
.login_container {
  display: flex;
  flex-direction: column;
  justify-content:center;
  align-items: center;
  min-height: 460px;
  background-color: #0009;
  border-radius: 5px;
  box-sizing: border-box;
  width: 100%;
  margin: auto;
  max-width: 450px;
  padding: 60px 68px 40px;
  margin-bottom: 100px;
}
.login_container .login{
  display: flex;
  flex-direction: column;
  max-width: 450px;
  width: 100%;
  align-items: center;
}
.login_container .login h1{
  font-family: 'Bebas Neue', cursive;
  color: white;
  font-size: 32px;
  margin-bottom: 28px;
}
.login_container .login input{
  background: #0009;
border-radius: 4px;
border: 0;
color: white;  
height: 40px;
line-height: 40px;
padding: 5px 20px;
margin-bottom: 20px;
}

.login_container .login button{
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
.login_container .login span{
  color: lig;
}
.login_container .login .gosignup {
  text-decoration: none;
  color: white;
}
</style>