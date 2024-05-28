<template>
  <div>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
      <div v-for="product in paginatedProducts" :key="product.id" class="border p-4 rounded">
        <img :src="product.images[0].image_url" alt="product.title" class="w-full h-48 object-cover mb-2" v-if="product.images.length > 0">
        <h2 class="text-xl font-bold">{{ product.title }}</h2>
        <p>{{ product.description }}</p>
        <p class="font-bold">$ {{ product.price }}</p>
      </div>
    </div>
    <Pagination :totalPages="totalPages" :currentPage="currentPage" @page-changed="handlePageChange" />
  </div>
</template>

<script setup>
  import { ref, computed } from 'vue'
  import { useProductStore } from '@/store/productStore'
  import Pagination from '@/components/Pagination.vue'

  // Initialize the product store
  const store = useProductStore()

  // Define a ref to hold the current page number
  const currentPage = ref(1)

  // Define the number of items to display per page
  const itemsPerPage = 6

  // Computed property to get the filtered list of products from the store
  const filterProducts = computed(() => store.filterProducts)

  /**
   * Computed property to get the paginated products based on the current page and items per page.
   * 
   * @returns {Array} - The paginated list of products.
   */
  const paginatedProducts = computed(() => {
    const start = (currentPage.value - 1) * itemsPerPage
    const end = start + itemsPerPage
    return filterProducts.value.slice(start, end)
  })

  /**
   * Computed property to calculate the total number of pages based on the number of filtered products.
   * 
   * @returns {number} - The total number of pages.
   */
  const totalPages = computed(() => {
    return Math.ceil(filterProducts.value.length / itemsPerPage)
  })

  /**
   * Handles the change of the current page.
   * 
   * @param {number} page - The new page number.
   */
  const handlePageChange = (page) => {
    currentPage.value = page
  }
</script>

