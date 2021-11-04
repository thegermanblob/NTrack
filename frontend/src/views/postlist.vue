<template>
    <div class="container">
        <createPost />
        <div v-if="errorMsg" class="alert alert-danger fade show" role="alert">
              <strong>{{ errorMsg }}</strong> 
        </div>
        
        <div v-for="post in posts" :key="post.id">
            <router-link :to="{ name: 'singleBlog', params: { id: post.id } }">
                <h3>{{post.id}}. {{post.title}}</h3>
            </router-link>
            <p>{{post.body}}</p>
            <hr>
        </div> 
    </div>
</template>

<script>
    import createPost from "@/components/createpost.vue";
    import axios from 'axios';

    export default 
    {
        name: 'postList',
        components: {
            createPost
        },
        created() {
             this.getPosts()
        },
        data() {
            return {
                posts: [],
                errorMsg: ''
            }
        },
        methods: {
            getPosts() {
                axios.get('https://jsonplaceholder.typicode.com/posts/')
                .then((response) => {
                    console.log(response.data)
                    this.posts = response.data
                })
                .catch((error) => {
                    console.log(error),
                    this.errorMsg = 'There was an error getting the list.  Try later!'
                })
            },            
        },
    }
</script>

<style scoped>
    .container
    {
        color: white;
    }

    .container hr {
        margin-bottom: 50px;
    }

    .container a {
        color:cyan;
    }

    .container a:hover {
        color:turquoise;
    }

</style>