<template>
<div>
  <h1>Customer List</h1>
  <ul>
    <table class="table">
      <thead>
        <tr>
          <th></th>
          <th scope="col">Customer id</th>
          <th scope="col">Name</th>
          <th scope="col">Address</th>
          <th scope="col">Email</th>
          <th scope="col">Phone</th>
          <th></th>
        </tr>
      </thead>
        <tbody>
          <tr v-for="customer in Customers" :key="customer.cust_id">
            <td><a href="#/editcustomer/"><button type="button" class="btn btn-primary">Edit</button></a></td>
            <th scope="row">{{customer.cust_id}}</th>
            <th>{{customer.c_first_name}} {{customer.c_last_name}}</th>
            <td>{{customer.address}}, {{customer.city}}, {{customer.postal_code}}</td>
            <td>{{customer.email}}</td>
            <td>{{customer.phone}}</td>
            <td><a href="#/listcustomers/"><button type="button" v-on:click="deleteCustomer (customer.cust_id)" color="error" class="btn btn-danger">Delete</button></a></td>
          </tr>
        </tbody>
    </table>
    <a href="#/addcustomer/"><button type="button" class="btn btn-primary">Create</button></a>
    <!-- <button type="button" class="btn btn-primary" onclick="window.location.href='#/createcustomer/'">Create</button> -->
    <button type="button" class="btn btn-primary" onclick="window.location.href='#/updatecustomer/'">Update</button>
    <button type="button" class="btn btn-primary">Delete</button>
  </ul>
</div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'ListCustomers',
  data () {
    return {
      Customers: []
    }
  },
  mounted () {
    this.getCustomers()
  },
  methods: {
    getCustomers () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/myapp/customers/'
      }).then(response => (this.Customers = response.data))
    },
    deleteCustomer: function(id){
      axios.delete('http://127.0.0.1:8000/myapp/customers/'+id)
      .then((response)=>{
        this.getCustomers();
      })
      .catch((error)=>{
        console.log(error);
      });
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
