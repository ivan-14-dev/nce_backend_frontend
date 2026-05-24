<script setup>
import Navbar from './components/Navbar.vue'
import { RouterLink } from 'vue-router'
import { onMounted, ref, computed } from 'vue'

const contactInfo = ref({
  email: '',
  phone_fr: '',
  phone_cm: '',
})

const whatsappPhone = computed(() => contactInfo.value.phone_cm || contactInfo.value.phone_fr || '')

async function loadContactInfo() {
  try {
    const res = await fetch('/api/contact-info')
    if (!res.ok) throw new Error(`HTTP ${res.status}`)
    const data = await res.json()
    contactInfo.value = {
      email: data.email ?? '',
      phone_fr: data.phone_fr ?? '',
      phone_cm: data.phone_cm ?? '',
    }
  } catch {
    // Footer reste affiché même si l'API ne charge pas.
  }
}

onMounted(loadContactInfo)
</script>

<template>
  <div class="min-h-screen bg-white">
    <Navbar />

    <RouterView />

    <!-- FOOTER -->
    <footer class="bg-nce-dark text-white pt-16 pb-8 px-6">
      <div class="max-w-6xl mx-auto">
        <div class="grid md:grid-cols-3 gap-12 mb-12">
          <!-- Colonne 1 : A propos -->
          <div>
            <img src="/logo2retouché.png" alt="Logo NCE" class="h-24 w-auto mb-4 brightness-200">
            <p class="text-gray-400 leading-relaxed text-sm">
              NCE Outsourcing, votre centre de contact multicanal basé à Yaoundé.
              Qualité, innovation et efficacité au service de votre croissance.
            </p>
          </div>
          <!-- Colonne 2 : Liens rapides -->
          <div>
            <h4 class="font-bold text-lg mb-4">Liens Rapides</h4>
            <ul class="space-y-2 text-gray-400 text-sm">
              <li><a href="/#services" class="hover:text-nce-orange transition">Nos Services</a></li>
              <li><a href="/#methodologie" class="hover:text-nce-orange transition">Méthodologie</a></li>
              <li><a href="/#equipe" class="hover:text-nce-orange transition">L'Équipe</a></li>
              <li><a href="/#temoignages" class="hover:text-nce-orange transition">Témoignages</a></li>
              <li><a href="/#contact" class="hover:text-nce-orange transition">Contact</a></li>
              <li><RouterLink to="/politique-de-confidentialite" class="hover:text-nce-orange transition">Politique de confidentialité</RouterLink></li>
            </ul>
          </div>
          <!-- Colonne 3 : Contact -->
          <div>
            <h4 class="font-bold text-lg mb-4">Contact</h4>
            <ul class="space-y-3 text-gray-400 text-sm">
              <li class="flex items-center gap-2">
                <span>📍</span> Yaoundé, Cameroun
              </li>
              <li class="flex items-center gap-2">
                <span>📞</span> {{ whatsappPhone || '+237 —' }}
              </li>
              <li class="flex items-center gap-2">
                <span>✉️</span> {{ contactInfo.email || '—' }}
              </li>
            </ul>
          </div>
        </div>
        <!-- Copyright -->
        <div class="pt-8 border-t border-gray-800 text-center text-sm text-gray-500">
          &copy; 2026 NCE Outsourcing. Tous droits réservés.
        </div>
      </div>
    </footer>
  </div>
</template>
