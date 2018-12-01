<template>
  <div id="index">
    <Canvas :inputTexts="texts"></Canvas><br>
    <textarea v-model="texts" placeholder="input here"/><br>
    <p>texts: {{ texts }}</p>
  </div>
</template>

<script>
import Canvas from './Canvas.vue'
export default {
  components: {
    Canvas
  },
  data () {
    return {
      texts: ''
    }
  }
}
</script>
