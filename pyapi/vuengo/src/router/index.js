import Vue from 'vue'
import Router from 'vue-router'
import ListAirplanes from '@/components/ListAirplanes'
import HomePage from '@/components/HomePage'
import ListAirports from '@/components/ListAirports'
import ListCustomers from '@/components/ListCustomers'
import ListFlights from '@/components/ListFlights'

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
    }
  ]
})
