<template>
  <div id="app" class="widget">
    <div >
      <router-link
        :to="{ name: 'detalle', params: { id: 0, state: 'nuevo' } }"
        class="btn btn-primary"
         style="width: 18rem;"
        >Agregar</router-link
      >
      <br />
      <br />
    </div>

    <div class="row justify-content-start row ">
      <div
        v-for="post in listaPosts"
        v-bind:key="post.codigo"
        class="card col-5 offset-1 card border-primary mb-3"
      >
        <div class="card-body ">
          <router-link
            :to="{
              name: 'detalle',
              params: { id: post.codigo, state: 'ver', nota: post },
            }"
          >
            <h4 class="card-title col-12">
              {{ post.titulo.toUpperCase() }}
            </h4>
          </router-link>

          <p class="card-subtitle text-truncate text-muted">
            <span>{{ post.descripcion }}</span>
          </p>
          <div class="card-text">
            <br>
            <p class="blockquote-footer">             
              {{ post.autor.nombre }} - {{ new Date(post.fecha).toLocaleDateString() }}
            </p>
          </div>
        </div>
        <p>
          <button
            type="button"
            class="btn btn-danger"
            @click="deleteNota(post.codigo)"
          >
            Eliminar
          </button>
          <router-link
            :to="{
              name: 'detalle',
              params: { id: post.codigo, state: 'editar' },
            }"
            class="btn btn-primary"
            >Editar</router-link
          >
        </p>
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
    getMensaje() {// trae los posts que esten guardados en el backend
      //this.listaPosts = [
        // {
        //   autor: "Adam",
        //   codigo: 2,
        //   descripcion:
        //     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
        //   dni: 34845678,
        //   fecha: "2020-12-18 21:40:23.123333",
        //   titulo: "Hoy es hoy",
        // },
        // {
        //   autor: "Adam",
        //   codigo: 3,
        //   descripcion:
        //     'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.\r\n\r\nThe standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.',
        //   dni: 34845678,
        //   fecha: "2020-12-18 21:41:51.043333",
        //   titulo: "Un dia mas",
        // },
        // {
        //   autor: "Timy",
        //   codigo: 4,
        //   descripcion:
        //     "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using , making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for  lorem ipsum  will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).",
        //   dni: 23456890,
        //   fecha: "2020-12-18 21:44:07.390000",
        //   titulo: "sapo de otro poso",
        // },
     // ];

      const path = "http://192.168.1.10:5000/api/posts";//se crea una constante para guardar la ruta
      axios //a través del cliente se solicita al backend que traiga(esa dirección)
        .get(path)
        .then((resp) => {//si la respuesta fue bien
          this.listaPosts = resp.data;//guardamos en el array lista de posts la parte de la data de la respuesta
        })
        .catch((error) => { // si la repuesta fue mal
          console.error(error);//escribe por consola el error.
        });
    },
    deleteNota(id) {// esté método elimina la nota 
      if (confirm("Se eliminara el post!")) {// si confirmas se elimina la nota
        const path = `http://192.168.1.10:5000/api/posts?codigo=${id}`;//se crea una costante para guardar la ruta
        axios//a través del cliente se solicita al backend que elimine(esa dirección)
          .delete(path)// elimina en esa ruta
          .then((resp) => {// si la respuesta fue bien
            console.log(resp.data);//escribe por consola la parte de la data de la respuesta
            this.getMensaje();// con esté método se vuelven a cargar las notas que tiene o refrescar los posts que recibe
          })
          .catch((error) => {// si la repuesta fue mal
            console.error(error);//escribe por consola el error.
          });
      }
    },
  },
  mounted() {// el método mounted propio de vue  se llama despúes que se haya montado el DOM para poder acceder a los componentes reactivos,las pantallas y los elementos del DOM, y manipularlos.
    this.getMensaje();// carga todos los posts que estén guardados en el backend
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
  margin-bottom: 50px;
  max-width: 100%;
}
.nota {
  padding: 5px;
}
</style>