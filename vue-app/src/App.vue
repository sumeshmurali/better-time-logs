<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'

import NavBar from './components/NavBar.vue'
import CategoryView from './components/CategoryView.vue'
import RecentTask from './components/RecentTasks.vue'
import AddTask from './components/AddTask.vue'
import AddCategory from './components/AddCategory.vue'

const baseUrl = location.host

const isAddTaskVisible = ref(false)
const isAddCategoryVisible = ref(false)
const recentTasks = ref(
  Array<{
    name: string
    type: string
    duration: string
    added: number
    description: string | null
  }>()
)
const categories = ref(
  Array<{ name: string; description: string | null; totalTimeSpend: number }>()
)
const categorySelected = ref('')

function addNewCategory(category: {
  name: string
  description: string | null
  totalTimeSpend: number
}) {
  categories.value.push(category)
}
function addNewTimeEntry(timeDetail: {
  type: string
  name: string
  duration: number
  description: string
  added: number
}) {
  let formattedTimeDetail = { ...timeDetail, duration: convertSecondsToHuman(timeDetail.duration) }
  recentTasks.value.push(formattedTimeDetail)
}

function convertHumanToSeconds(timeInStr: string): number | null {
  const normalizedTimeStr = timeInStr.split(' ').join('')
  var match = /^(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?$/.exec(normalizedTimeStr)
  if (match) {
    return (
      3600 * (parseInt(match[1]) || 0) + 60 * (parseInt(match[2]) || 0) + (parseInt(match[3]) || 0)
    )
  } else {
    return null
  }
}

function convertSecondsToHuman(time: number): string {
  let hours = ~~(time / 3600)
  time = time % 3600
  let minutes = ~~(time / 60)
  // we don't need the seconds part
  // time = time % 60
  return `${hours}h ${minutes}m`
}

recentTasks.value = [
  {
    name: 'Meeting with george',
    type: 'Meeting',
    duration: '1h',
    added: 1680849349693,
    description: null
  },
  {
    name: 'Meeting with david',
    type: 'Meeting',
    duration: '2h',
    added: 1680849340000,
    description: null
  },
  {
    name: 'Meeting with john',
    type: 'Meeting',
    duration: '1h',
    added: 1680849345000,
    description: null
  },
  {
    name: 'Meeting with Jane',
    type: 'Meeting',
    duration: '1h',
    added: new Date().valueOf(),
    description: null
  }
]

onMounted(() => {
  console.log(baseUrl)
  axios.get(`http://${baseUrl}/api/categories`).then(response => {
    categories.value = response.data
  }
  )
}
)
// )
// categories.value = [
//   {
//     name: 'Meeting',
//     description: null,
//     totalTimeSpend: 102
//   },
//   {
//     name: 'Development',
//     description: null,
//     totalTimeSpend: 80
//   },
//   {
//     name: 'Development',
//     description: null,
//     totalTimeSpend: 80
//   }
// ]
</script>

<template>
  <header>
    <NavBar></NavBar>
  </header>
  <div class="main">
    <div class="flex h-screen justify-between">
      <CategoryView
        :categories="categories"
        @add-category-btn-clicked="isAddCategoryVisible = true"
        @add-time-clicked="(category: string)=>{isAddTaskVisible = true; categorySelected = category}"
      ></CategoryView>
      <RecentTask :recent-tasks="recentTasks"></RecentTask>
    </div>
    <AddTask
      v-if="isAddTaskVisible"
      :category-selected="categorySelected"
      @close-time-entry-modal="isAddTaskVisible = false"
      @time-added="addNewTimeEntry"
    ></AddTask>
    <AddCategory
      v-if="isAddCategoryVisible"
      @close-btn-clicked="isAddCategoryVisible = false"
      @add-new-category="addNewCategory"
    ></AddCategory>
  </div>
</template>

<style>
@tailwind base;
@tailwind components;
@tailwind utilities;
</style>
