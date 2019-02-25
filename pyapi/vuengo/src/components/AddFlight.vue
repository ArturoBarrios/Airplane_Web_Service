<template>
  <div class="hero is-fullheight is-info is-bold">
  <div class="hero-body">
  <div class="container">

    <h1 class="title has-text-left">Flight Registration</h1>
    <div class="box">

      <!-- our signup form ===================== -->
      <ul>

        <div class="form-group">
          <label class="col-form-label" for="airplaneId">Airplane id:</label>
          <input type="text" v-model="airplane_id" class="form-control" placeholder="Airplane id" id="airplane_id">
        </div>
        <div class="form-group">
          <label class="col-form-label" for="customerId">Customer id:</label>
          <input type="text" v-model="cust_id" class="form-control" placeholder="Customer id" id="cust_id">
        </div>
        <div class="form-group">
          <label class="col-form-label" for="typ">Departure Airport:</label>
          <input type="text" v-model="departure_airport" class="form-control" placeholder="CMH" id="departure_airport">
        </div>
        <div class="form-group">
          <label for="example-date-input" class="col-form-label" >Departure Date:</label>
          <input type="date" v-model="date_dep" class="form-control" value="2011-10-15" id="date_dep">
        </div>
        <div class="form-group">
          <label class="col2-form-label" for="example-time-input">Departure Time:</label>
          <input type="time" v-model="scheduled_dep_time" class="form-control" value="13:45:00" id="scheduled_dep_time">
        </div>
        <div class="form-group">
          <label class="col-form-label" for="typ">Arrival Airport:</label>
          <input type="text" v-model="arrival_airport" class="form-control" placeholder="ICN" id="arrival_airport">
        </div>
        <div class="form-group">
          <label for="example-date-input" class="col-form-label" >Arrival Date:</label>
          <input type="date" v-model="date_arriv" class="form-control" value="2011-08-10" id="date_arriv">
        </div>
        <div class="form-group">
          <label class="col2-form-label" for="example-time-input">Arrival Time:</label>
          <input type="time" v-model="scheduled_arriv_time" class="form-control" value="19:30:00" id="scheduled_arriv_time">
        </div>

        <div class="form-row align-items-left">
           <div class="col-auto">
            <button type="button" v-on:click="createpost ()" class="btn btn-primary">Submit</button>
           </div>
           <div class="col-auto">
            <a href="#/listflights/"><button type="button" class="btn btn-primary">Back</button></a>
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
  name: 'CreateFlight',
  data () {
    return {
      flight_id: null,
      airplane_id: null,
      cust_id: null,
      date_arriv: null,
      date_dep: null,
      scheduled_dep_time: null,
      scheduled_arriv_time: null,
      departure_airport: null,
      arrival_airport: null
    }
  },
  methods: {
    createpost () {
      axios.post('http://127.0.0.1:8000/myapp/flights/', {
        flight_id: Date.now(),
        airplane_id: this.airplane_id,
        cust_id: this.cust_id,
        date_arriv: this.date_arriv,
        date_dep: this.date_dep,
        scheduled_dep_time: this.scheduled_dep_time,
        scheduled_arriv_time: this.scheduled_arriv_time,
        departure_airport: this.departure_airport,
        arrival_airport: this.arrival_airport
      }).then((response) => { window.location.href = 'http://localhost:8080/#/listflights/' }).catch((e) => {
        console.log(e)
      })
    }
  }
}
</script>
