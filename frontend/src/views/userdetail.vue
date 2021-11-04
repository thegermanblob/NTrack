<template>
<div id="showTicket" class="container">

    <fieldset class="myform" style="margin:auto;">
            <legend><span>User details ({{ this.fullname }})</span></legend>
            <div class="divider"></div>
            
              <!-- ALERTS SECTION START ------------------------------------------>
            
            <div v-if="errorMsg" class="alert alert-danger alert-dismissible fade show" role="alert">
              {{ errorMsg }}
              <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
            <div v-if="successMsg" class="alert alert-success alert-dismissible fade show" role="alert">
              {{ successMsg }}
              <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>


              <!----------------------- GENERAL DETAILS --------------------------------------->

        <form>                            
          <h3 class="clearwhite"><i class="fas fa-info-circle"></i> Modify general details</h3>
            <div class="row">
                <div class="col-md-6">                  
                  <div class="form-group">
                    <p class="control-label clearblack"><strong>First name:</strong> {{ user.name }}</p>      
                                  
                    <input type="text" id="userName" class="form-control" placeholder="Enter a new value to be changed">
                  </div>
                </div>
                <div class="col-md-6">                  
                  <div class="form-group">
                    <p class="control-label clearblack"><strong>Last name:</strong> {{ user.last_name }}</p>                    
                    <input type="text" id="last_name" class="form-control" placeholder = 'Enter a new value to be changed'>
                  </div>
                </div>
            </div>
            <div class="row">
                <div class="col-md-12">
                  <div class="form-group">
                    <p class="control-label clearblack"><strong>User phone number:</strong> {{ user.phone }}</p>
                    <input type="text" id="phone" class="form-control" placeholder = 'Enter a new value to be changed'>
                  </div>
                </div>
            </div>
            <div class="row">
                <div class="col-md-12">
                  <div class="form-group">
                    <p class="control-label clearblack"><strong>Email address:</strong> {{ user.email }}</p>
                    <input type="text" id="email" class="form-control" placeholder = 'Enter a new value to be changed'>                                     
                  </div>
                </div>
            </div>
            <div class="row">
                <div class="col-md-12">
                  <div class="form-group">
                    <button class="btn btn-primary"><i class="fas fa-user-check"></i> Update details</button>
                  </div>
                </div>
            </div>
          </form>
      
      </fieldset>

</div>
</template>
<script>
  import axios from 'axios';
  export default {
    props: ['userID'],
    methods: {},
    data() {
        return {
          user: [],
          fullname: '',
          errorMsg: '',
          successMsg: ''
        }
    },
    
    created() {        
        axios.get('https://2ktpylu8p5.execute-api.us-east-2.amazonaws.com/dev/api/v1/users/' + this.userID)
        .then((response) => {
            console.log(response.data);
            this.user = response.data;
            this.fullname = this.user.name + ' ' + this.user.last_name;
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