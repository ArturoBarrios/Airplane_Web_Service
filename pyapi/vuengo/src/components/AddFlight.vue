<template>
  <div class="hero is-fullheight is-info is-bold">
  <div class="hero-body">
  <div class="container">

    <h1 class="title has-text-centered">Customer Registration</h1>
    <div class="box">

      <!-- our signup form ===================== -->
      <ul>
        <div class="form-group">
          <label class="col-form-label" for="customerID">Flight id:</label>
          <input type="text" v-model="flight_id" class="form-control" placeholder="Flight id" id="flight_id">
        </div>
        <div class="form-group">
          <label class="col-form-label" for="manufac">Airplane id:</label>
          <input type="text" v-model="airplane_id" class="form-control" placeholder="Airplane id" id="airplane_id">
        </div>
        <div class="form-group">
          <label class="col-form-label" for="maxSeats">Customer id:</label>
          <input type="text" v-model="cust_id" class="form-control" placeholder="Customer id" id="cust_id">
        </div>
        <div class="form-group">
          <label class="col-form-label" for="typ">Departure time:</label>
          <input type="text" v-model="scheduled_dep_time" class="form-control" placeholder="Departure time" id="scheduled_dep_time">
        </div>
        <div class="form-group">
          <label class="col-form-label" for="typ">Arrival time:</label>
          <input type="text" v-model="scheduled_arriv_time" class="form-control" placeholder="Arrival time" id="scheduled_arriv_time">
        </div>
        <div class="form-group">
          <label class="col-form-label" for="typ">Departure airport:</label>
          <input type="text" v-model="departure_airport" class="form-control" placeholder="Departure Airport" id="departure_airport">
        </div>
        <div class="form-group">
          <label class="col-form-label" for="typ">Arrival Airport:</label>
          <input type="text" v-model="arrival_airport" class="form-control" placeholder="Arrival Airport" id="arrival_airport">
        </div>
        <button type="button" v-on:click="createpost ()" class="btn btn-primary">Submit</button>
        {{flight_id}}
        {{airplane_id}}
        {{cust_id}}
        {{scheduled_dep_time}}
        {{scheduled_arriv_time}}
        {{departure_airport}}
        {{arrival_airport}}
      </ul>

    </div>

  </div>
  </div>
  </div>

</template>
<script>
import axios from 'axios'
export default {
  name: 'CreateFlight',
  data () {
    return {
      flight_id: null,
      airplane_id: null,
      cust_id: null,
      scheduled_dep_time: null,
      scheduled_arriv_time: null,
      departure_airport: null,
      arrival_airport: null
    }
  },
  methods: {
    createpost () {
      axios.post('http://127.0.0.1:8000/myapp/flights/', {
        flight_id: this.flight_id,
        airplane_id: this.airplane_id,
        cust_id: this.cust_id,
        scheduled_dep_time: this.scheduled_dep_time,
        scheduled_arriv_time: this.scheduled_arriv_time,
        departure_airport: this.departure_airport,
        arrival_airport: this.arrival_airport
      }).then((response) => { window.location.href = 'http://localhost:8080/#/listflights/' }).catch((e) => {
        console.error(e)
      })
    }
  }
}
</script>
