<template>
  <section class="py-16 bg-gray-50">
    <div class="max-w-4xl mx-auto px-6">
      <div class="text-center mb-12">
        <h2 class="text-3xl font-bold text-nce-dark">Discutons de votre projet</h2>
        <p class="text-gray-600 mt-2">Notre équipe basée à Yaoundé vous répond en moins de 24h.</p>
        <div class="h-1 w-20 bg-nce-orange mx-auto mt-2"></div>
      </div>

      <div class="bg-white rounded-2xl shadow-xl p-8 md:p-12 border border-gray-100">
        <div v-if="contactInfo.email || contactInfo.phone_cm || contactInfo.phone_fr" class="mb-6 text-sm text-gray-600">
          <div class="flex flex-col sm:flex-row sm:items-center gap-2 sm:gap-6">
            <div class="flex items-center gap-2">
              <span>✉️</span>
              <span class="font-semibold text-gray-800">{{ contactInfo.email || '—' }}</span>
            </div>
            <div class="flex items-center gap-2">
              <span>📞</span>
              <span class="font-semibold text-gray-800">{{ whatsappPhone || '—' }}</span>
            </div>
          </div>
        </div>

        <form @submit.prevent="envoyerFormulaire" class="space-y-6">
          <div class="grid md:grid-cols-2 gap-6">
            <div>
              <label class="block text-sm font-semibold text-nce-dark mb-2">Votre Nom</label>
              <input
                v-model="formulaire.nom"
                type="text"
                class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-nce-blue focus:border-transparent outline-none transition"
                placeholder="Ex: Yves Anelka"
                required
              />
            </div>
            <div>
              <label class="block text-sm font-semibold text-nce-dark mb-2">Nom de l'Entreprise</label>
              <input
                v-model="formulaire.entreprise"
                type="text"
                class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-nce-blue focus:border-transparent outline-none transition"
                placeholder="Ex: PME Sarl"
              />
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
              />
            </div>
            <div>
              <label class="block text-sm font-semibold text-nce-dark mb-2">Numéro de Téléphone (WhatsApp de préférence)</label>
              <input
                v-model="formulaire.telephone"
                type="tel"
                class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-nce-blue focus:border-transparent outline-none transition"
                placeholder="Ex: +237 6xx xx xx xx"
                required
              />
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

          <div v-if="submitError" class="text-sm text-red-600 font-semibold">
            {{ submitError }}
          </div>

          <div v-if="submitSuccess" class="text-sm text-green-700 font-semibold">
            {{ submitSuccess }}
          </div>

          <div class="flex flex-col sm:flex-row gap-4 pt-4">
            <button
              type="submit"
              :disabled="isSubmitting"
              class="flex-1 bg-nce-blue text-white font-bold py-3 px-6 rounded-lg transition shadow-md disabled:opacity-60 disabled:cursor-not-allowed"
            >
              <span v-if="isSubmitting">Envoi en cours…</span>
              <span v-else>Envoyer la demande</span>
            </button>

            <a
              v-if="whatsappHref"
              :href="whatsappHref"
              target="_blank"
              rel="noreferrer"
              class="flex-1 bg-green-500 text-white font-bold py-3 px-6 rounded-lg hover:bg-green-600 transition shadow-md flex items-center justify-center gap-2"
            >
              <span>💬</span> Discuter sur WhatsApp
            </a>

            <div v-else class="flex-1 bg-gray-200 text-gray-600 font-bold py-3 px-6 rounded-lg shadow-md flex items-center justify-center">
              WhatsApp indisponible
            </div>
          </div>
        </form>
      </div>
    </div>
  </section>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue'

const contactInfo = ref({
  email: '',
  phone_fr: '',
  phone_cm: '',
})

const isSubmitting = ref(false)
const submitError = ref('')
const submitSuccess = ref('')

const formulaire = ref({
  nom: '',
  entreprise: '',
  email: '',
  telephone: '',
  message: '',
})

const whatsappPhone = computed(() => contactInfo.value.phone_cm || contactInfo.value.phone_fr || '')

function toDigits(phone) {
  return (phone || '').replace(/[^\d]/g, '')
}

const whatsappHref = computed(() => {
  const digits = toDigits(whatsappPhone.value)
  return digits ? `https://wa.me/${digits}` : ''
})

async function loadContactInfo() {
  try {
    const res = await fetch('/api/contact-info/')
    if (!res.ok) throw new Error(`HTTP ${res.status}`)
    const data = await res.json()
    contactInfo.value = {
      email: data.email ?? '',
      phone_fr: data.phone_fr ?? '',
      phone_cm: data.phone_cm ?? '',
    }
  } catch {
    // On laisse le formulaire fonctionner même si la config ne charge pas.
  }
}

onMounted(loadContactInfo)

async function envoyerFormulaire() {
  submitError.value = ''
  submitSuccess.value = ''
  isSubmitting.value = true

  try {
    const entrepriseLine = formulaire.value.entreprise
      ? `Entreprise: ${formulaire.value.entreprise}\n`
      : ''

    const payload = {
      language: 'fr',
      full_name: formulaire.value.nom,
      email: formulaire.value.email,
      phone: formulaire.value.telephone,
      message: `${entrepriseLine}${formulaire.value.message}`.trim(),
    }

    const res = await fetch('/api/contact/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    })

    if (!res.ok) {
      const text = await res.text().catch(() => '')
      throw new Error(text || `HTTP ${res.status}`)
    }

    submitSuccess.value = 'Merci ! Votre demande a été envoyée. Nous vous répondrons rapidement.'
    formulaire.value = { nom: '', entreprise: '', email: '', telephone: '', message: '' }
  } catch (err) {
    submitError.value = 'Une erreur est survenue pendant l’envoi. Veuillez réessayer.'
  } finally {
    isSubmitting.value = false
  }
}
</script>
