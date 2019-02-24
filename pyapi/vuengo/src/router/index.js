import Vue from 'vue'
import Router from 'vue-router'
import ListAirplanes from '@/components/ListAirplanes'
import HomePage from '@/components/HomePage'
import ListAirports from '@/components/ListAirports'
import ListCustomers from '@/components/ListCustomers'
import ListFlights from '@/components/ListFlights'
import CreateAirplane from '@/components/CreateAirplane'
import UpdateAirplane from '@/components/UpdateAirplane'
import UpdateAirport from '@/components/UpdateAirport'
import AddCustomer from '@/components/AddCustomer'
import AddAirport from '@/components/AddAirport'
import AddFlight from '@/components/AddFlight'
import AddAirplane from '@/components/AddAirplane'

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
      path: '/createairplane',
      name: 'CreateAirplane',
      component: CreateAirplane
    },
    {
      path: '/updateairplane',
      name: 'UpdateAirplane',
      component: UpdateAirplane
    },
    {
      path: '/updateairport',
      name: 'UpdateAirport',
      component: UpdateAirport
    }

  ]
})
