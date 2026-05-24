<script setup>
import { RouterLink } from 'vue-router'
import Values from '../components/Values.vue'
</script>

<template>
  <!-- HERO SECTION - Image + Texte côte à côte -->
  <header class="relative bg-nce-dark pt-44 pb-20 px-6 overflow-hidden">
    <div class="absolute inset-0 bg-gradient-to-br from-nce-dark via-nce-dark to-blue-900 opacity-95"></div>
    <div class="absolute top-20 right-10 w-72 h-72 bg-nce-blue/10 rounded-full blur-3xl"></div>
    <div class="absolute bottom-10 left-10 w-96 h-96 bg-nce-orange/5 rounded-full blur-3xl"></div>

    <div class="relative max-w-7xl mx-auto grid md:grid-cols-2 gap-12 items-center">
      <!-- Texte -->
      <div>
        <p class="text-nce-orange font-semibold uppercase tracking-widest text-sm mb-4">Centre d'appels & Outsourcing</p>
        <h1 class="text-4xl md:text-5xl lg:text-6xl font-extrabold text-white leading-tight">
          Votre partenaire<br>
          <span class="text-nce-blue">Outsourcing</span> au Cameroun
        </h1>
        <p class="mt-6 text-gray-300 text-lg leading-relaxed">
          Multi-compétences et multicanal. Nous transformons votre relation client
          depuis Yaoundé pour conquérir le marché local et international.
        </p>
        <div class="mt-10 flex flex-col sm:flex-row gap-4">
          <RouterLink to="/services" class="bg-nce-orange text-white px-8 py-4 rounded-full font-bold hover:bg-orange-600 hover:shadow-xl transition-all duration-300 text-sm uppercase tracking-wide text-center">
            Découvrir nos services
          </RouterLink>
          <RouterLink to="/contact" class="border-2 border-white/30 text-white px-8 py-4 rounded-full font-bold hover:bg-white/10 transition-all duration-300 text-sm uppercase tracking-wide text-center">
            Demander un devis
          </RouterLink>
        </div>
      </div>
      <!-- Image -->
      <div class="hidden md:block">
        <img src="/photoFemmeCallcenter.jpg" alt="Opératrice call center" class="rounded-2xl shadow-2xl w-full h-auto object-cover max-h-[500px]">
      </div>
    </div>
  </header>

  <!-- CHIFFRES CLES - Barre de stats -->
  <section class="bg-white py-14 border-b border-gray-100">
    <div class="max-w-6xl mx-auto px-6 grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
      <div class="group">
        <p class="text-4xl md:text-5xl font-extrabold text-nce-blue group-hover:scale-110 transition-transform duration-300">+500</p>
        <p class="text-gray-600 mt-2 text-sm font-medium">Appels gérés / jour</p>
      </div>
      <div class="group">
        <p class="text-4xl md:text-5xl font-extrabold text-nce-orange group-hover:scale-110 transition-transform duration-300">98%</p>
        <p class="text-gray-600 mt-2 text-sm font-medium">Taux de satisfaction</p>
      </div>
      <div class="group">
        <p class="text-4xl md:text-5xl font-extrabold text-nce-blue group-hover:scale-110 transition-transform duration-300">24/7</p>
        <p class="text-gray-600 mt-2 text-sm font-medium">Disponibilité</p>
      </div>
      <div class="group">
        <p class="text-4xl md:text-5xl font-extrabold text-nce-orange group-hover:scale-110 transition-transform duration-300">3+</p>
        <p class="text-gray-600 mt-2 text-sm font-medium">Années d'expérience</p>
      </div>
    </div>
  </section>

  <!-- SECTION PRESENTATION - Image + Texte alternés -->
  <section class="py-20 px-6 bg-gray-50">
    <div class="max-w-7xl mx-auto grid md:grid-cols-2 gap-16 items-center">
      <!-- Image -->
      <div>
        <img src="/photoCallcenter.jpg" alt="Notre centre d'appels" class="rounded-2xl shadow-xl w-full h-auto object-cover max-h-[450px]">
      </div>
      <!-- Texte -->
      <div>
        <p class="text-nce-orange font-semibold uppercase tracking-widest text-sm mb-3">Qui sommes-nous</p>
        <h2 class="text-3xl md:text-4xl font-extrabold text-nce-dark leading-tight">
          Un centre de contact <span class="text-nce-blue">nouvelle génération</span>
        </h2>
        <p class="mt-6 text-gray-600 text-lg leading-relaxed">
          Basé à Yaoundé plus précisément à la montée Anne-rouge, NCE Outsourcing réunit une équipe qualifiée et passionnée,
          dédiée à l'excellence de la relation client. Nous accompagnons les entreprises
          locales et internationales avec des solutions sur-mesure.
        </p>
        <ul class="mt-6 space-y-3">
          <li class="flex items-start gap-3">
            <span class="w-6 h-6 bg-nce-blue/10 rounded-full flex items-center justify-center flex-shrink-0 mt-0.5">
              <span class="w-2 h-2 bg-nce-blue rounded-full"></span>
            </span>
            <span class="text-gray-700">Équipes formées aux standards internationaux</span>
          </li>
          <li class="flex items-start gap-3">
            <span class="w-6 h-6 bg-nce-blue/10 rounded-full flex items-center justify-center flex-shrink-0 mt-0.5">
              <span class="w-2 h-2 bg-nce-blue rounded-full"></span>
            </span>
            <span class="text-gray-700">Infrastructure technologique de pointe</span>
          </li>
          <li class="flex items-start gap-3">
            <span class="w-6 h-6 bg-nce-blue/10 rounded-full flex items-center justify-center flex-shrink-0 mt-0.5">
              <span class="w-2 h-2 bg-nce-blue rounded-full"></span>
            </span>
            <span class="text-gray-700">Suivi qualité et reporting en temps réel</span>
          </li>
          <li class="flex items-start gap-3">
            <span class="w-6 h-6 bg-nce-blue/10 rounded-full flex items-center justify-center flex-shrink-0 mt-0.5">
              <span class="w-2 h-2 bg-nce-blue rounded-full"></span>
            </span>
            <span class="text-gray-700">Flexibilité et adaptation à vos besoins</span>
          </li>
        </ul>
        <RouterLink to="/methodologie" class="inline-block mt-8 bg-nce-blue text-white px-7 py-3 rounded-full font-bold hover:bg-blue-700 hover:shadow-lg transition-all duration-300 text-sm uppercase tracking-wide">
          Notre méthodologie
        </RouterLink>
      </div>
    </div>
  </section>

  <!-- SERVICES APERCU -->
  <section class="py-20 px-6 bg-white">
    <div class="max-w-6xl mx-auto text-center mb-14">
      <p class="text-nce-orange font-semibold uppercase tracking-widest text-sm mb-3">Nos expertises</p>
      <h2 class="text-3xl md:text-4xl font-extrabold text-nce-dark">Des services adaptés à vos besoins</h2>
    </div>
    <div class="max-w-6xl mx-auto grid md:grid-cols-3 gap-8">
      <div class="bg-gray-50 rounded-2xl p-8 hover:shadow-xl hover:-translate-y-1 transition-all duration-300 border border-gray-100">
        <div class="w-14 h-14 bg-nce-blue/10 rounded-xl flex items-center justify-center mb-5">
          <svg class="w-7 h-7 text-nce-blue" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
        </div>
        <h3 class="text-xl font-bold text-nce-dark mb-3">Réception d'appels</h3>
        <p class="text-gray-600 leading-relaxed">Accueil téléphonique professionnel, gestion des demandes et support client multilingue.</p>
      </div>
      <div class="bg-gray-50 rounded-2xl p-8 hover:shadow-xl hover:-translate-y-1 transition-all duration-300 border border-gray-100">
        <div class="w-14 h-14 bg-nce-orange/10 rounded-xl flex items-center justify-center mb-5">
          <svg class="w-7 h-7 text-nce-orange" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8h2a2 2 0 012 2v6a2 2 0 01-2 2h-2v4l-4-4H9a1.994 1.994 0 01-1.414-.586m0 0L11 14h4a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2v4l.586-.586z"/></svg>
        </div>
        <h3 class="text-xl font-bold text-nce-dark mb-3">Émission d'appels</h3>
        <p class="text-gray-600 leading-relaxed">Prospection commerciale, prise de rendez-vous, enquêtes de satisfaction et relances.</p>
      </div>
      <div class="bg-gray-50 rounded-2xl p-8 hover:shadow-xl hover:-translate-y-1 transition-all duration-300 border border-gray-100">
        <div class="w-14 h-14 bg-nce-blue/10 rounded-xl flex items-center justify-center mb-5">
          <svg class="w-7 h-7 text-nce-blue" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
        </div>
        <h3 class="text-xl font-bold text-nce-dark mb-3">Services digitaux</h3>
        <p class="text-gray-600 leading-relaxed">Chat en ligne, gestion des e-mails, modération des réseaux sociaux et back-office.</p>
      </div>
    </div>
    <div class="text-center mt-12">
      <RouterLink to="/services" class="inline-block bg-nce-orange text-white px-8 py-4 rounded-full font-bold hover:bg-orange-600 hover:shadow-xl transition-all duration-300 text-sm uppercase tracking-wide">
        Voir tous nos services
      </RouterLink>
    </div>
  </section>

  <!-- CTA SECTION -->
  <section class="bg-gradient-to-r from-nce-blue to-blue-700 py-20 px-6">
    <div class="max-w-4xl mx-auto text-center">
      <h2 class="text-3xl md:text-4xl font-extrabold text-white">Prêt à externaliser vos services ?</h2>
      <p class="text-blue-100 mt-4 text-lg">Contactez-nous dès aujourd'hui pour un devis personnalisé et gratuit.</p>
      <RouterLink to="/contact" class="inline-block mt-8 bg-nce-orange text-white px-8 py-4 rounded-full font-bold hover:bg-orange-600 hover:shadow-xl transition-all duration-300 text-sm uppercase tracking-wide">
        Demander un devis gratuit
      </RouterLink>
    </div>
  </section>

  <!-- VALEURS -->
  <Values />
</template>
