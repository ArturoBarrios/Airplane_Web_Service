
<template>
<div>
  <h1>Airplane List</h1>
  <ul>
    <table class="table">
      <thead>
        <tr>
          <th></th>
          <th scope="col">Airplane Id</th>
          <th scope="col">Manufacturer</th>
          <th scope="col">Max Seats</th>
          <th scope="col">Type</th>
          <th></th>
        </tr>
      </thead>
        <tbody>
          <tr v-for="airplane in Airplanes" :key="airplane.airplane_id">
            <td><router-link :to="{ name: 'EditAirplane', params: {id: airplane.airplane_id} }"><button type="button" class="btn btn-primary">Edit</button></router-link></td>
            <th scope="row">{{airplane.airplane_id}}</th>
            <td>{{airplane.manufacturer}}</td>
            <td>{{airplane.max_seats}}</td>
            <td>{{airplane.type}}</td>
            <td><a href="#/listairplanes/"><button type="button" v-on:click="deleteAirplane (airplane.airplane_id)" color="error" class="btn btn-danger">Delete</button></a></td>
          </tr>
        </tbody>
    </table>
    <a href="#/addairplane/"><button type="button" class="btn btn-primary">Create</button></a>
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
    },
    deleteAirplane: function(id){
      axios.delete('http://127.0.0.1:8000/myapp/airplanes/'+id)
      .then((response)=>{
        this.getAirplanes();
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
