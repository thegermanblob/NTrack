<template>
    <div class="container" style='margin-top:3%'>
        <div v-if="errors.length" class="alert alert-danger fade show" role="alert">
              <strong>Please correct the following error(s):</strong>              
                <ul>
                <li v-for="error in errors" :key="error.index">{{ error }}</li>
                </ul>
        </div>
        <div v-if="sucessMsg" class="alert alert-success fade show" role="alert">
              <strong>{{ sucessMsg }}</strong> 
        </div>
        
        <form class="myform" @submit.prevent="checkForm">
            <label for="userID" class="control-label">{{ formData }}</label>
            <hr>
            <div class="form-group">
                <label for="userID" class="control-label">Post user ID</label>
                <input type="text" id="userID" class="form-control" v-model="formData.userID"> 
            </div>
            <div class="form-group">
                <label for="title" class="control-label">Post Title</label>
                <input type="text" id="title" class="form-control" v-model="formData.title"> 
            </div>
            <div class="form-group">
                <label for="body" class="control-label">Post body</label>
                <input type="text" id="body" class="form-control" v-model="formData.body"> 
            </div>
            <button class="btn btn-primary">Create post</button>
        </form>
    </div>
</template>

<script>
    import axios from 'axios' 
    export default {
        name: 'createPost',
        data() {
            return {
                errors: [],                
                errorMsg: '',
                sucessMsg: '',
                formData: {
                    userID: '',
                    title: '',
                    body: '',
                }
            }
        },
        methods: {
            checkForm: function() {
                if (this.formData.userID && this.formData.title && this.formData.body) {
                    this.createPost();
                    this.errors = [];
                    return;           
                }
                this.sucessMsg = '';
                this.errors = [];
                if (!this.formData.userID) {
                    this.errors.push('User ID required');
                }
                if (!this.formData.title) {
                    this.errors.push('Title required');
                }
                if (!this.formData.body) {
                    this.errors.push('Body required');
                }
            },
            createPost() {
                 axios.post('https://jsonplaceholder.typicode.com/posts', this.formData)
                 .then(
                     response => {
                         console.log(response),
                         this.sucessMsg = 'Post inserted successfuly, please check it out at the console',
                         this.formData.userID = '',
                         this.formData.title = '',
                         this.formData.body = ''
                     })
                 .catch(
                     error => {
                         console.log(error),
                         this.errorMsg = 'Error posting data'
                     })
            }
        }
    }
</script>

<style scoped>
.myform
{
    border: 0 !important;
    margin: 40px auto 40px !important;
    background:rgba(0, 0, 0, .7);
    padding: 10px 40px 10px !important;
}
</style>