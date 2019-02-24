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
          <input type="text" v-model="c_first_name" class="form-control" placeholder="First Name" id="c_first_name">
        </div>
        <div class="form-group">
          <label class="col-form-label" for="maxSeats">Last Name:</label>
          <input type="text" v-model="c_last_name" class="form-control" placeholder="Last Name" id="c_last_name">
        </div>
        <div class="form-group">
          <label class="col-form-label" for="typ">Adress:</label>
          <input type="text" v-model="address" class="form-control" placeholder="Address" id="address">
        </div>
        <div class="form-group">
          <label class="col-form-label" for="typ">City:</label>
          <input type="text" v-model="city" class="form-control" placeholder="City" id="city">
        </div>
        <div class="form-group">
          <label class="col-form-label" for="typ">Postal code:</label>
          <input type="text" v-model="postal_code" class="form-control" placeholder="Postal Code" id="postal_code">
        </div>
        <div class="form-group">
          <label class="col-form-label" for="typ">Email:</label>
          <input type="text" v-model="email" class="form-control" placeholder="Email" id="email">
        </div>
        <div class="form-group">
          <label class="col-form-label" for="typ">Phone:</label>
          <input type="text" v-model="phone" class="form-control" placeholder="phone" id="phone">
        </div>
        <button type="button" v-on:click="createpost ()" class="btn btn-primary">Submit</button>
        {{cust_id}}
        {{c_first_name}}
        {{c_last_name}}
        {{address}}
        {{city}}
        {{postal_code}}
        {{email}}
        {{phone}}
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
      axios.put('http://127.0.0.1:8000/myapp/customers/1', {
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
