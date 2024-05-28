<template>
  <div class="flex justify-center my-4">
    <button @click="prevPage" :disabled="currentPage === 1" class="px-4 py-2 mx-1 bg-gray-300 rounded">Previous</button>
    <button v-for="page in totalPages" :key="page" @click="setPage(page)" :class="{'bg-blue-500 text-white': currentPage === page}" class="px-4 py-2 mx-1 bg-gray-300 rounded">
      {{ page }}
    </button>
    <button @click="nextPage" :disabled="currentPage === totalPages" class="px-4 py-2 mx-1 bg-gray-300 rounded">Next</button>
  </div>
</template>

<script setup>
  import { defineEmits } from 'vue'

  // Define the props that the component receives
  const props = defineProps({
    totalPages: Number,
    currentPage: Number
  })

  // Define the events that the component will emit
  const emits = defineEmits(['page-changed'])

  /**
   * Navigate to the previous page if not already on the first page.
   */
  const prevPage = () => {
    if (props.currentPage > 1) {
      emits('page-changed', props.currentPage - 1)
    }
  }

  /**
   * Navigate to the next page if not already on the last page.
   */
  const nextPage = () => {
    if (props.currentPage < props.totalPages) {
      emits('page-changed', props.currentPage + 1)
    }
  }

  /**
   * Navigate to a specific page.
   * 
   * @param {number} page - The page number to navigate to.
   */
  const setPage = (page) => {
    emits('page-changed', page)
  }
</script>

