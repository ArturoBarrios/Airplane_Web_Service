<template>
  <div class="hero is-fullheight is-info is-bold">
  <div class="hero-body">
  <div class="container">

    <h1 class="title has-text-centered">Customer Registration</h1>
    <div class="box">

      <!-- our signup form ===================== -->
      <form id="signup-form">
        <!-- first name -->
        <div class="field">
          <label class="label">First Name</label>
          <input type="text" class="input" name="c_first_name">
        </div>
          <!-- last name -->
        <div class="field">
          <label class="label">Last Name</label>
          <input type="text" class="input" name="c_last_name">
        </div>
          <!-- address name -->
        <div class="field">
          <label class="label">Address</label>
          <input type="text" class="input" name="address">
        </div>

        <div class="field">
          <label class="label">City</label>
          <input type="text" class="input" name="city">
        </div>

        <div class="field">
          <label class="label">Postal Code</label>
          <input type="text" class="input" name="postal_code">
        </div>

        <!-- email -->
        <div class="field">
          <label class="label">Email</label>
          <input type="email" class="input" name="email">
        </div>

        <div class="field">
          <label class="label">Phone</label>
          <input type="text" class="input" name="phone">
        </div>



        <!-- submit button -->
        <div class="field has-text-right">
          <button type="submit" class="button is-danger" @click="addCustomer(customer)">Submit</button>
        </div>
      </form>

    </div>

  </div>
  </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'app',
  data () {
    return {
      c_first_name: null,
      c_last_name: null,
      address: null,
      city: null,
      postal_code: null,
      email: null,
      phone: null,
      posts: []
    }
  },
  created() {
    this.$http.get('posts').then((response) => {
      this.posts = response.data
    })
    .catch((e) => {
      console.error(e)
    })
  },
  methods: {
    createPost () {
      this.$http.post('posts', {
        c_first_name: this.c_first_name,
        c_last_name: this.c_last_name,
        address: this.address,
        city: this.city,
        postal_code: this.postal_code,
        email: this.email,
        phone: this.phone,
      }).then((response) => {})
      .catch((e) => {
        console.error(e)
      })
    }
  }
}
</script>
