<template>
  <div class="row">
    <div class="col-12">
       {{ isAuthenticated }}
       {{ token}}
       <div v-if="!isAuthenticated">
       <b-form >
         <b> Se connecter </b>
         <b-form-input required v-model="username" type="text" placeholder="Identifiant"/>
         {{ username }}
         <b-form-input required v-model="password" type="password" placeholder="Password"/>
         <hr/>
         <b-button @click='login' class="primary">Login</b-button>

         <b> S'inscrire </b>
         <b-form-input required v-model="registerFirstName" type="text" placeholder="Prénom"/>
         <b-form-input required v-model="registerLastName" type="text" placeholder="Nom"/>
         <b-form-input required v-model="registerUsername" type="text" placeholder="Identifiant"/>
         <b-form-input required v-model="registerPassword" type="password" placeholder="Password"/>
         <hr/>
         <b-button @click='register' class="primary">S'inscrire</b-button>
       </b-form>
       </div>
       <div v-else>
         <b-button @click='logout' class="danger">Logout</b-button>
       </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data: function () {
    return {
      username: '',
      password: '',

      registerFirstName: '',
      registerLastName: '',
      registerUsername: '',
      registerPassword: ''
    }
  },
  computed: {
    isAuthenticated () {
      return this.$store.getters.isAuthenticated
    },
    token () {
      return this.$store.getters.TOKEN
    }
  },
  methods: {
   login: function () {
     var username = this.username
     var password = this.password
     this.$store.dispatch('obtainToken', {username, password}).then((res) => {
       this.$router.push('/login')
     })
   },
   register: function () {
     var username = this.registerUsername
     var password = this.registerPassword
     var first_name = this.registerFirstName
     var last_name = this.registerLastName
     axios.post(
      'http://localhost:8000/api/create-users/',
      {'username':username, 'password': password, 'first_name': first_name, 'last_name': last_name }
      )
      .then((response)=>{
        console.log('ok')
        console.log(response.data)
      })
      .catch((error)=>{
        console.log("EROOR")
        console.log(error);
      })
   },
   logout: function () {
     this.$store.dispatch('removeToken').then((res) => {
       this.$router.push('/login')
     })
   }
  }
}
</script>
