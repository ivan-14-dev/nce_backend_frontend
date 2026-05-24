<template>
  <nav class="fixed top-0 left-0 right-0 z-50 bg-white/95 backdrop-blur-sm shadow-md transition-all duration-300">
    <div class="max-w-7xl mx-auto px-6 py-3 flex justify-between items-center">
      <!-- Le Logo -->
      <RouterLink to="/" class="flex items-center">
        <img src="/logo2retouché.png" alt="Logo NCE" class="h-28 w-auto">
      </RouterLink>

      <!-- Le Menu (Visible sur ordinateur) -->
      <ul class="hidden lg:flex gap-8 text-nce-dark font-medium text-sm uppercase tracking-wide">
        <li><RouterLink to="/" class="hover:text-nce-blue transition py-2 border-b-2 border-transparent hover:border-nce-blue">Accueil</RouterLink></li>
        <li><RouterLink to="/services" class="hover:text-nce-blue transition py-2 border-b-2 border-transparent hover:border-nce-blue">Services</RouterLink></li>
        <li><RouterLink to="/methodologie" class="hover:text-nce-blue transition py-2 border-b-2 border-transparent hover:border-nce-blue">Méthodologie</RouterLink></li>
        <li><RouterLink to="/equipe" class="hover:text-nce-blue transition py-2 border-b-2 border-transparent hover:border-nce-blue">Équipe</RouterLink></li>
        <li><RouterLink to="/temoignages" class="hover:text-nce-blue transition py-2 border-b-2 border-transparent hover:border-nce-blue">Témoignages</RouterLink></li>
      </ul>

      <!-- Bouton Contact -->
      <RouterLink to="/contact" class="hidden md:inline-block bg-nce-orange text-white px-6 py-2.5 rounded-full font-bold text-sm hover:bg-orange-600 hover:shadow-lg transition-all duration-300">
        Nous contacter
      </RouterLink>

      <!-- Menu mobile -->
      <button @click="menuOuvert = !menuOuvert" class="lg:hidden text-nce-dark">
        <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path v-if="!menuOuvert" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
          <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
        </svg>
      </button>
    </div>

    <!-- Menu mobile déroulant -->
    <div v-if="menuOuvert" class="lg:hidden bg-white border-t border-gray-100 shadow-lg">
      <ul class="flex flex-col py-4 px-6 gap-4 text-nce-dark font-medium">
        <li><RouterLink to="/" @click="menuOuvert = false" class="block py-2 hover:text-nce-blue transition">Accueil</RouterLink></li>
        <li><RouterLink to="/services" @click="menuOuvert = false" class="block py-2 hover:text-nce-blue transition">Services</RouterLink></li>
        <li><RouterLink to="/methodologie" @click="menuOuvert = false" class="block py-2 hover:text-nce-blue transition">Méthodologie</RouterLink></li>
        <li><RouterLink to="/equipe" @click="menuOuvert = false" class="block py-2 hover:text-nce-blue transition">Équipe</RouterLink></li>
        <li><RouterLink to="/temoignages" @click="menuOuvert = false" class="block py-2 hover:text-nce-blue transition">Témoignages</RouterLink></li>
        <li><RouterLink to="/contact" @click="menuOuvert = false" class="block py-2 text-nce-orange font-bold">Nous contacter</RouterLink></li>
      </ul>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink } from 'vue-router'

const menuOuvert = ref(false)
</script>
