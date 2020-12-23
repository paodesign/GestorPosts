<template>
  <div id="app">
    <h1>{{ titulo }}</h1>
    <div v-for="post in listaPosts">
      <h4>{{ post.titulo.toUpperCase()}}</h4>
      <p>{{post.descripcion}}</p>
      <p>{{post.autor}}  <span>{{new Date(post.fecha).toLocaleDateString()}}</span></p>  
    </div>
      <!-- <ul>
    <li>

    </li>
    </ul> -->

    <!-- <div class="form">
    <div class="form-group">
      <label>Titulo: </label>
      <input class="form-control" type="text" v-model="nota.titulo">
    </div>
  </div>
  <div class="form">
    <div class="form-group">
      <label>Texto: </label>
      <textarea class="form-control" v-model="nota.texto"></textarea>
    </div> 
    
  </div>-->
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "app",
  data() {
    return {
      titulo: "Gestión de Posts",
      listaPosts: [],
      nota: {
        titulo: "",
        texto: "",
        autor: "",
      },
    };
  },
  methods: {
    getMensaje() {
      const path = "http://192.168.1.10:5000/api/posts";
      axios
        .get(path)
        .then((posts) => {
          this.listaPosts = posts.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  mounted () {
    this.getMensaje();
  },
  // mounted () {
  //   axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';
  //   // var optionAxios = {
  //   //         headers: {
  //   //             'Content-Type': 'application/x-www-form-urlencoded',
  //   //             'Access-Control-Allow-Origin': '*'
  //   //         }
  //   //     }
  //   axios
  //     .get('http://192.168.1.10:5000/api/posts',{
  //  headers: {
  //         // remove headers
  //       }
  //     } )
  //     .then(response => (console.log(response)))
  //     .catch(console.error)
  // },
  //   methods: {
  //     agregarNota:function(){
  //       let {texto, titulo} = this.nota;
  //       this.notas.push({
  //         texto,
  //         titulo,
  //         fecha: new Date(Date.now()).toLocaleDateString()
  //       })
  //     },
  //     eliminarNota: function(index){
  //       this.notas.splice(index, 1)
  //     }
  //   }
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
