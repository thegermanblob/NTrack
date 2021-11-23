<template>

        <form class="input-group has-search">
            <span class="fa fa-search form-control-feedback" ></span>

            <input v-model="searchQuery" type="text"

            @click="glow = true"
            @input="displayOptions"
            @keyup.enter="doSearch"
            @keyup.esc="hideOptions"          
            placeholder="Type the name of user to search" class="searchBox form-control">
            <button @click="searchQuery=''" id="resetBtn" class="resetBtn" type="reset" v-if="searchQuery">
                <span class="fa fa-close"></span>
            </button>

                <div class="options" v-show="showOptions" id='resultsList'>
                    <ul>
                    <!-- <li v-if="filteredUser.length == 0">Not found "{{ searchQuery }}"</li> -->
                    <li  v-for="(user, id) in filteredUser" v-bind:key="id">
                        
                        <router-link :to="{ name: 'userDetail', params: { userID: user.id }}" 
                        @click="selectItem(user)">
                            {{ user.name }}
                        </router-link>

                    </li>
                    </ul>
                </div>
        </form>

</template>

<script>
import axios from 'axios';

export default {
    name: 'dropDown',
    data() {
        return {
            searchQuery: '',
            glow: false,         
            showOptions: false,
            userArray: []
        }
    },
    computed: {
        filteredUser() {
            const query = this.searchQuery.toLowerCase();
            
            if (this.searchQuery == '') {
                return '';                
            }
            
            return this.userArray.filter((user) => {
                return Object.values(user).some((word) => 
                    String(word).toLowerCase().includes(query)
                );
            });
        }
    },
    methods: {
        selectItem(user) {
            this.searchQuery = user.name;
            this.showOptions = false;
            console.log('You selected: ' + user.id + ': ' + user.name);
        },
        hideOptions() {
            this.showOptions = false;
            this.glow = false;
            console.log('Focus lost, list hidden');            
        },
        displayOptions() {
            this.showOptions = true;            
            console.log('You typed: ' + this.searchQuery);
        },
        doSearch() {
            this.showOptions = false;
            console.log('Query sent: ' + this.searchQuery);        
        }
    },
    mounted() {
        axios.get("https://jsonplaceholder.typicode.com/users")
        .then((response) => { 
            console.log(response.data);
            this.userArray = response.data;
        })        
    }
};
</script>

<style scoped>

   .searchBox {        
        border:0;
        font-size: 14px;
        padding:10px;
        padding-left:38px;
        position:relative;
        width:100%;
    }

    .fa-search
    {
       position:absolute; z-index:100; 
    }

    .resetBtn {
        background:none;
        border:0;
        position:absolute; z-index:100;
        color:#999;
        right:10px;
        margin-top:8px;
    }

    .resetBtn:hover {
        color:#333;
    }

    .clearTxt {
        background: white;
        color:#999;
    }

    .clearTxt:hover {
        background: rgb(240, 239, 239);
        color:#000;
    }

    .options {
        width: 100%;
    }

    ul {
        list-style: none;
        text-align: left;
        padding-left: 0px;
        max-height: 300px;
        overflow-y: scroll; 
        overflow-x: hidden;
        border:0;
        width:100%;
        position:absolute;
    }

    li {
        width: 100%;
        border-bottom: 1px solid #ccc;        
        background: #f1f1f1;
        cursor: pointer;
    }

    li > a {
        text-decoration:none;
        color:#666;
        width:100%;
        height:100%;
        padding: 10px 10px 10px 20px;        
        display:inline-block;
    }

    li > a:hover {
        background: rgb(235, 243, 129);
        color:#000;
    }

    .glow {
        box-shadow: 0px 0px 20px rgba(255,255,255,.8);
    }


</style>
