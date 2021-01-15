<template>
  <div class="container">
    <form name="formNota" @submit.prevent>
      <div class="form card">
        <div class="form-group card-header">
          <label class="bold">Titulo: </label>
          <input
            id="titulo"
            class="form-control card-title"
            type="text"
            v-model="nota.titulo"
            :readonly="estadoForm == 'ver'"
            v-on:input="marcarCambio"
          />
        </div>

        <div class="form-group row">
          <label class="bold">Autores: </label>
          <div class="col-9">
            <select
              v-model="nota.autor"
              :options="listaAutores"
              class="form-control"
              @change="marcarCambio"
            >
              <option
                v-bind:value="autor"
                v-for="autor in listaAutores"
                v-bind:key="autor.dni"
              >
                {{ autor.nombre }}
              </option>
            </select>
          </div>
          <div class="col-3">
            <input
              type="button"
              @click="isModalVisible = true"
              class="btn btn-primary"
              value="Nuevo Autor"
            />
            <modal
              :titulo="'Agregar un nuevo Autor'"
              v-if="isModalVisible"
              @close="isModalVisible = false"
              @guardar="guardarAutor"
            ></modal>
          </div>
        </div>

        <div class="form-group card-text">
          <label class="bold">Texto: </label>
          <textarea
            class="form-control"
            v-model="nota.descripcion"
            :readonly="estadoForm == 'ver'"
            v-on:input="marcarCambio"
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
          :disabled="!esValido() || huboCambiosAlEditar()"
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
import Modal from "./Modal.vue";

export default {
  components: {
    Modal,
  },
  name: "detalle",
  data() {
    return {
      haCambiado: false,
      estadoForm: "",
      listaAutores: [],
      nota: {
        codigo: "",
        titulo: "",
        descripcion: "",
        fecha: "",
        autor: {},
      },
      isModalVisible: false,
    };
  },
  methods: {
    volver() {
      //con el método volver redireciona a la página anterior
      this.$router.push("/post"); //Vue crea la variable $router para que puedas navegar desde los componentes.
    },
    guardar() {
      //tiene dos comportamientos, según el estado del formulario sea "nuevo" o "editar"
      //va a guardar una nota editada o una nueva nota
      let promise; //se crea una variable promise, para guardar la referencia a la promesa y para simplificar código

      if (this.estadoForm == "editar") {
        //si el estdo del formulario es "editar": se suscribe a la promesa
        promise = axios.put(
          `http://192.168.1.10:5000/api/posts?codigo=${this.nota.codigo}`,
          this.nota,
          {
            headers: {
              "Content-Type": "application/json",
            },
          }
        ); //
      } //a través del cliente se solicita al backend que modifique(en esa dirección, la nota)y la guardamos en promise
      if (this.estadoForm == "nuevo") {
        //si el estado del formulario es "nuevo": se suscribe a la promesa
        this.nota.fecha = new Date(); // le asignamos la fecha a la nota
        promise = axios.post("http://192.168.1.10:5000/api/posts", this.nota);
      } // a taves del cliente solicitamos al backend que cree una nueva nota(en esa dirección,nota) y la guardamos en promise

      promise //contiene la refrencia a la promesa
        .then((resp) => {
          //si la respuesta fue bien
          console.log(resp.data); // escribe por consola la parte de la data de la respuesta
          this.volver(); // con el método volver redireciona a la página anterior
        })
        .catch(console.error); // si la repuesta fue mal, escribe por consola el error.
    },
    esValido() {
      // esté método realiza las validaciones del formulario
      return (
        this.nota.titulo.length > 3 && // valida que la longitud de los caracteres del titulo tenga más de 3 caracteres
        this.nota.descripcion.length > 3 // valida que la longitud de los caracteres de la descripción tenga más de 3 caracteres
      );
    },
    marcarCambio() {
      //esté método guarada si ha cambiado de estado algun input
      this.haCambiado = true;
    },
    huboCambiosAlEditar() {
      return this.estadoForm == "editar" && this.haCambiado == false;
    },
    cargaInicial() {
      //esté método carga la nota al inicio con los parametros que recibe

      const id = this.$route.params.id;

      const path = `http://192.168.1.10:5000/api/posts/${id}`;
      axios //a través del cliente se solicita al backend que traiga(esa dirección)
        .get(path)
        .then((resp) => {
          //si la respuesta fue bien
          console.log("nota por id", resp.data);
          this.nota = resp.data;
        })
        .catch((error) => {
          // si la repuesta fue mal
          console.error(error); //escribe por consola el error.
        });
    },
    cargarAutores() {
      const path = `http://192.168.1.10:5000/api/autores`;
      axios //a través del cliente se solicita al backend que traiga(esa dirección)
        .get(path)
        .then((resp) => {
          //si la respuesta fue bien
          console.log("autor por dni", resp.data);
          this.listaAutores = resp.data;
        })
        .catch((error) => {
          // si la repuesta fue mal
          console.error(error); //escribe por consola el error.
        });
    },
    guardarAutor(autor) {
      this.isModalVisible = false;
      this.listaAutores.push(autor);
      this.nota.autor = autor;
      this.marcarCambio()
    },
  },
  mounted() {
    this.cargarAutores();
    // el método mounted propio de vue  se llama despúes que se haya montado el DOM para poder acceder a los componentes reactivos,las pantallas y los elementos del DOM, y manipularlos.
    this.estadoForm = this.$route.params.state; // se guarda en el estado del formulario "estadoForm" los parametros que recibe de state
    if (this.estadoForm == "ver" || this.estadoForm == "editar") {
      //si el estado del formulario es "ver" o "editar"
      this.cargaInicial(); // se procede a realizar la carga inicial, cargar la nota al inicio con los parametros q ue recibió
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
.card {
  text-align: center;
  border: 1px solid #2c3e50;
  border-radius: 4px;
  padding-left: 8px;
  padding-right: 8px;
  margin-bottom: 50px;
  max-width: 100%;
}
</style>