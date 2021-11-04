<template>
  <div id="showTicket" class="container">
    <fieldset class="myform" style="margin:auto;">
      <legend>
        <span>Ticket details (#{{ this.printTicketNumber(ticket._id?.$oid) }})</span>
      </legend>
      <div class="divider"></div>

      <!----------------------- GENERAL DETAILS --------------------------------------->

      
        <div class="row">
          <div class="col-md-6">
            <h3 class="clearwhite">
              <i class="fas fa-info-circle"></i> General Details
            </h3>
            <div class="form-group">
              
              <p class="control-label clearblack">
                <strong>Created by:</strong> {{ ticket.created_by?.name }}
                {{ ticket.created_by?.last_name }}
              </p>
              <p class="control-label clearblack">
                <strong>Description:</strong> {{ ticket.description }}
              </p>
              <p class="control-label clearblack">
                <strong>Device:</strong> {{ ticket.device }}
              </p>
              <p class="control-label clearblack">
                <strong>Status: </strong> {{ ticket.status?.toUpperCase() }}
              </p>

              <p class="control-label clearblack">
                <strong>Client name:</strong> {{ ticket.client_id?.client_name }}
                {{ ticket.client_id?.client_last_name }}
              </p>
              <p class="control-label clearblack">
                <strong>Client phone:</strong> {{ ticket.client_id?.client_phone }}
              </p>
              <p class="control-label clearblack">
                <strong>Client email:</strong> {{ ticket.client_id?.client_email }}
              </p>
            </div>
            <div class="divider"></div>
            <!----------------------- STATUS UPDATE BLOCK ----------------------------------->
            <div class="form-group">
              <h3 class="clearwhite">
                <i class="fas fa-history"></i> Status update history</h3>
                    <form class="form-group" @submit.prevent="addStatus(this.ticketID)">

                      <div class="input-group">
                        <select v-model="this.updateData.status" class="form-select" id="inputGroupSelect04" aria-label="Example select with button addon">
                          <option selected value="">Select a new status from the list and press OK...</option>
                          <option value="Open">Open</option>
                          <option value="Progress">Progress</option>
                          <option value="Ready">Ready</option>
                          <option value="Closed">Closed</option>
                        </select>
                        <button v-on:click="addStatus(this.ticketID)" class="btn btn-outline-secondary font-weight-bold" type="button">OK</button>
                      </div>

                    </form>
              <table class="mytable table table-responsive clearblack">
                <tr>
                  <th>Status</th>
                  <th>Employee name</th>
                  <th>Date set</th>
                </tr>
                <tr v-for="statusline in ticket.status_updates"
                  :key="statusline.status">
                  <template v-if="statusline.status_change">
                    <td>{{ statusline.status_change }}</td>
                    <td>
                      {{ statusline.created_by.name }}
                      {{ statusline.created_by.last_name }}
                    </td>
                    <td>{{ formatDate(statusline.created.$date) }}</td>
                  </template>
                </tr>
              </table>

              
            </div>
          </div>
          <div class="col-md-6" style="padding-left:40px">
            <h3 class="clearwhite">
              <i class="far fa-comments"></i> Posted comments</h3>
            <!--------------------- COMMENTS ADD FORM ------------------------------>
                <form class="form-group" @submit.prevent="addComment(this.ticketID)">
                  <textarea                       
                      v-model="this.commentData.comment"
                      id="txtNewComment"    
                      maxlength="200"             
                      class="form-control"
                      rows="2"              
                      placeholder="Add a new note for this here..."
                    />
                    <div class="text-end">
                      <button type="button" v-on:click="addComment(this.ticketID)" class="btn btn-outline-secondary font-weight-bold">
                        <i class="fas fa-comment-alt"></i> Post note</button>                     
                    </div>
                </form>
       
            <!--------------------- COMMENTS LIST ------------------------------>
            <ul class="commentlist">
              <template
                class="clearblack control-label"
                v-for="commline in ticket.status_updates"
                :key="commline.created.$date">
                    <div v-if="commline.comment">
                        <li>
                            <p class="commentdesc clearblack">
                              <strong>{{ commline.created_by.name }}
                                {{ commline.created_by.last_name }}</strong> on {{ commline.created.$date }}
                            </p>
                            <p class="comment">{{ commline.comment }}</p>
                        </li>
                    </div>
              </template>
            </ul>

          </div>
        </div>
      
    </fieldset>
  
 
  </div>
</template>
<script>
import axios from "axios";
//import moment from 'moment';

export default {
  
  props: ["ticketID"],
  data() {
    return {
      ticket: [],
      updateData: {
        'status': ''
      },
      commentData: {
        'comment': ''
      },
      errorMsg: "",
      successMsg: "",
    }
  },
  created() {
      this.loadTicket(this.ticketID)
  },
  methods: 
  {
      formatDate(value) {
        if (value) {
          //return moment(String(value)).format('MMMM Do YYYY, hh:mm a');
          /*var b = value.toString().split(/\D+/);
          return new Date(Date.UTC(b[0], --b[1], b[2], b[3], b[4], b[5], b[6]));
          */
         return value;
        }
      },
      printTicketNumber(id)
      {        
        return id?.substr(0,7);
      },
      loadTicket(id) {
          console.log('Fetching ticket...');
          axios
          .get(
            "https://2ktpylu8p5.execute-api.us-east-2.amazonaws.com/dev/api/v1/ticket_full/" +
              id
          )
          .then((response) => {          
              console.log(response.data);
              this.ticket = response.data;
          })
          .catch((error) => {
            console.log(error);
            this.errorMsg = "There was an error loading this ticket. Try again!";
          });
      },
      addComment(id)  {
        if (!this.commentData.comment) {
          return;
        }
        console.log('Posting comment for ticket #' + id + '...');
        console.log(this.commentData);
        axios.put('https://2ktpylu8p5.execute-api.us-east-2.amazonaws.com/dev/api/v1/tickets/' + id, this.commentData)
                 .then(
                     response => {                                                  
                         console.log(response);                                            
                         this.commentData.comment = '';
                         this.loadTicket(id);
                         return;
                     })
                 .catch(
                     error => {                         
                         this.errorMsg = 'Error adding comment',
                         console.log(error)
                     })
      },
      addStatus(id)  {
        if (!this.updateData.status) {
          return;
        }
        console.log('Setting status for ticket #' + id + '...');
        console.log(this.updateData);
        axios.put('https://2ktpylu8p5.execute-api.us-east-2.amazonaws.com/dev/api/v1/tickets/' + id, this.updateData)
                 .then(
                     response => {                                                  
                         console.log(response);                                            
                         this.updateData.status = '';
                         this.loadTicket(id);
                         return;
                     })
                 .catch(
                     error => {                         
                         this.errorMsg = 'Error setting status',
                         console.log(error)
                     })
      }
  }
}

</script>

<style scoped>
.commentdesc {
  font-size: 12px;
  padding: 10px !important;
  color: #ccc;
}

p.comment {
  padding:5px 10px !important;
}

ul.commentlist {
  list-style: none;
  list-style-image: none;
  list-style-type: none;
  margin: 0 !important;
  padding-inline-start: 0 !important;
  padding:0 !important;
  color: white;
}

ul.commentlist li {
  padding: 0 10px 10px 0;
  
  border-bottom: 1px dotted #666 !important;
  margin:0 0 20px !important;
}


ul.commentlist li > p {
  padding:0;
  margin:0;
  
}

ul.commentlist li > p.comment {
  padding: 10px;
}

 .btn {
   color:white;
 }
</style>