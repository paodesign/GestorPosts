import Vue from 'vue'
import VueRouter from 'vue-router'

import App from './App.vue'
import Posts from './Posts.vue'
import Detalle from './Detalle.vue'

Vue.use(VueRouter)

const routes=[
    {
        path:'/', 
        redirect:'post'
    },
    {
        path:'/post',
        name:'post',
        component: Posts
    },
    {
        path:'/detalle',
        name:'detalle',
        component: Detalle
    }
]

const router = new VueRouter({
    mode: "history",
    routes
  });

export default router;