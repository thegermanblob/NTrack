<template>
<div id="showTicket" class="container">

    <fieldset class="myform" style="margin:auto;">
            
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

      </fieldset>

</div>
</template>
<script>
  import axios from 'axios';
  import { maska } from 'maska';

  export default {
    
    props: ['id'],
    directives: { maska },
    data() {
        return {
          client: [],
          errors: [],
          clientData: {              
                name: '',
                username: '',
                email: '',
                catchPhrase: '',
                bs: '',
                
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
        loadClient(id) {                   
                  axios.get('https://jsonplaceholder.typicode.com/users/' + id)
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
  
  .myform {
    margin-top:10% !important;
  }

</style>