<template>
  <div>
    <h1>Update Airplane</h1>
    <ul>
      <div class="form-group">
        <label class="col-form-label" for="airplaneID">Airplane Id:</label>
        <select class="form-control" v-model="airplane_id" id="airplane_id" placeholder="Airplane id">
          <option v-for="airplane in Airplanes" :key="airplane.airplane_id">
            {{airplane.airplane_id}}
          </option>
        </select>
    </div>
      <div class="form-group">
        <label class="col-form-label" for="manufac">Manufacturer:</label>
        <input type="text" v-model="manufacturer" class="form-control" placeholder="Boeing" id="manufacturer">
      </div>
      <div class="form-group">
        <label class="col-form-label" for="maxSeats">Max Seats:</label>
        <input type="text" v-model="max_seats" class="form-control" placeholder="280" id="max_seats">
      </div>
      <div class="form-group">
        <label class="col-form-label" for="typ">Type:</label>
        <input type="text" v-model="type" class="form-control" placeholder="A320" id="type">
      </div>

      <div class="form-row align-items-left">
         <div class="col-auto">
          <button type="button" v-on:click="createput ()" class="btn btn-primary" onclick="window.location.href='#/listairplanes'">Submit</button>
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
export default {
  name: 'UpdateAirplane',
  data () {
    return {
      airplane_id: null,
      manufacturer: null,
      max_seats: null,
      type: null,
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
    createput () {
      axios.put('http://127.0.0.1:8000/myapp/airplanes/' + this.airplane_id, {
        airplane_id: this.airplane_id,
        manufacturer: this.manufacturer,
        max_seats: this.max_seats,
        type: this.type
      }).then((response) => {}).catch((e) => { console.error(e) })
    },
    getObject: function (id) {
      for (airplane in this.Airplanes) {
        if (airplane.airplane_id == id) {
          return airplane;
        }
      }
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
