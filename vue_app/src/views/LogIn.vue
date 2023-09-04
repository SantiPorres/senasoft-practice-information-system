<template>
  <div class="page-log-in d-flex align-items-center py-4 bg-dark h-100">
    <main class="form-signin w-100 m-auto">          
      <div class="col">
        <img src="../assets/logo.png" width="64" alt="">
        
        <h2 class="title">Information system</h2>
        <h4 class="subtitle">Environmental - Security and health at work</h4>
        <form @submit.prevent="submitForm">
          <div class="my-5">
            <div class="form-floating mb-3">
              <input type="text" id='floatingInput' class="form-control" v-model="username">
              <label for="floatingInput">Username</label>
            </div>
            <div class="form-floating mb-3">
              <input type="password" id="floatingInput" class="form-control" v-model="password">
              <label for="floatingInput">Password</label>
            </div>
            
            <button class="btn btn-outline-secondary w-100 py-3"><h5 class="my-0">Log In</h5></button>
          </div>

          <div v-if="errors.length" class="toast-container position-static">
            <div v-for="error in errors" v-bind:key="error" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
              <div class="toast-body">
                {{ error }}
              </div>
            </div>
          </div>
        </form>
      </div>
    </main>
  </div>
</template>

<script>
import axios from 'axios';
import { Toast } from 'bootstrap';

export default {
  name: 'LogIn',
  data() {
    return {
      username: '',
      password: '',
      errors: []
    }
  },
  mounted() {
    document.title = 'Log In | Information system'
  },
  methods: {
    async submitForm() {
      axios.defaults.headers.common["Authorization"] = ""

      localStorage.removeItem('token')

      const formData = {
        username: this.username,
        password: this.password
      }

      await axios
        .post('/api/token/login', formData)
        .then(response => {
          const token = response.data.auth_token

          this.$store.commit('setToken', token)

          axios.defaults.headers.common['Authorization'] = "Token " + token

          localStorage.setItem('token', token)

          const toPath = this.$route.query.to || '/admin'

          this.$router.push(toPath)
        })
        .catch(error => {
          if (error.response) {
            console.log('if error.response');
            for (const property in error.response.data) {
              this.errors.push(`${property}: ${error.response.data[property]}`)
            }
          }
          else if (error.request) {
            console.log('if error.request');
            this.errors.push('No response received from server. Please try again');
            console.log(this.errors)
          }
          else {
            console.log('else');
            this.errors.push('Something went wrong. Please try again')
          }
        })
    }
  }
}
</script>

<style>

.title {
  color: #fff;
}

.subtitle {
  color: #fff8;
}

.form-signin {
  max-width: 500px;
  padding: 1rem;
}

</style>