<template>
<div id="showTicket" class="container">

    <fieldset class="myform">
            <legend><span>Register a new ticket</span></legend>
            <div class="divider"></div>
      

        <form @submit.prevent="checkForm">                            
          
            <div class="row">
              <h3 class="clearwhite"><i class="fas fa-info-circle"></i> Enter a description of the service to be provided and ID of client</h3>
            </div>

            <!-------------------------- ALERTS SECTION START ------------------------>
            
            <div v-if="errors.length" class="alert alert-danger fade show" role="alert">
              <strong>Please correct the following error(s):</strong>              
                <ul>
                <li v-for="error in errors" :key="error.index">{{ error }}</li>
                </ul>
            </div>
            <div v-if="this.successMsg" class="alert alert-success alert-dismissible fade show" role="alert">
              {{ successMsg }}
              <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>

            <div class="row">
                  


                  <div class="col-md-6">                  
                  <div class="form-group">
                      <p class="control-label clearblack"><strong>Client:</strong></p>
                      <div class="input-group">
                        <select class="form-select" v-model="formData.client_id">
                          <option selected value="">Select a client to assign this service...</option>
                          <option value='6170be1ace938dab7b685232'>JOSE CRUZ</option>
                          
                        </select>                        
                      </div>
                  </div>
                </div>


            </div>
            <div class="row">
              <!--
                <div class="col-md-6">      
                  <div class="form-group">
                        <p class="control-label clearblack"><strong>Select a client:</strong></p>
                      
                        <select id="client-id" v-model="formData.client_id" class="form-select">
                            <option aria-selected="true" value="">Select a client</option>
                            <template v-for="client in clients" :key="client._id.$oid">
                                <option value={{ client._id.$oid }}>{{ client._id.$oid }} {{ client.last_name }} (Email:{{ client.email }})</option>
                            </template>                        
                        </select>
                     
                  </div> 
                </div>-->
                <div class="col-md-6">                  
                  <div class="form-group">
                      <p class="control-label clearblack"><strong>Description of issue:</strong> </p>
                      <textarea rows="2" length='200' id="description" class="form-control" v-model="formData.description" placeholder="Enter a brief summary of the service needed"></textarea>
                  </div>
                </div>
                <div class="col-md-6">                  
                  <div class="form-group">
                      <p class="control-label clearblack"><strong>Information of equipment:</strong> </p>
                      <textarea rows="2" length='200' id="device" class="form-control" v-model="formData.device" placeholder="Enter a brand, model and/or serial number"></textarea>
                    </div>
                  </div>
                                 
            </div>
            <div class="divider"></div>         
            <div class="row">
                  <div class="form-group">
                      <button class="btn btn-primary btn-outline-success newticket me-2 clearwhite">
                        <i class="fas fa-clipboard-check"></i> Create ticket
                      </button> 
                      
                      
                      <router-link to='/' class="btn btn-primary btn-outline-success newticket me-2 clearwhite">
                        <i class="far fa-arrow-alt-circle-left"></i> Go back
                      </router-link>
                  </div>
            </div>
          </form>
          </fieldset>

</div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'newTicket',
    created() {
        //this.loadClients()
    },
    data() {
        return {          
            errors: [],
            clients: [],
            errorMsg: '',
            successMsg: '',
            formData: {
                client_id: '6170be1ace938dab7b685232',
                status: 'open',
                description: '',
                device: '',
                user_id: '616f4c9ff66c2a496d7e5bd3'
            }            
        }
    },
    methods: {
        checkForm: function() {

                if (this.formData.description && this.formData.client_id && this.formData.device) {
                    this.addTicket();
                    console.log('form passed'); 
                    console.log(this.formData);   
                }
                this.successMsg = '';
                this.errors = [];

                if (!this.formData.description) {
                    console.log('Form didnt pass');
                    this.errors.push('Description of the issue is required');
                }
                if (!this.formData.client_id) {
                    console.log('Form didnt pass');
                    this.errors.push('You need to select a client from the list');
                }
                if (!this.formData.device) {
                    console.log('Form didnt pass');
                    this.errors.push('You need to specify the client\'s device');
                }
            },
            addTicket() {
              console.log(this.formData);
                     
                 axios.post('https://2ktpylu8p5.execute-api.us-east-2.amazonaws.com/dev/api/v1/tickets', this.formData)
                 .then(
                     response => {
                         console.log(response),                         
                         this.successMsg = 'New ticket added successfuly';
                         return;
                     })
                 .catch(
                     error => {
                         console.log(error),
                         this.errorMsg = 'Error adding new ticket'
                     })
            },/*
            loadClients() {                   
                  axios.get('https://2ktpylu8p5.execute-api.us-east-2.amazonaws.com/dev/api/v1/clients')
                  .then((response) => {
                      console.log(response.data);
                      this.clients = response.data;
                  })
                  .catch((error) => {
                      console.log(error),
                      this.errorMsg = 'There was an error loading client list. Try again!'
                  })
            }*/
    }        
  }
  

</script>

<style scoped>
  .commentdesc {
    font-size: 12px;
    padding:10px;
    color:#ccc;
  }

  ul.commentlist
  {
    list-style: none;
    list-style-image: none;
    list-style-type: none;
    margin:0 !important;
    padding-inline-start: 0 !important;
  }

  ul.commentlist li
  {
    padding: 10px;
    border-bottom: 1px dotted #666;
  }

  ul.commentlist li:last-child
  {
    border: 0;
  }

 ul.commentlist li > p
  {
    margin: 0;
  }

   ul.commentlist li > p.comment
  {
    padding: 10px;
  }

  .myform {
    margin:auto;
  }

  .newticket {
    background: none;
  }

</style>