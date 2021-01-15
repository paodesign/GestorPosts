<template>
  <div id="app" class="widget">
    <h1 class="card text-white bg-dark mb-3">{{ titulo }}</h1>
    <router-view />
  </div>
</template>

<script>
export default {
  name: "app",
  data() {
    return {
      titulo: "Gestión de Posts",
    };
  },
  methods: {},
  mounted() {},
};
</script>

<style>
#app {
  font: Arial, Helvetica, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin: 20px;
}
</style>
