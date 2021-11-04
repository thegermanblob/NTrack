import { createRouter, createWebHistory } from 'vue-router'
import postList from '../views/postlist.vue'
import singleBlog from '../views/singleblog.vue'

import clientList from '../views/clientlist.vue'
import clientDetail from '../views/clientdetail.vue'
import newClient from '../views/newclient.vue'
import userList from '../views/userlist.vue'
import userDetail from '../views/userdetail.vue'

import ticketList from '../views/ticketlist.vue'
import ticketDetail from '../views/ticketdetail.vue'
import newTicket from '../views/newticket.vue'

const routes = [    
    {
        path: '/',
        name: 'TicketList',
        component: ticketList
    },
    {
        path: '/ticketdetail/:ticketID',
        name: 'ticketDetail',
        component: ticketDetail,
        props: true
    },
    {
        path: '/posts',
        name: 'postList',
        component: postList
    },
    {
        path: '/posts/:id',
        name: 'singleBlog',
        component: singleBlog,
        props: true
    },
    {
        path: '/clients',
        name: 'clientList',
        component: clientList,    
    },
    {
        path: '/clients/:clientID',
        name: 'clientDetail',
        component: clientDetail,
        props: true
    },
    {
        path: '/users',
        name: 'userList',
        component: userList,
        props: true
    },
    {
        path: '/users/:userID',
        name: 'userDetail',
        component: userDetail,
        props: true
    },
    {
        path: '/newticket',
        name: 'newTicket',
        component: newTicket,
        props: true
    },
    {
        path: '/newclient',
        name: 'newClient',
        component: newClient,        
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router