<template>
  <div id="app" class="widget">
    <h1 class="card text-white bg-dark mb-3">{{ titulo }}</h1>
    <button @click="showModal">mostrar</button>
    <router-view />
<!-- v-if="showModal"   @close="showModal = false"-->
    <modal  v-show="isModalVisible"
      @close="closeModal"></modal>
  </div>
</template>

<script>
import Modal from "./Modal.vue";
export default {
  components: {
     Modal 
     },
  name: "app",
  data() {
    return {
      titulo: "Gestión de Posts",
      // showModal: false,
      isModalVisible: false,
    };
  },
  methods: {
      showModal() {
        this.isModalVisible = true;
      },
      closeModal() {
        this.isModalVisible = false;
      }
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
