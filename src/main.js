import Vue from 'vue'
import App from './App.vue'
import router from './router'
import Posts from './Posts.vue'

new Vue({
  el:"#app",
  router,
  render: h => h(App),
  components: {
    Posts
  }

});

