<template>
  <div>
    <button
      class="btn btn-primary btn-margin"
      v-if="!authenticated"
      @click="login()">
      Log In
    </button>

    <button
      class="btn btn-primary btn-margin"
      v-if="authenticated"
      @click="privateMessage()">
      Call Private
    </button>

    <button
      class="btn btn-primary btn-margin"
      v-if="authenticated"
      @click="logout()">
      Log Out
    </button>
    {{ message }}
    <br>
  </div>
</template>

<script>
import AuthService from './auth/AuthService'
import axios from 'axios'

const API_URL = 'http://localhost:8000'
const auth = new AuthService()

export default {
  name: 'app',
  data () {
    this.handleAuthentication()
    this.authenticated = false

    auth.authNotifier.on('authChange', authState => {
      this.authenticated = authState.authenticated
    })

    return {
      authenticated: false,
      message: ''
    }
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
