<template>
  <div class="flex items-center space-x-4">
    <select v-model="selectedCategory" @change="updateSearchQuery" class="p-2 border rounded">
      <option value="">All Categories</option>
      <option v-for="category in categories" :key="category" :value="category">{{ category }}</option>
    </select>
    <input
      type="text"
      v-model="query"
      @input="updateSearchQuery"
      class="p-2 border rounded w-full"
      placeholder="Search..."
    />
  </div>
</template>

<script setup>
  import { useProductStore } from '@/store/productStore'
  import { ref, computed } from 'vue'

  // Initialize the product store
  const store = useProductStore()

  // Define a ref to hold the search query
  const query = ref(store.searchQuery)

  // Define a ref to hold the selected category
  const selectedCategory = ref('')

  // Computed property to get the list of categories from the store
  const categories = computed(() => store.categories)

  /**
   * Updates the search query and selected category in the store.
   * If a category is selected, it will filter by that category.
   * If no category is selected, it will remove the category filter.
   */
  const updateSearchQuery = () => {
    store.setSearchQuery(query.value)
    store.setCurrentCategories(selectedCategory.value ? [selectedCategory.value] : [])
  }
</script>

  