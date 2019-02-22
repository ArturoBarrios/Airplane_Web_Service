<template>
  <div>
    <h1>Create Airplane</h1>
    <ul>
      <div class="form-group">
        <label class="col-form-label" for="airplaneID">Airplane id:</label>
        <input type="text" v-model="airplane_id" class="form-control" placeholder="Airplane id" id="airplane_id">
      </div>
      <div class="form-group">
        <label class="col-form-label" for="manufac">Manufacturer:</label>
        <input type="text" v-model="manufacturer" class="form-control" placeholder="Manufacturer" id="manufacturer">
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
      type: null
    }
  },
  methods: {
    createpost () {
      axios.post('http://127.0.0.1:8000/myapp/airplanes/', {
        airplane_id: this.airplane_id,
        manufacturer: this.manufacturer,
        max_seats: this.max_seats,
        type: this.type
      }).then((response) => {}).catch((e) => { console.error(e) })
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
