<template>
  <div class="hero is-fullheight is-info is-bold">
  <div class="hero-body">
  <div class="container">

    <h1 class="title has-text-centered">Add Airport</h1>
    <div class="box">

      <!-- our signup form ===================== -->
      <ul>
        <div class="form-group">
          <label class="col-form-label" for="customerID">Airport id:</label>
          <input type="text" v-model="airport_id" class="form-control" placeholder="Airport id" id="airport_id">
        </div>
        <div class="form-group">
          <label class="col-form-label" for="manufac">Airport Name:</label>
          <input type="text" v-model="airport_name" class="form-control" placeholder="Airport Name" id="airport_name">
        </div>
        <div class="form-group">
          <label class="col-form-label" for="maxSeats">City:</label>
          <input type="text" v-model="city" class="form-control" placeholder="City" id="city">
        </div>
        <div class="form-group">
          <label class="col-form-label" for="typ">State:</label>
          <input type="text" v-model="state" class="form-control" placeholder="State" id="state">
        </div>
        <button type="button" v-on:click="createpost ()" class="btn btn-primary">Submit</button>
        {{airport_id}}
        {{airport_name}}
        {{city}}
        {{state}}
      </ul>

    </div>

  </div>
  </div>
  </div>

</template>
<script>
import axios from 'axios'
export default {
  name: 'CreateAirport',
  data () {
    return {
      airport_id: null,
      airport_name: null,
      city: null,
      state: null
    }
  },
  methods: {
    createpost () {
      axios.post('http://127.0.0.1:8000/myapp/airports/', {
        airport_id: this.airport_id,
        airport_name: this.airport_name,
        city: this.city,
        state: this.state
      }).then((response) => { window.location.href = 'http://localhost:8080/#/listairports/' }).catch((e) => {
        console.error(e)
      })
    }
  }
}
</script>
