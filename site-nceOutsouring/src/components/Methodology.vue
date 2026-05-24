<template>
  <section class="py-20 bg-gray-50">
    <div class="max-w-6xl mx-auto px-6">
      <!-- Titre de la section -->
      <div class="text-center mb-16">
        <p class="text-nce-orange font-semibold uppercase tracking-widest text-sm mb-2">Comment nous travaillons</p>
        <h2 class="text-3xl md:text-4xl font-bold text-nce-dark">Notre Méthodologie</h2>
        <div class="h-1 w-20 bg-nce-orange mx-auto mt-4"></div>
        <p class="mt-4 text-gray-600 max-w-2xl mx-auto">
          Une approche structurée en 4 étapes pour garantir des résultats concrets et mesurables.
        </p>
      </div>

      <!-- Les 4 étapes -->
      <div class="relative">
        <!-- Ligne de connexion (visible sur desktop) -->
        <div class="hidden lg:block absolute top-24 left-[10%] right-[10%] h-0.5 bg-gradient-to-r from-nce-blue via-nce-orange to-nce-blue"></div>

        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-10">

          <!-- Étape 1 -->
          <div class="relative text-center group">
            <div class="w-16 h-16 bg-nce-blue text-white rounded-full flex items-center justify-center text-2xl font-bold mx-auto mb-8 relative z-10 shadow-lg group-hover:scale-110 transition-transform duration-300">
              1
            </div>
            <div class="bg-white p-6 rounded-2xl shadow-md hover:shadow-xl transition-all duration-300 border border-gray-100">
              <h3 class="text-lg font-bold text-nce-dark mb-3">Analyse des Besoins</h3>
              <p class="text-gray-600 text-sm leading-relaxed">
                Nous étudions vos processus existants, identifions vos enjeux et définissons ensemble des objectifs clairs et atteignables.
              </p>
            </div>
          </div>

          <!-- Étape 2 -->
          <div class="relative text-center group">
            <div class="w-16 h-16 bg-nce-orange text-white rounded-full flex items-center justify-center text-2xl font-bold mx-auto mb-8 relative z-10 shadow-lg group-hover:scale-110 transition-transform duration-300">
              2
            </div>
            <div class="bg-white p-6 rounded-2xl shadow-md hover:shadow-xl transition-all duration-300 border border-gray-100">
              <h3 class="text-lg font-bold text-nce-dark mb-3">Mise en Place des Solutions</h3>
              <p class="text-gray-600 text-sm leading-relaxed">
                Nous déployons les outils, les équipes et les processus adaptés, avec une intégration fluide à votre environnement existant.
              </p>
            </div>
          </div>

          <!-- Étape 3 -->
          <div class="relative text-center group">
            <div class="w-16 h-16 bg-nce-blue text-white rounded-full flex items-center justify-center text-2xl font-bold mx-auto mb-8 relative z-10 shadow-lg group-hover:scale-110 transition-transform duration-300">
              3
            </div>
            <div class="bg-white p-6 rounded-2xl shadow-md hover:shadow-xl transition-all duration-300 border border-gray-100">
              <h3 class="text-lg font-bold text-nce-dark mb-3">Formation & Accompagnement</h3>
              <p class="text-gray-600 text-sm leading-relaxed">
                Nos agents sont formés à votre culture d'entreprise, vos produits et vos standards pour une représentation fidèle de votre marque.
              </p>
            </div>
          </div>

          <!-- Étape 4 -->
          <div class="relative text-center group">
            <div class="w-16 h-16 bg-nce-orange text-white rounded-full flex items-center justify-center text-2xl font-bold mx-auto mb-8 relative z-10 shadow-lg group-hover:scale-110 transition-transform duration-300">
              4
            </div>
            <div class="bg-white p-6 rounded-2xl shadow-md hover:shadow-xl transition-all duration-300 border border-gray-100">
              <h3 class="text-lg font-bold text-nce-dark mb-3">Suivi & Optimisation</h3>
              <p class="text-gray-600 text-sm leading-relaxed">
                Reporting régulier, KPIs en temps réel et amélioration continue pour maximiser votre performance durablement.
              </p>
            </div>
          </div>

        </div>
      </div>
    </div>
  </section>
</template>
