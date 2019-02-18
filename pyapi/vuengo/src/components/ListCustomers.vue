<template>
<div>
  <h1>Airplane List</h1>
  <ul>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">Customer id</th>
          <th scope="col">Name</th>
          <th scope="col">Address</th>
          <th scope="col">Email</th>
          <th scope="col">Phone</th>
        </tr>
      </thead>
        <tbody>
          <tr v-for="customer in Customers" :key="customer.cust_id">
            <th scope="row">{{customer.cust_id}}</th>
            <th>{{customer.c_first_name}} {{customer.c_last_name}}</th>
            <td>{{customer.address}}, {{customer.city}}, {{customer.postal_code}}</td>
            <td>{{customer.email}}</td>
            <td>{{customer.phone}}</td>
          </tr>
        </tbody>
    </table>
    <button type="button" class="btn btn-primary">Create</button>
    <button type="button" class="btn btn-primary">Updata</button>
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
