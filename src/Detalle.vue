<template>
  <div class="container">
    <form>
      <div class="form card">
        <div class="form-group card-header">
          <label class="bold">Titulo: </label>
          <input
            class="form-control card-title"
            type="text"
            v-model="nota.titulo"
            :readonly="estadoForm == 'ver'"
          />
        </div>
        <div class="form-group form-control">
          <fieldset>
            <legend class="scheduler-border">Autor:</legend>
            <div class=" ">
              <label class="bold">Nombre: </label>
              <input
                class="form-control"
                v-model="nota.autor"
                :readonly="estadoForm == 'ver'"
              />
            </div>

            <div class="form-group has-warning">
              <label class="bold">Documento: </label>
              <input
                type="number"
                class="form-control control-label"
                v-model="nota.dni"
                :readonly="estadoForm == 'ver'"
              />
            </div>
          </fieldset>
        </div>

        <div class="form-group card-text">
          <label class="bold">Texto: </label>
          <textarea
            class="form-control"
            v-model="nota.descripcion"
            :readonly="estadoForm == 'ver'"
            rows="5"
          ></textarea>
          <br />
        </div>
      </div>
      <p>
        <button
          type="button"
          class="btn btn-primary"
          style="width: 18rem"
          @click="guardar"
          :disabled="!esValido()"
          v-show="estadoForm != 'ver'"
        >
          Guardar
        </button>
      </p>
      <p>
        <button
          type="button"
          class="btn btn-secondary"
          style="width: 18rem"
          @click="volver"
        >
          Volver
        </button>
      </p>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "detalle",
  data() {
    return {
      estadoForm: "",
      nota: {
        codigo: "",
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
      let promise;

      if (this.estadoForm == "editar") {
        promise = axios.put(`http://192.168.1.10:5000/api/posts?codigo=${this.nota.codigo}`, this.nota);
      }
      if (this.estadoForm == "nuevo") {
        this.nota.fecha = new Date();
        promise = axios.post("http://192.168.1.10:5000/api/posts", this.nota);
      }

      promise
        .then((resp) => {
          console.log(resp.data);
          this.volver();
        })  
        .catch(console.error);
    },
    esValido() {
      return (
        this.nota.titulo.length > 3 &&
        this.nota.autor.length > 3 &&
        this.nota.dni.length == 8 &&
        this.nota.descripcion.length > 3
      );
    },
    cargaInicial() {
      this.nota = this.$route.params.nota;
    },
  },
  mounted() {
    this.estadoForm = this.$route.params.state;
    if (this.estadoForm == "ver" || this.estadoForm == "editar") {
      this.cargaInicial();
    }
  },
};
</script>

<style>
legend.scheduler-border {
  font-size: 1em !important;
  font-weight: bold !important;
  text-align: left !important;
  background-color: rgba(230, 230, 230, 0.493);
}
label.bold {
  font-weight: bold;
}
</style>