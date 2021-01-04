<template>
  <form>
    <div class="form">
      <div class="form-group">
        <label>Titulo: </label>
        <input class="form-control" type="text" v-model="nota.titulo" :readonly="estadoForm == 'ver'" />
      </div>
      <fieldset>
        <legend>Autor:</legend>
        <div class="form-group">
          <label>Nombre: </label>
          <input class="form-control" v-model="nota.autor" :readonly="estadoForm == 'ver'" />
        </div>

        <div class="form-group">
          <label>Documento: </label>
          <input type="number" class="form-control" v-model="nota.dni" :readonly="estadoForm == 'ver'" />
        </div>
      </fieldset>

      <div class="form-group">
        <label>Texto: </label>
        <textarea class="form-control" v-model="nota.descripcion" :readonly="estadoForm == 'ver'"></textarea>
      </div>
    </div>
    <p>
      <button type="button" class="btn btn-primary" @click="guardar" :disabled="!esValido()" v-show="estadoForm != 'ver'">
        Guardar
      </button>
    </p>
    <p>
      <button type="button" class="btn btn-secondary" @click="volver">
        Volver
      </button>
    </p>
    
  </form>
</template>

<script>
import axios from "axios";

export default {
  name: "detalle",
  data() {
    return {
      estadoForm: "",
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
    esValido(){
      return this.nota.titulo.length > 3 
        && this.nota.autor.length > 3 
        && this.nota.dni.length == 8 
        && this.nota.descripcion.length > 3;
    },
    cargaInicial(){
      this.nota = this.$route.params.nota
    }    
  },
  mounted(){
    this.estadoForm =this.$route.params.state
    if(this.estadoForm == "ver" || this.estadoForm == "editar"){
      this.cargaInicial()      
    }      
  }
};
</script>

<style>
</style>