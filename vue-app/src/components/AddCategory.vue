<script setup lang="ts">
import { ref } from 'vue'

// const emit = defineEmits(['close-btn-clicked'])
const emit = defineEmits<{
  (e: 'close-btn-clicked'): void
  (e: 'add-new-category', category: { name: string; description: string; totalTimeSpend: 0 }): void
}>()

const categoryName = ref('')
const categoryDescription = ref('')

console.log('created')

function addNewCategory(categoryName: string, categoryDescription: string) {
  if (!categoryName) {
    console.log('Failed to create category due to empty category name')
  }
  emit('add-new-category', {
    name: categoryName,
    description: categoryDescription,
    totalTimeSpend: 0
  })
  emit('close-btn-clicked')
}

const vFocus = {
  mounted: (el: HTMLElement) => el.focus()
}
</script>

<template>
  <div
    id="add-category-entry-modal"
    tabindex="-1"
    aria-hidden="true"
    class="flex place-content-center fixed top-0 left-0 right-0 z-50 w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] md:h-full"
    @keydown.esc="emit('close-btn-clicked')"
  >
    <div class="relative w-full h-full max-w-md md:h-auto">
      <!-- Modal content -->
      <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
        <button
          type="button"
          class="absolute top-3 right-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-800 dark:hover:text-white"
          data-modal-hide="authentication-modal"
          @click="emit('close-btn-clicked')"
        >
          <svg
            aria-hidden="true"
            class="w-5 h-5"
            fill="currentColor"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fill-rule="evenodd"
              d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
              clip-rule="evenodd"
            ></path>
          </svg>
          <span class="sr-only">Close modal</span>
        </button>
        <div class="px-6 py-6 lg:px-8">
          <h3 class="mb-4 text-xl font-medium text-gray-900 dark:text-white">
            Create new Category
          </h3>
          <form class="space-y-6" action="#" @submit.prevent>
            <div>
              <label
                for="categoryName"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >Category Name</label
              >
              <input
                type="text"
                name="categoryName"
                v-model="categoryName"
                id="categoryName"
                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                placeholder="Meeting"
                required
                v-focus
              />
            </div>
            <div>
              <label
                for="createCategory"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >Category Description [optional]</label
              >
              <input
                type="text"
                name="createCategory"
                id="createCategory"
                v-model="categoryDescription"
                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                placeholder="Place for all day today meetings"
              />
            </div>
            <button
              type="submit"
              class="w-full text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
              @click="(e) => addNewCategory(categoryName, categoryDescription)"
            >
              Create Category
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
