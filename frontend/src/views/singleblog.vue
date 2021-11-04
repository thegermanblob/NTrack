<template>
    <div id="single-blog" class="container">
        
        <h1>Title: {{ blog.title }}</h1>
        <h3>{{ blog.id }}</h3>
        <article>{{ blog.body }}</article>
        
    </div>
</template>

<script>
import axios from 'axios';
export default {
    props: ['id'],
    
    data() {
        return    {            
            blog: [],
            errorMsg: ''
        }        
    },
    created() {
        axios.get('https://jsonplaceholder.typicode.com/posts/' + this.id)
        .then((response) => {
            console.log(response.data);
            this.blog = response.data;
        })
        .catch((error) => {
            console.log(error),
            this.errorMsg = 'There was an error  list.  Try again!'
        })
    }
}
</script>
<style scoped>
.container
    {
        color: white;
    }
    </style>