<template>
  <div>
    <h1>Update Customer</h1>
    <ul>
      <div class="form-group">
        <label class="col-form-label" for="cust_id">Customer Id:</label>
        <input type="text" readonly="" class="form-control" :placeholder="cust_id" id="cust_id">
      </div>
      <div class="form-group">
        <label class="col-form-label" for="first_name">First Name:</label>
        <input type="text" v-model="c_first_name" class="form-control" :placeholder="customer.c_first_name" id="first_name">
      </div>
      <div class="form-group">
        <label class="col-form-label" for="last_name">Last Name:</label>
        <input type="text" v-model="c_last_name" class="form-control" :placeholder="customer.c_last_name" id="last_name">
      </div>
      <div class="form-group">
        <label class="col-form-label" for="address">Address:</label>
        <input type="text" v-model="address" class="form-control" :placeholder="customer.address" id="address">
      </div>
      <div class="form-group">
        <label class="col-form-label" for="city">City:</label>
        <input type="text" v-model="city" class="form-control" :placeholder="customer.city" id="city">
      </div>
      <div class="form-group">
        <label class="col-form-label" for="postal">Postal Code:</label>
        <input type="text" v-model="postal_code" class="form-control" :placeholder="customer.postal_code" id="postal">
      </div>
      <div class="form-group">
        <label class="col-form-label" for="email">Email Address:</label>
        <input type="email" v-model="email" class="form-control" :placeholder="customer.email" id="email">
      </div>
      <div class="form-group">
        <label class="col-form-label" for="phone">Phone Number:</label>
        <input type="tel" v-model="phone" class="form-control" :placeholder="customer.phone" id="phone">
      </div>

      <div class="form-row align-items-left">
         <div class="col-auto">
          <button type="button" v-on:click="createput ()" class="btn btn-primary" onclick="window.location.href='#/listcustomers'">Submit</button>
         </div>
         <div class="col-auto">
          <a href="#/listcustomers/"><button type="button" class="btn btn-primary">Back</button></a>
        </div>
      </div>

    </ul>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'UpdateCustomer',
  data () {
    return {
      cust_id: null,
      c_first_name: null,
      c_last_name: null,
      address: null,
      city: null,
      postal_code: null,
      email: null,
      phone: null,
      customer: null
    }
  },
  created () {
    this.cust_id = this.$route.params.id
  },
  mounted () {
    this.getCustomers()
  },
  methods: {
    getCustomers () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/myapp/customers/' + this.cust_id
      }).then(response => (this.customer = response.data))
    },
    createput () {
      axios.put('http://127.0.0.1:8000/myapp/customers/' + this.cust_id, {
        cust_id: this.cust_id,
        c_first_name: this.c_first_name,
        c_last_name: this.c_last_name,
        address: this.address,
        city: this.city,
        postal_code: this.postal_code,
        email: this.email,
        phone: this.phone
      }).then((response) => {}).catch((e) => { console.error(e) })
    }
  }
}
</script>

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
