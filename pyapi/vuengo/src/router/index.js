import Vue from 'vue'
import Router from 'vue-router'
import ListAirplanes from '@/components/ListAirplanes'
import HomePage from '@/components/HomePage'
import ListAirports from '@/components/ListAirports'
import ListCustomers from '@/components/ListCustomers'
import ListFlights from '@/components/ListFlights'
import UpdateAirplane from '@/components/UpdateAirplane'
import UpdateAirport from '@/components/UpdateAirport'
import UpdateCustomer from '@/components/UpdateCustomer'
import UpdateFlight from '@/components/UpdateFlight'
import AddCustomer from '@/components/AddCustomer'
import AddAirport from '@/components/AddAirport'
import AddFlight from '@/components/AddFlight'
import AddAirplane from '@/components/AddAirplane'
import EditAirplane from '@/components/EditAirplane'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: HomePage
    },
    {
      path: '/listAirplanes',
      name: 'ListAirplanes',
      component: ListAirplanes
    },
    {
      path: '/listairports',
      name: 'ListAirports',
      component: ListAirports
    },
    {
      path: '/listcustomers',
      name: 'ListCustomers',
      component: ListCustomers
    },
    {
      path: '/listflights',
      name: 'ListFlights',
      component: ListFlights
    },
    {
      path: '/updateairplane',
      name: 'UpdateAirplane',
      component: UpdateAirplane
    },
    {
      path: '/updateairplane/:id',
      name: 'EditAirplane',
      component: EditAirplane
    },
    {
      path: '/updateairport',
      name: 'UpdateAirport',
      component: UpdateAirport
    },
    {
      path: '/updatecustomer',
      name: 'updateCustomer',
      component: UpdateCustomer
    },
    {
      path: '/updateflight',
      name: 'UpdateFlight',
      component: UpdateFlight
    },
    {
      path: '/addcustomer',
      name: 'AddCustomer',
      component: AddCustomer
    },
    {
    path: '/addairport',
    name: 'AddAirport',
    component: AddAirport
    },
    {
    path: '/addflight',
    name: 'AddFlight',
    component: AddFlight
    },
    {
    path: '/addairplane',
    name: 'AddAirplane',
    component: AddAirplane
    }
  ]
})
