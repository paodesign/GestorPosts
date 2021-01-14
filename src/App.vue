<template>
  <div id="app" class="widget">
    <h1>{{ titulo }}</h1>
    <button @click="showModal = true">mostrar</button>
    <router-view />

  
  <modal v-if="showModal" @close="showModal = false"></modal>
  </div>

</template>

<script>
import Modal from './Modal.vue';
export default {
  components: { Modal },
  name: "app",
  data() {
    return {
      titulo: "Gestión de Posts",
      showModal: false
    };
  },
  methods: {
   
 },
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
