<template>
  <div>
  <br>
    <h1>Airport List</h1>
    <ul>
      <table class="table">
        <thead>
          <tr>
            <th></th>
            <th scope="col">Airport name</th>
            <th scope="col">City</th>
            <th scope="col">State</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="airport in Airports" :key="airport.airport_id">
            <td><router-link :to="{ name: 'EditAirport', params: {id: airport.airport_id} }"><button type="button" class="btn btn-primary">Edit</button></router-link></td>
            <td>{{airport.airport_name}}</td>
            <td>{{airport.city}}</td>
            <td>{{airport.state}}</td>
              <td><a href="#/listairports/"><button type="button" v-on:click="deleteAirport (airport.airport_id)" color="error" class="btn btn-danger">Delete</button></a></td>
          </tr>
        </tbody>
      </table>
      <hr>
      <a href="#/addairport/"><button type="button" class="btn btn-primary">Add Airport</button></a>
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
    },
    deleteAirport: function(id){
      axios.delete('http://127.0.0.1:8000/myapp/airports/'+id)
      .then((response)=>{
        this.getAirports();
      })
      .catch((error)=>{
        console.log(error);
      });
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
