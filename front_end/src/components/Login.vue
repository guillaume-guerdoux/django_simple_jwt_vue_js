<template>
  <div class="row">
    <div class="col-12">
       {{ isAuthenticated }}
       {{ token }}
       <b-form v-if="!isAuthenticated">
         <b-form-input required v-model="username" type="text" placeholder="Identifiant"/>
         {{ username }}
         <b-form-input required v-model="password" type="password" placeholder="Password"/>
         <hr/>
         <b-button @click='login' class="primary">Login</b-button>
       </b-form>

       <b-button v-else @click='logout' class="danger">Logout</b-button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data: function () {
    return {
      username: '',
      password: ''
    }
  },
  computed: {
    isAuthenticated () {
      return this.$store.getters.isAuthenticated
    },
    token () {
      return this.$store.state.jwt
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
   logout: function () {
     this.$store.dispatch('removeToken').then((res) => {
       this.$router.push('/login')
     })
   }
  }
}
</script>
