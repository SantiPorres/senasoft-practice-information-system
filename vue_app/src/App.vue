<template>
  <router-view/>
    <nav v-if="$route.name !== 'LogIn'" class="navbar navbar-expand-lg fixed-top">
      <div class="container-fluid">
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarMain" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse d-lg-flex" id="navbarMain">
          <a class="navbar-brand col-lg-3 me-0">Information system</a>
          <ul class="navbar-nav col-lg-6 justify-content-lg-center">
            <li class="nav-item p-2">
              <router-link to="/formation-areas" class="nav-item" style="color:white">Formation Areas</router-link>
            </li>
            <li class="nav-item p-2">
              <router-link to="/sub-formation-areas" class="nav-item" style="color:white">Sub Formation Areas</router-link>
            </li>
            <li class="nav-item p-2">
              <router-link to="/sub-formation-areas" class="nav-item" style="color:white">Formation Environments</router-link>
            </li>
            <li class="nav-item p-2">
              <router-link to="/sub-formation-areas" class="nav-item" style="color:white">Instructors</router-link>
            </li>
            <li class="nav-item p-2">
              <router-link to="/sub-formation-areas" class="nav-item" style="color:white">Environmental</router-link>
            </li>
            <li class="nav-item p-2">
              <router-link to="/sub-formation-areas" class="nav-item" style="color:white">Security and health at work</router-link>
            </li>
          </ul>
        </div>

      </div>
    </nav>
</template>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Play&family=Tilt+Neon&display=swap');

#app {
  font-family: 'Play', sans-serif;
  font-family: 'Tilt Neon', cursive;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #fff;
  margin: 0;
  padding: 0;
  width: 100vw;
  height: 100vh;
}

.navbar {
  background-color: #424242;
}

.navbar .container-fluid .collapse .navbar-nav .nav-item router-link {
  color: white;
}


</style>
