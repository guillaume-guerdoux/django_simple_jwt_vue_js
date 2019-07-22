<template>
  <div class="row">
    <div class="col-12">
      {{ token }}
      <div v-if='!isAuthenticated'>
        <p> Vous n'êtes pas connecté </p>
        <b-button class="primary" @click='goToLogin'> Connectez-vous</b-button>
      </div>
      <div v-else>
        <ul id="example-2">
          <li v-for="(item, index) in movies">
            {{ index }} - {{ item.name }} - {{ item.description }}
          </li>
        </ul>

        <b-form>
          <b> Rajouter un film </b>
          <b-form-input required v-model="newMoviesName" type="text" placeholder="Titre du film"/>
          <b-form-textarea required v-model="newMoviesDescription" type="text" placeholder="Description du film"/>
          <b-form-input required v-model="newMoviesStars" type="int" placeholder="Nombre d'étoiles"/>
          <b-button class="primary" @click='addMovie'> Ajouter ce film </b-button>
        </b-form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Movies',
  data: function () {
    return {
      movies: {},

      newMoviesName: '',
      newMoviesDescription: '',
      newMoviesStars: '',
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
  mounted: function() {
    this.getAllMovies()
  },
  methods: {
    getAllMovies () {
      if (!this.isAuthenticated) {
        this.movies = {}
      }
      else {
        console.log('authenticatded')
        console.log(JSON.parse(this.token).access)
        var headers = {
            'Authorization': 'Bearer '+ JSON.parse(this.token).access,
            'Content-Type': 'application/json',
        }
        axios.get(
          'http://localhost:8000/api/movies/',
          {
            'headers': headers
          })
          .then((response)=>{
            this.movies = response.data
            console.log('ok')
            console.log(response.data)
          })
          .catch((error)=>{
            console.log("EROOR")
            console.log(error);
          })
      }
    },
    addMovie () {
    if (!this.isAuthenticated) {
      console.log('not connected')
    }
    else {
      console.log('authenticatded')
      console.log(JSON.parse(this.token).access)
      var headers = {
          'Authorization': 'Bearer '+ JSON.parse(this.token).access,
          'Content-Type': 'application/json',
      }
      axios.post(
        'http://localhost:8000/api/movies-create/',
        {
          'name': this.newMoviesName,
          'description': this.newMoviesDescription,
          'stars': this.newMoviesStars
        },
        {
          'headers': headers,

        })
        .then((response)=>{
          this.getAllMovies()
          console.log('ok')
          console.log(response.data)
        })
        .catch((error)=>{
          console.log("EROOR")
          console.log(error);
        })
      }
    },
    goToLogin () {
      this.$router.push('/login')
    }
  }
}
</script>
