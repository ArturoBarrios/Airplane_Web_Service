<template>
  <div>
    <h1>Flight List</h1>
    <ul>
      <table class="table">
        <thead>
          <tr>
            <th scope="col">Flight id</th>
            <th scope="col">Airplane id</th>
            <th scope="col">Customer id</th>
            <th scope="col">Departure Time</th>
            <th scope="col">Arrival Time</th>
            <th scope="col">Departure Airport</th>
            <th scope="col">Arrival Airport</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="flight in Flights" :key="flight.flight_id">
            <th scope="row">{{flight.flight_id}}</th>
            <td>{{flight.airplane_id}}</td>
            <td>{{flight.cust_id}}</td>
            <td>{{flight.scheduled_dep_time}}</td>
            <td>{{flight.scheduled_arriv_time}}</td>
            <td>{{flight.departure_airport}}</td>
            <td>{{flight.arrival_airport}}</td>
          </tr>
        </tbody>
      </table>
      <a href="#/addflight/"><button type="button" class="btn btn-primary">Create</button></a>
      <button type="button" class="btn btn-primary">Updata</button>
      <button type="button" class="btn btn-primary">Delete</button>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'ListFlights',
  data () {
    return {
      Flights: []
    }
  },
  mounted () {
    this.getFlights()
  },
  methods: {
    getFlights () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/myapp/flights/'
      }).then(response => (this.Flights = response.data))
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
