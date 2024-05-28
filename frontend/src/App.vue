<template>
  <div class="container mx-auto p-4">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-4xl font-bold">Product List</h1>
      <SearchBar />
    </div>
    <div class="flex">
      <div class="w-1/4 pr-4">
        <CategoryFilter />
      </div>
      <div class="w-3/4">
        <ProductList />
      </div>
    </div>
  </div>
</template>

<script setup>
  import { useProductStore } from '@/store/productStore'
  import { onMounted } from 'vue'
  import SearchBar from '@/components/SearchBar.vue'
  import CategoryFilter from '@/components/CategoryFilter.vue'
  import ProductList from '@/components/ProductList.vue'

  // Initialize the product store
  const store = useProductStore()

  /**
   * Fetch the list of products from the store when the component is mounted.
   */
  onMounted(() => {
    store.fetchProducts()
  })
</script>


<style>
  .container {
    max-width: 1200px;
  }
</style>
