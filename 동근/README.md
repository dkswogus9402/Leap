### 매일 일지

---

#### 0517~0518 (기초 명세 작성)

전체적인 figma와 router, component에 대한 명세를 작성했다.

청사진이지만, 필요한 기능을 최대한 넣으려고 노력했지만, component와 같이 구체적인 부분에서

부족함이 보였다. 차후 수정이 필요하다



#### 0519(server단 company 공고 구현)

server단의 공고 CRUD를 구현해야한다.

1. 로그인하지 않았을 경우 글을 쓸 수 없다
2. 지금 로그인한 유저가 회사 계정인지 확인이 필요
3. POST 요청으로 글을 쓴 뒤 JSON 파일로 잘 보내지는지 확인 필요
4. 또한 DB에 저장되는지 확인 필요
5. 그렇게 생성된 공고 리스트들이 JSON으로 잘 보내지는지 확인 필요

다중 유저모델을 사용함에 따라서,  몇 가지 문제가 있었다.



2번 사항에서 `if request.user` 확인 과정에서 출력값은 같지만, 서로 같지 않다는 결과를 받았다.

이유는 다중유저모델을 구현함에 따라 서로 다른 class에 배정되었기 때문이었다. 

str으로 감싸서 해당 문제를 해결할 수 있었다.



Postman을 좀 더 익숙하게 사용할 수 있게 되었다.



### 0519~0521(front단 skeleton 구축)

1. vuex, router, persistedstate 설정'

   ```shell
   $ vue create skeleton	
   $ cd skeleton
   $ vue add router
   $ vue add vuex
   $ npm i vuex-persistedstate
   ```

   [store/index.js]

   ```javascript
   import Vue from 'vue'
   import Vuex from 'vuex'
   // persistedState 사용을 위해 import 추가
   import createPersistedState from 'vuex-persistedstate'
   
   Vue.use(Vuex)
   
   export default new Vuex.Store({
     // persistedState 사용을 위해 plugin 추가
     plugins: [
       createPersistedState(),
     ],
   	...
   })
   
   ```

2. Router 구축

3. 각 View와 component 구분 필요

4. 구분 후 용도에 맞게 구성하기(데이터는 나중에 받아오기)

[의논필요]

뒤로가기나 새로고침을 하는 경우, 무조건 메인페이지로 돌아가는 문제가 있음

짐작가는부분 => 링크 연결시 pk값을 줘야하는 등 디테일 페이지에서 그런점을 봐서 아직 pk를 안 넘겨줘서 그런듯? 
