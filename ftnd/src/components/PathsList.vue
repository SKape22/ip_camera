<template>
    <div class="path-list">
      <div class="cell"><h1>Paths</h1></div>
      <div class="path-table">
        <div class="path-header">
          <div class="header-cell">Path Name</div>
          <div class="header-cell">Conference Name</div>
          <div class="header-cell">Actions</div>
        </div>
        <div v-for="path in paths" :key="path.name" class="path-row">
          <div class="cell">{{ path.name }}</div>
          <div class="cell">{{ path.confName }}</div>
          <div class="cell">
            <button @click="fetchList(path.name)" class="fetch-button">Fetch Recordings</button>
          </div>
        </div>
      </div>
      <div class="video-section" v-if="options.length > 0">
        <select v-model="selectedOption" @change="playVideo" class="select-video">
          <option v-for="option in options" :value="option">{{ option.start }}</option>
        </select>
        <video controls v-if="videoSrc" class="video-player">
          <source :src="videoSrc" type="video/mp4" />
        </video>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        paths: [],
        options: [],
        selectedOption: null,
        videoSrc: null,
        selectedPath: null
      };
    },
    methods: {
      async fetchPaths() {
        try {
          const response = await axios.get('http://localhost:3000/paths');
          this.paths = response.data.items;
        } catch (error) {
          console.error('Error fetching paths:', error);
        }
      },
      async fetchList(confName) {
        try {
          const response = await axios.get(`http://localhost:3000/forward?path=${encodeURIComponent(confName)}`);
          this.options = response.data;
          this.selectedPath = confName;
        } catch (error) {
          console.error('Error fetching list:', error);
        }
      },
      playVideo() {
        if (this.selectedOption && this.selectedPath) {
          const url = `http://localhost:9996/get?path=${encodeURIComponent(this.selectedPath)}&start=${encodeURIComponent(this.selectedOption.start)}&duration=${this.selectedOption.duration}`;
          this.videoSrc = url;
        }
      }
    },
    mounted() {
      this.fetchPaths();
    }
  };
  </script>
  
  <style scoped>
  .path-list {
    width: 100%;
    max-width: 800px;
    margin: 0 auto;
  }
  
  .path-table {
    border: 1px solid #ccc;
    border-collapse: collapse;
    width: 100%;
  }
  
  .path-header {
    background-color: #f2f2f2;
    display: flex;
  }
  
  .header-cell {
    padding: 15px;
    border-bottom: 1px solid #ccc;
    flex: 1;
    text-align: center;
    font-weight: bold;
    color: #333;
  }
  
  .path-row {
    display: flex;
  }
  
  .cell {
    padding: 15px;
    border-bottom: 1px solid #ccc;
    flex: 1;
    text-align: center;
    color: black;
  }
  
  .fetch-button {
    padding: 8px 15px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 20px;
    cursor: pointer;
    outline: none;
  }
  
  .fetch-button:hover {
    background-color: #45a049;
  }
  
  .select-video {
    margin-top: 20px;
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 20px;
    outline: none;
  }
  
  .video-player {
    width: 100%;
  }
  /* Add more styles as needed */
  </style>
  