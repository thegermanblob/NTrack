<template>
<div id="showTicket" class="container">

    <fieldset class="myform" style="margin:auto;">
            
        <!----------------------- GENERAL DETAILS --------------------------------------->
                       
          <h3 class="clearwhite"><i class="fas fa-info-circle"></i> User details</h3>
            
            <!-- ALERTS SECTION START ------------------------------------------>
            
            <div v-if="errorMsg" class="alert alert-danger alert-dismissible fade show" role="alert">
              {{ errorMsg }}
              <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>

            <div class="row">
                <div class="col-md-6">                  
                  <div class="form-group">
                    <p class="control-label clearblack"><strong>Name:</strong> {{ user.name }}</p>                    
                  </div>
                </div>
                <div class="col-md-6">                  
                  <div class="form-group">
                    <p class="control-label clearblack"><strong>Address:</strong> {{ user.address.street + ', ' + user.address.suite + ' ' + user.address.city }}</p>
                  </div>
                </div>
            </div>
            <div class="row">
                <div class="col-md-6">
                  <div class="form-group">
                    <p class="control-label clearblack"><strong>User phone number:</strong> {{ user.phone }}</p>                    
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="form-group">
                    <p class="control-label clearblack"><strong>Email address:</strong> {{ user.email }}</p>                    
                  </div>
                </div>
            </div>
           
        
      
      </fieldset>

</div>
</template>
<script>
  import axios from 'axios';
  export default {
    props: ['userID'],    
    data() {
        return {
          user: [],          
          errorMsg: '',
          successMsg: ''
        }
    },
    
    created() {     
        console.log('Fetching details for id '+ this.userID +'...');
        axios.get('https://jsonplaceholder.typicode.com/users/' + this.userID)
        .then((response) => {
            console.log(response.data);
            this.user = response.data;            
        })
        .catch((error) => {
            console.log(error),
            this.errorMsg = 'There was an error loading this screen. Try again!'
        })
    }
  }
  

</script>

<style scoped>
  

</style>