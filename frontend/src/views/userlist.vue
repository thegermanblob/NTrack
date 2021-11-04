<template>
  <div class="container">
    <template v-if="users.length > 0">
      
      <h5 class="text-center clearblack">{{ users.length }} users registered in total</h5>
    <table class="table table-striped table-responsive ticketlist">
      <tr class="tableheading">
        <th width="5%" class="text-center">&nbsp;</th>        
        <th>Full name</th>
        <th width="20%">Email address</th>
        <th width="20%">Phone number</th>
        <th width="20%">Date created</th>
      </tr>      
      <tr
        v-for="user in users" :key="user._id.$oid">        
            <td>    
                <router-link :to="{ name: 'userDetail', params: { userID: user._id.$oid } }" class="btn btn-light btn-lg whitehover">
                <i class="far fa-file-alt"></i>
              </router-link>
            </td>            
            <td>{{ user.name }} {{ user.last_name}}</td>
            <td>{{ user.email }}</td>
            <td>{{ user.phone }}</td>
            <td>{{ user.created_at.$date }}</td>
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
        name: 'userList',
        components: {
           
        },
        created() {
             this.listUsers()
        },
        data() {
            return {
                users: [],
                errorMsg: ''
            }
        },
        methods: {
            listUsers() {
                axios.get('https://2ktpylu8p5.execute-api.us-east-2.amazonaws.com/dev/api/v1/users')
                .then((response) => {
                    console.log(response.data)
                    this.users = response.data
                })
                .catch((error) => {
                    console.log(error),
                    this.errorMsg = 'There was an error getting the user list.  Try later!'
                })
            }            
        },
    }
</script>

<style scoped src="../assets/css/ticketlist.css">

</style>
