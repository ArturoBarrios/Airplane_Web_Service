<template>
  <div class="hero is-fullheight is-info is-bold">
  <div class="hero-body">
  <div class="container">

    <h1 class="title has-text-centered">Customer Registration</h1>
    <div class="box">

      <!-- our signup form ===================== -->
      <ul>
        <div class="form-group">
          <label class="col-form-label" for="customerID">Airplane id:</label>
          <input type="text" v-model="airplane_id" class="form-control" placeholder="Airplane id" id="airplane_id">
        </div>
        <div class="form-group">
          <label class="col-form-label" for="manufac">Manufacurer:</label>
          <input type="text" v-model="manufacturer" class="form-control" placeholder="Manufacurer" id="manufacturer">
        </div>
        <div class="form-group">
          <label class="col-form-label" for="maxSeats">Max Seats:</label>
          <input type="text" v-model="max_seats" class="form-control" placeholder="Max Seats" id="max_seats">
        </div>
        <div class="form-group">
          <label class="col-form-label" for="typ">Type:</label>
          <input type="text" v-model="type" class="form-control" placeholder="Type" id="type">
        </div>
        <button type="button" v-on:click="createpost ()" class="btn btn-primary">Submit</button>
        {{airplane_id}}
        {{manufacturer}}
        {{max_seats}}
        {{type}}
      </ul>
    </div>
  </div>
  </div>
  </div>

</template>
<script>
import axios from 'axios'
export default {
  name: 'CreateAirplane',
  data () {
    return {
      airplane_id: null,
      manufacturer: null,
      max_seats: null,
      type: null,
    }
  },
  methods: {
    createpost () {
      axios.post('http://127.0.0.1:8000/myapp/airplanes/', {
        airplane_id: this.airplane_id,
        manufacturer: this.manufacturer,
        max_seats: this.max_seats,
        type: this.type,
        phone: this.phone
      }).then((response) => { window.location.href = 'http://localhost:8080/#/listairplanes/' }).catch((e) => {
        console.error(e)
      })
    }
  }
}
</script>
