import { createRouter, createWebHistory } from 'vue-router'
import Home from './pages/Home.vue'
import Services from './pages/Services.vue'
import Methodology from './pages/Methodology.vue'
import TeamPage from './pages/TeamPage.vue'
import TestimonialsPage from './pages/TestimonialsPage.vue'
import ContactPage from './pages/ContactPage.vue'
import PrivacyPolicy from './pages/PrivacyPolicy.vue'

const routes = [
  { path: '/', name: 'home', component: Home },
  { path: '/services', name: 'services', component: Services },
  { path: '/methodologie', name: 'methodologie', component: Methodology },
  { path: '/equipe', name: 'equipe', component: TeamPage },
  { path: '/temoignages', name: 'temoignages', component: TestimonialsPage },
  { path: '/contact', name: 'contact', component: ContactPage },
  { path: '/politique-de-confidentialite', name: 'privacy', component: PrivacyPolicy },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to) {
    if (to.hash) {
      return { el: to.hash, behavior: 'smooth' }
    }
    return { top: 0 }
  },
})

export default router
