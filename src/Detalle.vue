<template>
  <form>
    <div class="form">
      <div class="form-group">
        <label>Titulo: </label>
        <input class="form-control" type="text" v-model="nota.titulo" />
      </div>
      <fieldset>
        <legend>Autor:</legend>
        <div class="form-group">
          <label>Nombre: </label>
          <input class="form-control" v-model="nota.autor" />
        </div>

        <div class="form-group">
          <label>Documento: </label>
          <input class="form-control" v-model="nota.dni" />
        </div>
      </fieldset>

      <div class="form-group">
        <label>Texto: </label>
        <textarea class="form-control" v-model="nota.descripcion"></textarea>
      </div>
    </div>
    <p>
      <button type="button" class="btn btn-primary" @click="guardar">
        Guardar
      </button>
    </p>
    <p>
      <button type="button" class="btn btn-secondary" @click="volver">
        Volver
      </button>
    </p>
    <div class="alert alert-success" role="alert" v-if="!guardar">
      <p>Se guardo el post con éxito!</p>
    </div>
  </form>
</template>

<script>
import axios from "axios";

export default {
  name: "detalle",
  data() {
    return {
      nota: {
        titulo: "",
        descripcion: "",
        autor: "",
        dni: "",
        fecha: "",
        fecha_nac: new Date(),
      },
    };
  },
  methods: {
    volver() {
      this.$router.push("/post");
    },
    guardar() {
      this.nota.fecha = new Date();
      axios
        .post("http://192.168.1.10:5000/api/posts", this.nota)
        .then((resp) => {
          console.log(resp.data);
          this.volver();
        });
    },
    
  },
};
</script>

<style>
</style>