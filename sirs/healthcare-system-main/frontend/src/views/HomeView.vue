<template>
  <div class="home">
    <HelloWorld msg="Welcome to Hospital Saint Acutis hospital"/>
    <img alt="Hospital" style="width: 300px;height: 300px" :src="require('@/assets/hospitallogo.svg')">
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import HelloWorld from '@/components/HelloWorld.vue'; // @ is an alias to /src

export default defineComponent({
  name: 'HomeView',
  components: {
    HelloWorld,
  },
});
</script>
