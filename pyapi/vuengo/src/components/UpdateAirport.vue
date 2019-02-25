<template>
  <div>
    <h1>Update Airport</h1>
    <ul>
      <div class="form-group">
        <label class="col-form-label" for="airportID">Airport Id:</label>
        <select class="form-control" v-model="airport_id" id="airport_id" placeholder="Airport id">
          <option v-for="airport in Airports" :key="airport.airport_id">
            {{airport.airport_id}}
          </option>
        </select>
    </div>
      <div class="form-group">
        <label class="col-form-label" for="airportName">Airport Code:</label>
        <input type="text" v-model="airport_name" class="form-control" placeholder="CMH" id="airport_name">
      </div>
      <div class="form-group">
        <label class="col-form-label" for="citi">City:</label>
        <input type="text" v-model="city" class="form-control" placeholder="Columbus" id="city">
      </div>
      <div class="form-group">
        <label class="col-form-label" for="stat">State:</label>
        <input type="text" v-model="state" class="form-control" placeholder="Ohio" id="state">
      </div>

      <div class="form-row align-items-left">
         <div class="col-auto">
          <button type="button" v-on:click="createput ()" class="btn btn-primary" onclick="window.location.href='#/listairports'">Submit</button>
         </div>
         <div class="col-auto">
          <a href="#/listairports/"><button type="button" class="btn btn-primary">Back</button></a>
        </div>
      </div>

    </ul>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'UpdateAirport',
  data () {
    return {
      airport_id: null,
      airport_name: null,
      city: null,
      state: null,
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
    createput () {
      axios.put('http://127.0.0.1:8000/myapp/airports/' + this.airport_id, {
        airport_id: this.airport_id,
        airport_name: this.airport_name,
        city: this.city,
        state: this.state
      }).then((response) => {window.location.href='#/listairplane'}).catch((e) => { console.error(e) })
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
