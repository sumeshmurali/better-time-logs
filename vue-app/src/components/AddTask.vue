<script setup lang="ts">
import { ref, computed } from 'vue'

const props = defineProps<{
  categorySelected: string
}>();

const taskName = ref('');
const taskDescription = ref('');
const taskDurationRaw = ref('');

const taskDuration = computed(() => {
  return convertHumanToSeconds(taskDurationRaw.value)
})
// const preDefinedTimeDurations = ref(['15m', '30m', '1h', '2h'])

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

console.log('created')

const emit = defineEmits<{
  (e: 'close-time-entry-modal'): void
  (
    e: 'time-added',
    timeDetail: { type: string; name: string; duration: number; description: string; added: number }
  ): void
}>()

const vFocus = {
  mounted: (el: HTMLElement) => el.focus()
}
</script>

<template>
  <div
    id="task-entry-modal"
    tabindex="-1"
    aria-hidden="false"
    class="flex place-content-center fixed top-0 left-0 right-0 z-50 w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] md:h-full"
    @keydown.esc="emit('close-time-entry-modal')"
  >
    <div class="relative w-full h-full max-w-md md:h-auto">
      <!-- Modal content -->
      <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
        <button
          type="button"
          class="absolute top-3 right-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-800 dark:hover:text-white"
          data-modal-hide="authentication-modal"
          @click="emit('close-time-entry-modal')"
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
          <h3 class="mb-4 text-xl font-medium text-gray-900 dark:text-white">Add new task</h3>
          <form class="space-y-6" @submit.prevent>
            <div>
              <label
                for="default-search"
                class="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white"
                >New Category</label
              >
              <div class="relative">
                <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
                  <svg
                    aria-hidden="true"
                    class="w-5 h-5 text-gray-500 dark:text-gray-400"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
                    ></path>
                  </svg>
                </div>
                <input
                  type="search"
                  id="default-search"
                  class="block w-full p-4 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  placeholder="Meeting, Development..."
                  :value="categorySelected"
                  required
                />
                <button
                  type="submit"
                  class="text-white absolute right-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                >
                  Create
                </button>
              </div>
            </div>
            <div>
              <label
                for="taskName"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >Task Name</label
              >
              <input
                type="text"
                name="taskName"
                id="taskName"
                v-model="taskName"
                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                placeholder="Meeting with George"
                v-focus
                required
              />
            </div>
            <div class="space-y-2">
              <label
                for="taskDuration"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >Task Duration</label
              >
              <input
                type="text"
                name="taskDuration"
                id="taskDuration"
                :value="taskDuration ? convertSecondsToHuman(taskDuration) : ''"
                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                placeholder="1 hour"
                required
                readonly
              />
              <div class="inline-flex rounded-md shadow-sm" role="group">
                <button
                  type="button"
                  class="px-4 py-2 text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-l-lg hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-blue-500 dark:focus:text-white"
                  @click="taskDurationRaw = '15m'"
                >
                  15m
                </button>
                <button
                  type="button"
                  class="px-4 py-2 text-sm font-medium text-gray-900 bg-white border-t border-b border-r border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-blue-500 dark:focus:text-white"
                  @click="taskDurationRaw = '30m'"
                >
                  30m
                </button>
                <button
                  type="button"
                  class="px-4 py-2 text-sm font-medium text-gray-900 bg-white border-t border-b border-r border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-blue-500 dark:focus:text-white"
                  @click="taskDurationRaw = '1h'"
                >
                  1h
                </button>
                <button
                  type="button"
                  class="px-4 py-2 text-sm font-medium text-gray-900 bg-white border-t border-b border-r border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-blue-500 dark:focus:text-white"
                  @click="taskDurationRaw = '2h'"
                >
                  2h
                </button>
                <input
                  type="text"
                  name="customDuration"
                  id="customDuration"
                  class="px-4 w-full py-2 text-sm font-medium text-gray-900 bg-white border-t border-b border-r border-gray-200 rounded-r-md hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-blue-500 dark:focus:text-white"
                  placeholder="Custom (2h 30m)"
                  v-model="taskDurationRaw"
                />
              </div>
            </div>
            <div>
              <label
                for="taskDesc"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >Task Description [optional]</label
              >
              <input
                type="text"
                name="taskDesc"
                id="taskDesc"
                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                placeholder="Regarding the hiring process"
                v-model="taskDescription"
              />
            </div>
            <button
              type="submit"
              class="w-full text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
              @click="
                emit('time-added', {
                  type: categorySelected,
                  name: taskName,
                  duration: taskDuration ? taskDuration : 0,
                  description: taskDescription,
                  added: new Date().valueOf()
                }),
                emit('close-time-entry-modal')
              "
            >
              Add task
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
