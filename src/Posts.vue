<template>
  <div id="app" class="widget">
    <div>
      <router-link to="/detalle" class="btn btn-primary">Agregar</router-link>
      <br />
      <br />
    </div>

    <div class="row justify-content-start row">
      <div
        v-for="post in listaPosts"
        v-bind:key="post.codigo"
        class="card col-5 offset-1"
      >
        <div class="card-body">
          <h4 class="card-title alert-info col-12">
            {{ post.titulo.toUpperCase() }}
          </h4>
          <router-link to="/detalle">Ver </router-link>

          <p class="card-text">{{ post.descripcion }}</p>
          <p class="card-subtitle">
            {{ post.autor }}
            <span>{{ new Date(post.fecha).toLocaleDateString() }}</span>
          </p>
        </div>
        <p><button type="button" class="btn btn-danger" @click="deleteNota(post.codigo)">Eliminar</button></p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "posts",

  data() {
    return {
      listaPosts: [],
    };
  },
  methods: {
    getMensaje() {
      const path = "http://192.168.1.10:5000/api/posts";
      axios
        .get(path)
        .then((resp) => {
          this.listaPosts = resp.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    deleteNota(id) {
     const path = `http://192.168.1.10:5000/api/posts?codigo=${id}`;
      axios
        .delete(path)
        .then((resp) => {
          console.log(resp.data);
          this.getMensaje()
        })
        .catch((error) => {
          console.error(error);
        });
       
    },
  },
  mounted() {
    this.getMensaje();
  },
};
</script>

<style>
.form {
  text-align: left;
}
.card {
  text-align: center;
  border: 1px solid #2c3e50;
  border-radius: 4px;
  padding-left: 8px;
  padding-right: 8px;
}
.nota {
  padding: 5px;
}
</style>