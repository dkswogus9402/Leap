import Vue from 'vue'
import Vuex from 'vuex'

// 너무 많아지면 찾기 힘들거 같아서
// 용도에 따라 나누면 좋을거 같습니다.
// 공통으로 들어가는 경우 common에 넣기

import accounts from './modules/accounts'
import academy from './modules/academy'
import jobseeker from './modules/jobseeker'
import company from './modules/company'
import common from './modules/common'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: { 
    accounts, academy, jobseeker, 
    company, common},
})
