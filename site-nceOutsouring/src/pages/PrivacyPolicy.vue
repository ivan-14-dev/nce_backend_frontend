<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
  <div class="pt-44 pb-24 px-6 bg-gray-50 min-h-screen">
    <div class="max-w-4xl mx-auto bg-white rounded-2xl shadow-lg p-8 md:p-12">
      <h1 class="text-3xl md:text-4xl font-extrabold text-nce-dark mb-8">Politique de Confidentialité</h1>

      <p class="text-gray-600 mb-6">Dernière mise à jour : 17 mai 2026</p>

      <section class="mb-8">
        <h2 class="text-xl font-bold text-nce-dark mb-3">1. Introduction</h2>
        <p class="text-gray-700 leading-relaxed">
          NCE Outsourcing (« nous », « notre ») s'engage à protéger la vie privée de ses utilisateurs.
          Cette politique de confidentialité décrit comment nous collectons, utilisons et protégeons
          vos informations personnelles lorsque vous utilisez notre site web et nos services.
        </p>
      </section>

      <section class="mb-8">
        <h2 class="text-xl font-bold text-nce-dark mb-3">2. Données collectées</h2>
        <p class="text-gray-700 leading-relaxed mb-3">Nous pouvons collecter les informations suivantes :</p>
        <ul class="list-disc list-inside text-gray-700 space-y-2">
          <li>Nom et prénom</li>
          <li>Adresse e-mail</li>
          <li>Numéro de téléphone</li>
          <li>Nom de l'entreprise</li>
          <li>Toute information que vous nous transmettez via le formulaire de contact</li>
        </ul>
      </section>

      <section class="mb-8">
        <h2 class="text-xl font-bold text-nce-dark mb-3">3. Utilisation des données</h2>
        <p class="text-gray-700 leading-relaxed mb-3">Vos données sont utilisées pour :</p>
        <ul class="list-disc list-inside text-gray-700 space-y-2">
          <li>Répondre à vos demandes de contact et de devis</li>
          <li>Vous fournir nos services d'outsourcing</li>
          <li>Améliorer notre site web et nos services</li>
          <li>Vous envoyer des communications commerciales (avec votre consentement)</li>
        </ul>
      </section>

      <section class="mb-8">
        <h2 class="text-xl font-bold text-nce-dark mb-3">4. Protection des données</h2>
        <p class="text-gray-700 leading-relaxed">
          Nous mettons en place des mesures de sécurité techniques et organisationnelles
          appropriées pour protéger vos données personnelles contre tout accès non autorisé,
          modification, divulgation ou destruction.
        </p>
      </section>

      <section class="mb-8">
        <h2 class="text-xl font-bold text-nce-dark mb-3">5. Partage des données</h2>
        <p class="text-gray-700 leading-relaxed">
          Nous ne vendons, n'échangeons ni ne transférons vos informations personnelles
          à des tiers sans votre consentement, sauf si la loi l'exige.
        </p>
      </section>

      <section class="mb-8">
        <h2 class="text-xl font-bold text-nce-dark mb-3">6. Cookies</h2>
        <p class="text-gray-700 leading-relaxed">
          Notre site peut utiliser des cookies pour améliorer votre expérience de navigation.
          Vous pouvez configurer votre navigateur pour refuser les cookies, bien que cela
          puisse affecter certaines fonctionnalités du site.
        </p>
      </section>

      <section class="mb-8">
        <h2 class="text-xl font-bold text-nce-dark mb-3">7. Vos droits</h2>
        <p class="text-gray-700 leading-relaxed mb-3">Vous disposez des droits suivants :</p>
        <ul class="list-disc list-inside text-gray-700 space-y-2">
          <li>Droit d'accès à vos données personnelles</li>
          <li>Droit de rectification de vos données</li>
          <li>Droit à l'effacement de vos données</li>
          <li>Droit d'opposition au traitement de vos données</li>
          <li>Droit à la portabilité de vos données</li>
        </ul>
      </section>

      <section class="mb-8">
        <h2 class="text-xl font-bold text-nce-dark mb-3">8. Contact</h2>
        <p class="text-gray-700 leading-relaxed">
          Pour toute question concernant cette politique de confidentialité ou pour exercer
          vos droits, contactez-nous à :
          <a href="mailto:contact@nce-outsourcing.com" class="text-nce-blue hover:underline">contact@nce-outsourcing.com</a>
        </p>
      </section>

      <div class="mt-12 pt-8 border-t border-gray-200">
        <RouterLink to="/" class="inline-flex items-center text-nce-blue font-semibold hover:text-nce-orange transition">
          &larr; Retour à l'accueil
        </RouterLink>
      </div>
    </div>
  </div>
</template>
