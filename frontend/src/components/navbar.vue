<template>
<div>
    <div class="navbar navbar-expand-lg clearwhite">
    <div class="container-fluid">
        <router-link to='/' class="navbar-brand textwhite">
          <p class='brandname'>NTrack</p>
        </router-link>
        
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <i class="fas fa-sliders-h"></i>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          </ul>
        <ul class="nav navbar-nav navbar-right">
            <li>
                  <router-link :to="{ name: 'newTicket' }" class="btn btn-outline-success me-2 newticket">
                  <i class="fas fa-clipboard-check"></i> Create a new ticket</router-link>
            </li>
            <li class="nav-item searchBar"><dropDown /></li>
            <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle btn btn-dark textwhite" href="#" role="button" 
                     aria-expanded="false" data-bs-toggle="dropdown">
                        <i class="fas fa-user"></i>
                    </a>
                    <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
                          <li>
                          <div class="userInfo dropdown-item">
                              <p class='name' id="loggedUser"><i class="fas fa-user"></i> Staff Name</p>
                              <p class='email' id="loggedEmail">user@somedomain.com</p>
                          </div>
                          </li>
                          <li><router-link :to="{ name: 'clientList' }" class="dropdown-item">View client list</router-link></li>                        
                          <li><a class="dropdown-item" href="#">Admin settings</a></li>
                          <li><router-link :to="{ name: 'userList' }" class="dropdown-item">Manage staff accounts</router-link></li>         
                          <li><a class="dropdown-item" href="#">Profile settings</a></li>
                          <li><hr class="dropdown-divider"></li>
                          <li><a class="dropdown-item" href="#"><i class="fas fa-sign-out-alt"></i> Sign out</a></li>
                    </ul>
            </li>
        </ul>
        </div>
      </div>
</div>
<!--
<div class="container">
      <div class="row">
        <div class="col-md-4">&nbsp;</div>
        <div class="col-md-4">
          <div class="form-group has-search">
                    <span class="fa fa-search form-control-feedback"></span>
                    <input id="txtTicketID" type="text" class="form-control" placeholder="Search ticket number">
          </div>
        </div>
      </div>
</div>
-->
</div>
</template>

<script>
  import dropDown from "./dropdown.vue";
  export default {
    name: 'navBar',
    components: {
      dropDown
    }
  };
</script>

<style scoped>
    .searchBar {
      width:300px;
      margin:0 20px;
    }

    .navbar {
      margin-bottom: 3%;
    }


</style>