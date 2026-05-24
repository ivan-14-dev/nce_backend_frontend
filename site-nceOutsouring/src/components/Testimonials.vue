<template>
  <section class="py-20 bg-gray-50">
    <div class="max-w-6xl mx-auto px-6">
      <div class="text-center mb-16">
        <p class="text-nce-orange font-semibold uppercase tracking-widest text-sm mb-2">Retours clients</p>
        <h2 class="text-3xl md:text-4xl font-bold text-nce-dark">Ils nous font confiance</h2>
        <div class="h-1 w-20 bg-nce-orange mx-auto mt-4"></div>
      </div>

      <div class="grid md:grid-cols-3 gap-8">
        <div
          v-for="(temoignage, index) in listeTemoignages"
          :key="index"
          class="bg-white p-8 rounded-2xl shadow-md hover:shadow-xl transition-all duration-300 relative"
        >
          <!-- Quote icon -->
          <div class="absolute top-6 right-6 text-4xl opacity-10" :class="index % 2 === 0 ? 'text-nce-blue' : 'text-nce-orange'">
            "
          </div>
          <p class="text-gray-600 leading-relaxed italic mb-6">
            "{{ temoignage.texte }}"
          </p>
          <div class="flex items-center gap-3 pt-4 border-t border-gray-100">
            <div class="w-10 h-10 rounded-full flex items-center justify-center text-white font-bold text-sm"
              :class="index % 2 === 0 ? 'bg-nce-blue' : 'bg-nce-orange'">
              {{ temoignage.auteur.charAt(0) }}
            </div>
            <div class="text-left">
              <p class="font-bold text-nce-dark text-sm">{{ temoignage.auteur }}</p>
              <p class="text-gray-500 text-xs">{{ temoignage.ville }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const listeTemoignages = [
  {
    texte: "NCE Outsourcing a transformé notre service client à Douala. Leur réactivité est impressionnante.",
    auteur: "Responsable Logistique",
    ville: "PME Littoral"
  },
  {
    texte: "Une équipe bilingue et très professionnelle. Idéal pour nos clients basés à l'étranger.",
    auteur: "CEO",
    ville: "Hydrocare Group Yaoundé"
  },
  {
    texte: "Le suivi des appels est transparent et les rapports hebdomadaires nous aident beaucoup.",
    auteur: "Directeur Commercial",
    ville: "Hôtel Franco Yaoundé"
  }
]
</script>
