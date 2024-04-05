<template>
  <div>
    <img :src="streamUrl" alt="Video Stream">
  </div>
</template>

<script>
export default {
  data() {
    return {
      streamUrl: 'http://localhost:5000/' // Update the URL with your Flask server URL
    };
  },
  mounted() {
    this.startStream();
  },
  methods: {
    startStream() {
      // Set the src attribute of the img tag to the stream URL
      this.streamUrl += '?t=' + Date.now(); // Append timestamp to URL to prevent caching
    }
  }
};
</script>
