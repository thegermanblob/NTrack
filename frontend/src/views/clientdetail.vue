<template>
<div id="showTicket" class="container">

    <fieldset class="myform" style="margin:auto;">
            <legend><span>Client details for <strong>{{ this.fullname }}</strong></span></legend>
            <div class="divider"></div>
            
              <!-- ALERTS SECTION START ------------------------------------------>
            
            <div v-if="errors.length" class="alert alert-danger fade show" role="alert">
              <strong>Please correct the following error(s):</strong>              
                <ul>
                <li v-for="error in errors" :key="error.index">{{ error }}</li>
                </ul>
            </div>
            <div v-if="successMsg" class="alert alert-success alert-dismissible fade show" role="alert">
              {{ this.successMsg }}
              <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>

              <!----------------------- GENERAL DETAILS --------------------------------------->
          <!--<p class="control-label">{{ formData }}</p> -->

        <form @submit.prevent="checkForm">                        
          <h3 class="clearwhite"><i class="fas fa-info-circle"></i> Modify general client details</h3>
            <div class="row">
                <div class="col-md-6">                  
                  <div class="form-group">
                    <p class="control-label clearblack">
                      <strong>First name:</strong> {{ client.client_name }}</p>                                        
                    <input type="text" v-model="formData.client_name" id="clientName" rows="1" class="form-control" placeholder="Enter a new value to be changed">
                  </div>
                </div>
                <div class="col-md-6">                  
                  <div class="form-group">
                    <p class="control-label clearblack"><strong>Last name:</strong> {{ client.client_last_name }}</p>                    
                    <input type="text" v-model="formData.client_last_name" id="last_name" class="form-control" placeholder = 'Enter a new value to be changed'>
                  </div>
                </div>
            </div>
            <div class="row">
                <div class="col-md-6">
                  <div class="form-group">
                    <p class="control-label clearblack"><strong>Client phone number:</strong> {{ client.client_phone }}</p>
                    <input v-maska="'(###) ###-####'" type="text" v-model="formData.client_phone" id="phone" class="form-control" placeholder = '(999) 999-9999'>
                  </div>
                </div>

                <div class="col-md-6">
                  <div class="form-group">
                    <p class="control-label clearblack"><strong>Client email address:</strong> {{ client.client_email }}</p>
                    <input type="text" v-model="formData.client_email" id="email" class="form-control" placeholder = 'Enter a new value to be changed'>                                     
                  </div>
                </div>
            </div>
            <div class="divider"></div>
            <div class="row">
                  <div class="form-group">
                      <button class="btn btn-primary btn-outline-success newticket me-2 clearwhite" role="button">
                        <i class="fas fa-user-check"></i> Update details
                      </button> 
                      <router-link :to="{ name: 'clientList' }" class="btn btn-primary btn-outline-success newticket me-2 clearwhite">
                        <i class="far fa-arrow-alt-circle-left"></i> Go back
                      </router-link>
                  </div>
            </div>
            
          </form>
      
      </fieldset>

</div>
</template>
<script>
  import axios from 'axios';
  import { maska } from 'maska';

  export default {
    
    props: ['clientID'],
    directives: { maska },
    data() {
        return {
          client: [],
          errors: [],
          formData: {
                _id: {
                  $oid: this.clientID
                },
                client_name: '',
                client_last_name: '',
                client_phone: '',
                client_email: ''
          },
          fullname: '',
          errorMsg: '',
          successMsg: ''
        }
    },   
    created() {
        this.loadClient(this.clientID)
    },
    methods: {
        checkForm: function() {

                if (this.formData.client_name && this.formData.client_last_name && this.formData.client_phone && this.formData.client_email) {
                    
                    console.log('Form passed');
                    this.updateClient(this.clientID);           
                }
                this.successMsg = '';
                this.errors = [];

                if (!this.formData.client_name) {
                    console.log('Form didnt pass');
                    this.errors.push('First name is required');
                }
                if (!this.formData.client_last_name) {
                    console.log('Form didnt pass');
                    this.errors.push('Last name is required');
                }
                if (!this.formData.client_phone) {
                    console.log('Form didnt pass');
                    this.errors.push('Phone number is required');
                }
                if (!this.formData.client_email) {
                    console.log('Form didnt pass');
                    this.errors.push('A valid email address is required');
                }
        },
        updateClient(id) {          
                 axios.put('https://2ktpylu8p5.execute-api.us-east-2.amazonaws.com/dev/api/v1/clients/' + id, this.formData)
                 .then(
                     response => {
                         console.log('Saving record #' + id + '...');
                         console.log(response);
                         console.log(this.formData);
                         this.successMsg = 'Client details updated successfuly';
                         this.errors = [];
                         this.loadClient(id);
                         return;
                     })
                 .catch(
                     error => {
                         console.log(error),
                         this.errorMsg = 'Error saving client details'
                     })
        },
        loadClient(id) {                   
                  axios.get('https://2ktpylu8p5.execute-api.us-east-2.amazonaws.com/dev/api/v1/client/' + id)
                  .then((response) => {
                      console.log('Loading record #' + id + '...');
                      console.log(response.data);
                      this.client = response.data;
                      this.fullname = this.client.client_name + ' ' + this.client.client_last_name;
                  })
                  .catch((error) => {
                      console.log(error),
                      this.errorMsg = 'There was an error loading client list. Try again!'
                  })
            }
    },
    
  }
  

</script>

<style scoped>
  

</style>