<template>
  <section class="py-20 bg-white">
    <div class="max-w-6xl mx-auto px-6 text-center">
      <div class="mb-16">
        <p class="text-nce-blue font-semibold uppercase tracking-widest text-sm mb-2">Qui sommes-nous</p>
        <h2 class="text-3xl md:text-4xl font-bold text-nce-dark">L'Équipe Dirigeante</h2>
        <div class="h-1 w-20 bg-nce-blue mx-auto mt-4"></div>
      </div>

      <div class="flex flex-wrap justify-center gap-12">
        <!-- Carte Directeur Général -->
        <div class="group bg-gray-50 p-8 rounded-2xl shadow-md hover:shadow-xl transition-all duration-300 w-80">
          <div class="w-36 h-36 bg-gray-200 rounded-full mx-auto mb-6 overflow-hidden border-4 border-nce-orange group-hover:border-nce-blue transition-colors duration-300">
            <img src="/PhotoMonsieurJordan.jpeg" alt="Directeur Général" class="w-full h-full object-cover">
          </div>
          <h3 class="text-xl font-bold text-nce-dark">LAJIE JORDAN</h3>
          <p class="text-nce-blue font-medium mt-1">Directeur Général</p>
          <p class="text-gray-500 text-sm mt-3">Visionnaire et stratège, il pilote la croissance de NCE Outsourcing avec ambition et rigueur.</p>
        </div>

        <!-- Carte Directrice des Opérations -->
        <div class="group bg-gray-50 p-8 rounded-2xl shadow-md hover:shadow-xl transition-all duration-300 w-80">
          <div class="w-36 h-36 bg-gray-200 rounded-full mx-auto mb-6 overflow-hidden border-4 border-nce-blue group-hover:border-nce-orange transition-colors duration-300">
            <img src="/Directrice_Operation.jpeg" alt="Directrice des Opérations" class="w-full h-full object-cover">
          </div>
          <h3 class="text-xl font-bold text-nce-dark">Nom de la DO</h3>
          <p class="text-nce-blue font-medium mt-1">Directrice des Opérations</p>
          <p class="text-gray-500 text-sm mt-3">Experte en management d'équipes, elle garantit l'excellence opérationnelle au quotidien.</p>
        </div>
      </div>
    </div>
  </section>
</template>
