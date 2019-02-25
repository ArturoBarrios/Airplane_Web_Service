<template>
  <div>
    <h1>Update Airplane</h1>
    <ul>
      <div class="form-group">
        <label class="col-form-label" for="airplaneID">Airplane id:</label>
        <input type="text" readonly="" class="form-control" :placeholder="airplane_id" id="airplane_id">
      </div>
      <div class="form-group">
        <label class="col-form-label" for="manufac">Manufacturer:</label>
        <input type="text" v-model="manufacturer" class="form-control" :placeholder="airplane.manufacturer" id="manufacturer">
      </div>
      <div class="form-group">
        <label class="col-form-label" for="maxSeats">Max Seats:</label>
        <input type="text" v-model="max_seats" class="form-control" :placeholder="airplane.max_seats" id="max_seats">
      </div>
      <div class="form-group">
        <label class="col-form-label" for="typ">Type:</label>
        <input type="text" v-model="type" class="form-control" :placeholder="airplane.type" id="type">
      </div>

      <div class="form-row align-items-left">
         <div class="col-auto">
          <button type="button" v-on:click="createput ()" class="btn btn-primary" >Submit</button>
         </div>
         <div class="col-auto">
          <a href="#/listairplanes/"><button type="button" class="btn btn-primary">Back</button></a>
        </div>
      </div>

    </ul>
  </div>
</template>

<script>
import axios from 'axios'
import router from '../router'
export default {
  name: 'EditAirplane',
  data () {
    return {
      airplane_id: null,
      manufacturer: '',
      max_seats: null,
      type: null,
      airplane: null
    }
  },
  created () {
    this.airplane_id = this.$route.params.id
  },
  mounted () {
    this.getAirplanes()
  },
  methods: {
    getAirplanes () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/myapp/airplanes/' + this.airplane_id
      }).then(response => (
        this.airplane = response.data))
    },
    createput () {
      axios.put('http://127.0.0.1:8000/myapp/airplanes/' + this.airplane_id, {
        airplane_id: this.airplane_id,
        manufacturer: this.manufacturer,
        max_seats: this.max_seats,
        type: this.type
      }).then((response) => {window.location.href='#/listairplanes'}).catch((e) => { console.error(e) })
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
