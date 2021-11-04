<template>
  <div class="container">
    <template v-if="clients.length > 0">
      
      <h5 class="text-center clearblack">{{ clients.length }} clients registered in total</h5>
    <table class="table table-striped table-responsive ticketlist">
      <tr class="tableheading">
        <th width="5%" class="text-center">&nbsp;</th>        
        <th>Full name</th>
        <th width="20%">Email address</th>
        <th width="20%">Phone number</th>
        <th width="20%">Date created</th>
      </tr>      
      <tr
        v-for="client in clients" :key="client._id.$oid">        
            <td>              
                <router-link :to="{ name: 'clientDetail', params: { clientID: client._id.$oid } }" class="btn btn-light btn-lg whitehover">
                <i class="far fa-file-alt"></i>
              </router-link>
            </td>            
            <td>{{ client.client_name }} {{ client.client_last_name}}</td>
            <td>{{ client.client_email }}</td>
            <td>{{ client.client_phone }}</td>
            <td>{{ client.created_at.$date }}</td>
        </tr>

    </table>
    </template>
    <template v-else>
        <div class="alert alert-info fade show text-center" role="alert">
             <i class="fas fa-hourglass-half"></i> Please wait, retrieving list
        </div>
    </template>

  </div>
</template>

<script>    
    import axios from 'axios';

    export default 
    {
        name: 'clientList',
        components: {
           
        },
        created() {
             this.listClients()
        },
        data() {
            return {
                clients: [],
                errorMsg: ''
            }
        },
        methods: {
            listClients() {
                axios.get('https://2ktpylu8p5.execute-api.us-east-2.amazonaws.com/dev/api/v1/clients')
                .then((response) => {
                    console.log(response.data)
                    this.clients = response.data
                })
                .catch((error) => {
                    console.log(error),
                    this.errorMsg = 'There was an error getting the client list.  Try later!'
                })
            }            
        },
    }
</script>

<style scoped src="../assets/css/ticketlist.css">

</style>
