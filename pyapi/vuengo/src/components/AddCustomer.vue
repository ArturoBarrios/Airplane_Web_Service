<template>
  <div class="hero is-fullheight is-info is-bold">
  <div class="hero-body">
  <div class="container">

    <h1 class="title has-text-centered">Customer Registration</h1>
    <div class="box">

      <!-- our signup form ===================== -->
      <ul>
        <div class="form-group">
          <label class="col-form-label" for="customerID">Customer id:</label>
          <input type="text" v-model="cust_id" class="form-control" placeholder="Customer id" id="cust_id">
        </div>
        <div class="form-group">
          <label class="col-form-label" for="manufac">First Name:</label>
          <input type="text" v-model="c_first_name" class="form-control" placeholder="John" id="c_first_name">
        </div>
        <div class="form-group">
          <label class="col-form-label" for="maxSeats">Last Name:</label>
          <input type="text" v-model="c_last_name" class="form-control" placeholder="Smith" id="c_last_name">
        </div>
        <div class="form-group">
          <label class="col-form-label" for="typ">Address:</label>
          <input type="text" v-model="address" class="form-control" placeholder="1234 Apple St" id="address">
        </div>
        <div class="form-group">
          <label class="col-form-label" for="typ">City:</label>
          <input type="text" v-model="city" class="form-control" placeholder="Columbus" id="city">
        </div>
        <div class="form-group">
          <label class="col-form-label" for="typ">Postal code:</label>
          <input type="text" v-model="postal_code" class="form-control" placeholder="43201" id="postal_code">
        </div>
        <div class="form-group">
          <label class="col-form-label" for="typ">Email:</label>
          <input type="email" v-model="email" class="form-control" placeholder="smith.1@osu.edu" id="email">
        </div>
        <div class="form-group">
          <label class="col-form-label" for="typ">Phone:</label>
          <input type="tel" v-model="phone" class="form-control" placeholder="1234567890" id="phone">
        </div>

        <div class="form-row align-items-left">
           <div class="col-auto">
            <button type="button" v-on:click="createpost ()" class="btn btn-primary">Submit</button>
           </div>
           <div class="col-auto">
            <a href="#/listcustomers/"><button type="button" class="btn btn-primary">Back</button></a>
          </div>
        </div>

      </ul>

    </div>

  </div>
  </div>
  </div>

</template>
<script>
import axios from 'axios'
export default {
  name: 'CreateCustomer',
  data () {
    return {
      cust_id: null,
      c_first_name: null,
      c_last_name: null,
      address: null,
      city: null,
      postal_code: null,
      email: null,
      phone: null
    }
  },
  methods: {
    createpost () {
      axios.post('http://127.0.0.1:8000/myapp/customers/', {
        cust_id: this.cust_id,
        c_first_name: this.c_first_name,
        c_last_name: this.c_last_name,
        address: this.address,
        city: this.city,
        postal_code: this.postal_code,
        email: this.email,
        phone: this.phone
      }).then((response) => { window.location.href = 'http://localhost:8080/#/listcustomers/' }).catch((e) => {
        console.error(e)
      })
    }
  }
}
</script>
