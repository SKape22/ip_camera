<template>
  <div>
    <input type="text" v-model="url" placeholder="Enter URL">
    <input type="text" v-model="name" placeholder="Enter Name">
    <button @click="publish">Publish</button>
    <iframe v-if="iframeSrc" :src="iframeSrc" width="100%" height="400px"></iframe>
  </div>
</template>

<script>

import axios from 'axios';
export default {
  data() {
    return {
      url: '',
      name: '',
      iframeSrc: null
    };
  },
  methods: {
    async publish() {
      try {
        const response = await axios.post('http://127.0.0.1:3000/publish', { url: this.url, name: this.name });
        if (response.data) {
          this.iframeSrc = 'http://127.0.0.1:8888/' + this.name;
        } else {
          // Handle error response from backend
          console.error('No link found in response');
        }
      } catch (error) {
        // Handle error
        console.error('Error publishing:', error);
      }
    }
  }
};
</script>
