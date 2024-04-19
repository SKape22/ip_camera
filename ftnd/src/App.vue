<template>
  <div class="container">
    <div class="form-container">
      <input type="text" v-model="url" placeholder="Enter URL" class="input-box">
      <input type="text" v-model="name" placeholder="Enter Name" class="input-box">
      <button @click="publish" class="publish-button">Publish</button>
      <iframe v-if="iframeSrc" :src="iframeSrc" width="100%" height="400px"></iframe>
    </div>
    <div class="list-container">
      <PathList ref="pathscomponent" />
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import PathList from './components/PathsList.vue';

export default {
  components: {
    PathList
  },
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
          this.$refs.pathscomponent.fetchPaths();
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
<style scoped>
body {
  margin: 0; /* Reset default margin */
  padding: 0; /* Reset default padding */
}

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background-color: #f5f5f5;
  border-radius: 10px;
  width: 100vw;
   /* Set width to 100vw for full-screen */
  margin: 0 auto; /* Center the container horizontally */
}

.form-container {
  margin-bottom: 20px;
}

.input-box {
  width: calc(100% - 40px); /* Subtract padding for full width */
  max-width: 400px; /* Limit maximum width for better readability */
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 20px;
  outline: none;
}

.publish-button {
  width: 100%;
  max-width: 400px; /* Limit maximum width for better readability */
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 20px;
  cursor: pointer;
  outline: none;
}

.publish-button:hover {
  background-color: #45a049;
}

.list-container {
  width: 100%;
}

/* Add more styles as needed */
</style>
