<template>
  <div>
    <h1>Airport List</h1>
    <ul>
      <table class="table">
        <thead>
          <tr>
            <th scope="col">Airport id</th>
            <th scope="col">Airport name</th>
            <th scope="col">City</th>
            <th scope="col">State</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="airport in Airports" :key="airport.airport_id">
            <th scope="row">{{airport.airport_id}}</th>
            <td>{{airport.airport_name}}</td>
            <td>{{airport.city}}</td>
            <td>{{airport.state}}</td>
          </tr>
        </tbody>
      </table>
      <button type="button" class="btn btn-primary">Create</button>
      <button type="button" class="btn btn-primary" onclick="window.location.href='#/updateairport'">Update</button>
      <button type="button" class="btn btn-primary">Delete</button>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'ListAirports',
  data () {
    return {
      Airports: []
    }
  },
  mounted () {
    this.getAirports()
  },
  methods: {
    getAirports () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/myapp/airports/'
      }).then(response => (this.Airports = response.data))
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
