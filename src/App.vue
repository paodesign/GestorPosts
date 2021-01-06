<template>
  <div id="app" class="widget">
    <h1>{{ titulo }}</h1>
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

</style>
