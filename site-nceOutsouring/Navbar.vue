<template>
  <nav class="fixed top-0 left-0 right-0 z-50 bg-white/95 backdrop-blur-sm shadow-md transition-all duration-300">
    <div class="max-w-7xl mx-auto px-6 py-3 flex justify-between items-center">
      <!-- Le Logo -->
      <a href="#accueil" class="flex items-center">
        <img src="/logoNCEOUTSOURCING.jpeg" alt="Logo NCE" class="h-12 w-auto">
      </a>

      <!-- Le Menu (Visible sur ordinateur) -->
      <ul class="hidden lg:flex gap-8 text-nce-dark font-medium text-sm uppercase tracking-wide">
        <li><a href="#accueil" class="hover:text-nce-blue transition py-2 border-b-2 border-transparent hover:border-nce-blue">Accueil</a></li>
        <li><a href="#services" class="hover:text-nce-blue transition py-2 border-b-2 border-transparent hover:border-nce-blue">Services</a></li>
        <li><a href="#methodologie" class="hover:text-nce-blue transition py-2 border-b-2 border-transparent hover:border-nce-blue">Méthodologie</a></li>
        <li><a href="#equipe" class="hover:text-nce-blue transition py-2 border-b-2 border-transparent hover:border-nce-blue">Équipe</a></li>
        <li><a href="#temoignages" class="hover:text-nce-blue transition py-2 border-b-2 border-transparent hover:border-nce-blue">Témoignages</a></li>
      </ul>

      <!-- Bouton Contact -->
      <a href="#contact" class="hidden md:inline-block bg-nce-orange text-white px-6 py-2.5 rounded-full font-bold text-sm hover:bg-orange-600 hover:shadow-lg transition-all duration-300">
        Nous contacter
      </a>

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
        <li><a href="#accueil" @click="menuOuvert = false" class="block py-2 hover:text-nce-blue transition">Accueil</a></li>
        <li><a href="#services" @click="menuOuvert = false" class="block py-2 hover:text-nce-blue transition">Services</a></li>
        <li><a href="#methodologie" @click="menuOuvert = false" class="block py-2 hover:text-nce-blue transition">Méthodologie</a></li>
        <li><a href="#equipe" @click="menuOuvert = false" class="block py-2 hover:text-nce-blue transition">Équipe</a></li>
        <li><a href="#temoignages" @click="menuOuvert = false" class="block py-2 hover:text-nce-blue transition">Témoignages</a></li>
        <li><a href="#contact" @click="menuOuvert = false" class="block py-2 text-nce-orange font-bold">Nous contacter</a></li>
      </ul>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue'

const menuOuvert = ref(false)
</script>
