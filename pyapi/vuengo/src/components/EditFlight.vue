<template>
<div class="hero is-fullheight is-info is-bold">
<div class="hero-body">
<div class="container">
    <h1>Update Flight</h1>
    <div class="box">
    <ul>
      <div class="form-group">
        <label class="col-form-label" for="flight_">Flight Number:</label>
        <input type="text" readonly="" class="form-control" :placeholder="flight_id" id="flight_id">
      </div>
      <div class="form-group">
        <label class="col-form-label" for="airplane_id">Airplane Id:</label>
        <input type="text" v-model="airplane_id" class="form-control" :placeholder="flight.airplane_id" id="airplane_id">
      </div>
      <div class="form-group">
        <label class="col-form-label" for="cust_id">Customer Id:</label>
        <input type="text" v-model="cust_id" class="form-control" :placeholder="flight.cust_id" id="cust_id">
      </div>
      <div class="form-group">
        <label class="col-form-label" for="departure_airport">Departure Airport:</label>
        <input type="text" v-model="departure_airport" class="form-control" :placeholder="flight.departure_airport" id="departure_airport">
      </div>
      <div class="form-group">
        <label class="col-form-label" for="date_dep">Departure Date:</label>
        <input type="date" v-model="date_dep" class="form-control" :placeholder="flight.date_dep" id="date_dep">
      </div>
      <div class="form-group">
        <label class="col-form-label" for="scheduled_dep_time">Departure Time:</label>
        <input type="time" v-model="scheduled_dep_time" class="form-control" :placeholder="flight.scheduled_dep_time" id="scheduled_dep_time">
      </div>
      <div class="form-group">
        <label class="col-form-label" for="arrival_airport">Arrival Airport:</label>
        <input type="text" v-model="arrival_airport" class="form-control" :placeholder="flight.arrival_airport" id="arrival_airport">
      </div>
      <div class="form-group">
        <label class="col-form-label" for="date_arriv">Arrival Date:</label>
        <input type="date" v-model="date_arriv" class="form-control" :placeholder="flight.date_arriv" id="date_arriv">
      </div>
      <div class="form-group">
        <label class="col-form-label" for="scheduled_arriv_time">Arrival Time:</label>
        <input type="time" v-model="scheduled_arriv_time" class="form-control" :placeholder="flight.scheduled_arriv_time" id="scheduled_arriv_time">
      </div>

      <div class="form-row align-items-left">
         <div class="col-auto">
          <button type="button" v-on:click="createput ()" class="btn btn-primary">Submit</button>
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
  name: 'UpdateFlight',
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
      arrival_airport: null,
      flight: null
    }
  },
  created () {
    this.flight_id = this.$route.params.id
  },
  mounted () {
    this.getFlights()
  },
  methods: {
    getFlights () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/myapp/flights/' + this.flight_id
      }).then(response => (this.flight = response.data))
    },
    createput () {
      axios.put('http://127.0.0.1:8000/myapp/flights/' + this.flight_id, {
        flight_id: this.flight_id,
        aiplane_id: this.airplane_id,
        cust_id: this.cust_id,
        date_arriv: this.date_arriv,
        date_dep: this.date_dep,
        scheduled_dep_time: this.scheduled_dep_time,
        scheduled_arriv_time: this.scheduled_arriv_time,
        departure_airport: this.departure_airport,
        arrival_airport: this.arrival_airport
      }).then((response) => {window.location.href='#/listflights'}).catch((e) => { console.error(e) })
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
</style>
