<template>
  <navBar />
  
  <router-view/>
</template>

<script>
import navBar from "./components/navbar.vue";

export default {
  name: "App",
  components: {
    navBar    
  },
  data() {
    return {}
  },
  methods: {}
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

h1 {
  color: white;
}
</style>
