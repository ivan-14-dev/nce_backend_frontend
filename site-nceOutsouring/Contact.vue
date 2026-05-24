<template>
  <section class="py-16 bg-gray-50">
    <div class="max-w-4xl mx-auto px-6">
      
      <div class="text-center mb-12">
        <h2 class="text-3xl font-bold text-nce-dark">Discutons de votre projet</h2>
        <p class="text-gray-600 mt-2">Notre équipe à Douala et Yaoundé vous répond en moins de 24h.</p>
        <div class="h-1 w-20 bg-nce-orange mx-auto mt-2"></div>
      </div>

      <div class="bg-white rounded-2xl shadow-xl p-8 md:p-12 border border-gray-100">
        <form @submit.prevent="envoyerFormulaire" class="space-y-6">
          
          <div class="grid md:grid-cols-2 gap-6">
            <div>
              <label class="block text-sm font-semibold text-nce-dark mb-2">Votre Nom</label>
              <input 
                v-model="formulaire.nom"
                type="text" 
                class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-nce-blue focus:border-transparent outline-none transition"
                placeholder="Ex: Paul Biya"
                required
              >
            </div>
            <div>
              <label class="block text-sm font-semibold text-nce-dark mb-2">Nom de l'Entreprise</label>
              <input 
                v-model="formulaire.entreprise"
                type="text" 
                class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-nce-blue focus:border-transparent outline-none transition"
                placeholder="Ex: PME Sarl"
                required
              >
            </div>
          </div>

          <div class="grid md:grid-cols-2 gap-6">
            <div>
              <label class="block text-sm font-semibold text-nce-dark mb-2">Adresse Email</label>
              <input 
                v-model="formulaire.email"
                type="email" 
                class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-nce-blue focus:border-transparent outline-none transition"
                placeholder="adresse@domaine.cm"
                required
              >
            </div>
            <div>
              <label class="block text-sm font-semibold text-nce-dark mb-2">Numéro de Téléphone (WhatsApp de préférence)</label>
              <input 
                v-model="formulaire.telephone"
                type="tel" 
                class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-nce-blue focus:border-transparent outline-none transition"
                placeholder="Ex: +237 6xx xx xx xx"
                required
              >
            </div>
          </div>

          <div>
            <label class="block text-sm font-semibold text-nce-dark mb-2">Votre Besoin</label>
            <textarea 
              v-model="formulaire.message"
              rows="4" 
              class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-nce-blue focus:border-transparent outline-none transition"
              placeholder="Décrivez brièvement vos besoins en gestion d'appels ou outsourcing..."
              required
            ></textarea>
          </div>

          <div class="flex flex-col sm:flex-row gap-4 pt-4">
            <button 
              type="submit" 
              class="flex-1 bg-nce-blue text-white font-bold py-3 px-6 rounded-lg hover:bg-blue-700 transition shadow-md"
            >
              Envoyer la demande
            </button>
            
            <a 
              href="https://wa.me/33768665712" 
              target="_blank"
              class="flex-1 bg-green-500 text-white font-bold py-3 px-6 rounded-lg hover:bg-green-600 transition shadow-md flex items-center justify-center gap-2"
            >
              <span>💬</span> Discuter sur WhatsApp
            </a>
          </div>

        </form>
      </div>

    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'

// On crée un objet "réactif" pour stocker ce que l'utilisateur tape
const formulaire = ref({
  nom: '',
  entreprise: '',
  email: '',
  telephone: '',
  message: ''
})

// Fonction appelée quand on clique sur "Envoyer la demande"
const envoyerFormulaire = () => {
  alert(`Merci ${formulaire.value.nom} ! Votre demande pour l'entreprise ${formulaire.value.entreprise} a été pré-enregistrée. (C'est ici que ton collègue back-end interviendra pour envoyer le vrai mail !)`)
  
  // On vide le formulaire après l'envoi
  formulaire.value = { nom: '', entreprise: '', email: '', telephone: '', message: '' }
}
</script>