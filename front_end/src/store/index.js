import Vuex from 'vuex'
import Vue from 'vue'
import jwt_decode from 'jwt-decode'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    jwt: localStorage.getItem('user-jwt'),
    endpoints: {
      obtainJWT: 'http://localhost:8000/auth/token',
      refreshJWT: 'http:/localhost:8000/auth/token/refresh',
      verifyJWT: 'http:/localhost:8000/auth/token/verify',
    },
    status: '',
  },

  getters: {
    isAuthenticated: state => !!state.jwt,
    TOKEN: state => {
      return state.jwt
    }
  },

  mutations: {
    updateToken(state, newToken){
      localStorage.setItem('user-jwt', JSON.stringify(newToken));
      state.jwt = newToken;
    },
    removeToken(state){
      localStorage.removeItem('user-jwt');
      state.jwt = null;
    }
  },

  actions: {
    obtainToken(context, {username, password}){
      console.log('username ', username)
      console.log('password', password)

      axios.post(
      context.state.endpoints.obtainJWT,
      {
          'username': username,
          'password': password
      })
      .then((response)=>{
        console.log('ok')
        console.log(response)
        context.commit('updateToken', response.data);
      })
      .catch((error)=>{
        console.log("EROOR")
        console.log(error);
      })
    },

    removeToken(context){
      context.commit('removeToken')
    },

    refreshToken(){
      const payload = {
        token: this.state.jwt.refresh
      }
      axios.post(this.state.endpoints.refreshJWT, payload)
        .then((response)=>{
            this.commit('updateToken', response.data)
          })
        .catch((error)=>{
            console.log(error)
          })
    },
    inspectToken(){
      const token = this.state.jwt;
      if(token){
        const decoded = jwt_decode(token);
        const exp = decoded.exp
        const orig_iat = decode.orig_iat
        if(exp - (Date.now()/1000) < 1800 && (Date.now()/1000) - orig_iat < 628200){
          this.dispatch('refreshToken')
        } else if (exp -(Date.now()/1000) < 1800){
          // DO NOTHING, DO NOT REFRESH
        } else {
          // PROMPT USER TO RE-LOGIN, THIS ELSE CLAUSE COVERS THE CONDITION WHERE A TOKEN IS EXPIRED AS WELL
        }
      }
    }
  }
});
