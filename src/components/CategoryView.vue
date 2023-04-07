<script lang="ts" setup>
// const emit = defineEmits([])

const props = defineProps<{
  categories: {name: string, totalTimeSpend: number}[]
}>()

const emit = defineEmits<{
  (e: 'add-category-btn-clicked'): void,
  (e: 'add-time-clicked', category: string): void
}>()

</script>

<template>
  <div class="flex flex-col w-3/4">
    <div class="h-fit self-end mr-20">
        <button
          class="text-black text-lg bg-green-300 hover:bg-green-800 hover:text-white p-5 rounded-lg pr-10 pl-10"
          @click="emit('add-category-btn-clicked')"
        >
          Add new category
        </button>
      </div>
    
    
    <div class="grid grid-cols-4">
      <h1 class="text-white text-xl" v-if="!props.categories">Start by adding a new category</h1>
      <button 
      v-else v-for="category in props.categories" :key="category.totalTimeSpend"
      class="block max-w-sm p-6 m-5 bg-white border border-gray-200 rounded-lg shadow hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700"
      @click="emit('add-time-clicked', category.name)"
      >
        <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{{category.name}}</h5>
        <p class="font-normal text-gray-700 dark:text-gray-400">{{ category.totalTimeSpend }}</p>
      </button>
    </div>
    
  </div>
</template>
