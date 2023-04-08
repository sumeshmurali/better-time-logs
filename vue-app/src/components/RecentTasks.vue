<script lang="ts" setup>
import { computed } from 'vue'
import moment from 'moment'

const props = defineProps<{
  recentTasks: { name: string; type: string; duration: string; added: number }[]
}>()

const sortedTasks = computed(() => {
  return [...props.recentTasks].sort((a, b) => b.added - a.added)
})
</script>

<template>
  <!-- Side menu -->
  <div class="relative h-screen grow-1 space-y-10 overflow-x-auto self-center">
    <h2
      class="m-4 text-3xl font-extrabold leading-none tracking-tight text-white md:text-4xl dark:text-white"
    >
      Recent Tasks
    </h2>
    <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
      <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
        <tr>
          <th scope="col" class="px-4 py-3">Name</th>
          <th scope="col" class="px-4 py-3">Type</th>
          <th scope="col" class="px-4 py-3">Time Spend</th>
          <th scope="col" class="px-4 py-3">Added</th>
        </tr>
      </thead>
      <tbody class="text-xs">
        <tr v-if="!sortedTasks" class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
          <td colspan="4" class="px-4 py-2">Your recent tasks will appear here</td>
        </tr>
        <tr
          v-else
          v-for="task in sortedTasks"
          :key="task.added"
          class="bg-white border-b dark:bg-gray-800 dark:border-gray-700"
        >
          <th
            scope="row"
            class="px-4 py-2 font-medium text-gray-900 whitespace-nowrap dark:text-white"
          >
            {{ task.name }}
          </th>
          <td class="px-4 py-2">{{ task.type }}</td>
          <td class="px-4 py-2">{{ task.duration }}</td>
          <td class="px-4 py-2">{{ moment(task.added).fromNow() }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
