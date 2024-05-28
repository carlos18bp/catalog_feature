<template>
  <div class="mb-4">
    <h3 class="text-lg font-bold mb-2">Category</h3>
    <ul>
      <li v-for="category in categories" :key="category" class="cursor-pointer space-x-2">
        <input type="checkbox" :value="category" v-model="selectedCategories" @change="updateFilter">
        <label>{{ category }}</label>
      </li>
    </ul>
    <button @click="clearFilters" class="mt-4 px-4 py-2 bg-gray-300 rounded">Clear Filters</button>
  </div>
</template>

<script setup>
  import { useProductStore } from '@/store/productStore'
  import { ref, computed } from 'vue'

  // Initialize the product store
  const store = useProductStore()

  // Define a ref to hold the selected categories
  const selectedCategories = ref([])

  // Computed property to get the list of categories from the store
  const categories = computed(() => store.categories)

  /**
   * Updates the current categories in the store based on the selected categories.
   */
  const updateFilter = () => {
    store.setCurrentCategories(selectedCategories.value)
  }

  /**
   * Clears all the filters including the selected categories and search query.
   */
  const clearFilters = () => {
    selectedCategories.value = []
    store.setCurrentCategories([])
    store.setSearchQuery('')
  }
</script>

