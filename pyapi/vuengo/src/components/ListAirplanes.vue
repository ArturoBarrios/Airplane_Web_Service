
<template>
<div>
  <h1>Airplane List</h1>
  <ul>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">Airplane id</th>
          <th scope="col">Manufacturer</th>
          <th scope="col">Max Seats</th>
          <th scope="col">Type</th>
        </tr>
      </thead>
        <tbody>
          <tr v-for="airplane in Airplanes" :key="airplane.airplane_id">
            <th scope="row">{{airplane.airplane_id}}</th>
            <td>{{airplane.manufacturer}}</td>
            <td>{{airplane.max_seats}}</td>
            <td>{{airplane.type}}</td>
          </tr>
        </tbody>
    </table>
    <button type="button" class="btn btn-primary">Create</button>
    <button type="button" class="btn btn-primary">Updata</button>
    <button type="button" class="btn btn-primary">Delete</button>
  </ul>
</div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'ListAirplanes',
  data () {
    return {
      Airplanes: []
    }
  },
  mounted () {
    this.getAirplanes()
  },
  methods: {
    getAirplanes () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/myapp/airplanes/'
      }).then(response => (this.Airplanes = response.data))
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
